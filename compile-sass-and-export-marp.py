import os
import sys
from shutil import which

#
# Why use this script instead of compiling by hand?
#
# - SASS can't handle the pseudo-CSS import line for the default theme
# this is why we prepend the necessary line here
#
# - We can modify a flag in SCSS before compiling
#

# Constants

negativeInput = ["n", "no"]
positiveInput = ["y", "yes"]

marpPath = "marp"
sassPath = "sass"

dependencies = [marpPath, sassPath]

# Utilities

# Check if a command/tool can be called from the system's terminal
def is_tool(name):
    return which(name) is not None

# Dependency check

for dependency in dependencies:
    if is_tool(dependency) != True:
        raise ImportError(f"{dependency} does not seem to be installed or available as a command in PATH.")

# Input markdown File

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = input("What file would you like to convert? ")

if os.path.isfile(filename) == False:
    raise FileNotFoundError

# Options for SASS compile

if "--all-default" in sys.argv:
    optionFadeInactiveBulletsToGray = False
else:
    optionFadeInactiveBulletsToGray = input("Would you like inactive bullet points to be grayed out (y/N)? ")
    if optionFadeInactiveBulletsToGray.lower() in positiveInput:
        optionFadeInactiveBulletsToGray = True
    else:
        optionFadeInactiveBulletsToGray = False

# Get SCSS
with open(os.path.realpath("themes/cate-theme.scss"), 'r') as file:
  scssfile = file.read()
# Replace string
if optionFadeInactiveBulletsToGray:
    scssfile = scssfile.replace('$fade-inactive-bullets-to-gray: false;', '$fade-inactive-bullets-to-gray: true;')

with open(os.path.realpath("themes/temp.scss"), 'w') as file:
  file.write(scssfile)

# SASS Compile

print("Compiling using dependency sass...", end=" ")
os.system(f"{sassPath} themes/temp.scss themes/cate-theme.css")
os.remove("themes/temp.scss")
print("done")

print("Attaching marp import lines to compiled css...", end=" ")
with open(os.path.realpath("themes/cate-theme.css"), 'r') as content:
    previousContent = content.read()
with open(os.path.realpath("themes/cate-theme.css"), 'w') as content:
    newContent = '''/* @theme cate-theme */
@import "default";
'''
    content.write(newContent + previousContent)
print("done")

print("Exporting presentation as html using dependency marp...", end=" ")
os.system(f"{marpPath} --theme ./themes/cate-theme.css {filename}")
print("done")