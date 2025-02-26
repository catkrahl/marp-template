# Marp Template CaT / cate

## ATTENTION: compiling scss to css 
* the following two lines are needed in the theme.css
  * /* @theme cate-theme */
    @import "default";

This repo bundles our **CaT/cate presentation theme** for marp together with a way to quickly change style code and export a standalone html presentation by controlling the sass compiler and marp cli export through a python script.

## Making a presentation

### Front Matter

To make sure that marp (and VSCode if used for a live preview) can properly handle this theme, you have to start your presentation markdown file with some front matter.

Header, footer and pagination can be set to your liking.

```markdown
---

marp: true
theme: cate-theme
paginate: false
header: ILIAS DevConf September 2023
footer: No ILIAS on a dead planet.

---
```

### New Slide

In marp, you write your presentation in a markdown document. Use `---` to mark the break for the next slide.

```markdown
Slide 1

---

Slide 2
```

### Use Markdown

On the slide, you can use markdown for some visual structure:

```markdown
# Headline Slide 1

This is just a normal paragraph.

* some
* bullet
* points

---

Slide 2
```

### Special Slides

This cate-theme has special slide templates for the title and chapter slides that can be selected for the current slide like so:

```markdown
<!-- _class: title-01 -->

# **Headline on this cover slide**
```

The underscore in `_class` scopes this template style for this current slide only.

**The `**` bold markdown around the entire headline text is needed so the headline css styling works correctly on this slide template.** In the future the python script may be able to enforce this, but for now, you will have to make sure they are there!

### Images

See example.md for some example code of how to deal with images.

If you add more images you may want to place them in img/.

### Live Preview

You can use Visual Studio Code (https://snapcraft.io/code) and the marp extension (https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode) to get a live preview while you edit your presentation.

You can branch this repo as a basis, because you need themes/, img/, fonts/, .vscode/ and their contents for the cate-theme to work.

## Compiling and exporting in Ubuntu

Python3 should already be pre-installed on Ubuntu.

**You need to download and unzip the following dependencies:**
* Dart SASS: https://github.com/sass/dart-sass/releases
* Marp CLI: https://github.com/marp-team/marp-cli/releases

**And make the program files available through PATH variables to be called with 'sass' and 'marp' respectively from the terminal** e.g. by placing them in or linking to them from ~/.local/bin (just the local user) or usr/local/bin (all users).

Then you can use the Python script `compile-sass-and-export-marp.py` to both refresh the style code and to export a html version of the presentation.

Compiling themes/cate-theme.scss without using the script is not recommended as the css needs a line attached to the beginning to work in marp.

```bash
python3 compile-sass-and-export-marp.py
```

You will be prompted to give the following inputs:
* enter markdown file name
* set if inactive bullet points should fade to gray true/false (modifies scss)

You can also give the file name when calling the script and take all default options like so:

```bash
python3 compile-sass-and-export-marp.py example.md --all-default
```

The html version of the presentation needs img/ and fonts/ next to it to be displayed correctly. The folder themes/ is no longer needed as the style code is embedded in the html file.
