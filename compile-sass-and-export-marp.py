import os

#
# SASS can't compile the pseudo-CSS import line for the default theme
# this is why we prepend the necessary line with this script
#
print("Compiling using system sass...", end=" ")
os.system("sass themes/cate-theme.scss themes/cate-theme.css")
print("done")

print("Attaching marp import lines...", end=" ")
with open(os.path.realpath("themes/cate-theme.css"), 'r') as content:
    previousContent = content.read()
with open(os.path.realpath("themes/cate-theme.css"), 'w') as content:
    newContent = '''/* @theme cate-theme */
@import "default";
'''    
    content.write(newContent + previousContent)
print("done")

print("Exporting marp presentation as html...", end=" ")
os.system("marp --theme ./themes/cate-theme.css example-presentation.md")
print("done")