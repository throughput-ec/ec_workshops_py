---
type: slides
---

<div><h1><img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module1/00_ec_slide1.png?raw=true" alt="EC Theme" width=25% align="left"/>Your First Notebook</h1></div>

---

### Create a New Notebook

- Navigate to the `binder` repository. Here is the [link]('https://mybinder.org/v2/gh/throughput-ec/ec-binder/HEAD').

- Under Notebooks, select R.
- This will create a new untitled notebook
  - Note the .ipynb extension (comes from "interactive Python notebook", the previous name before it was changed to Jupyter to reflect multi-language support)
  - Rename the notebook to "workshop.ipynb"

- Notebooks usually auto-save periodically, since we are in a Binder, all your new content will be lost once the Binder is closed.
- You can download your notebooks by clicking on File -> Download
---

## Working with Notebooks

A notebook consists of a series of "cells":
- **Code cells**: execute snippets of code and display the output
- **Markdown cells**: formatted text, equations, images, and more

By default, a new cell is always a code cell.

---

## Code Cells

To run a code cell, click in it and press `Shift-Enter` or press the Run button on the toolbar

This is an example of a Code Cell

```r
# Print something
print("Hello world", quote = FALSE)
```

```out
Hello world
```

---

## Markdown Cells

In Markdown cells, you can write plain text or add formatting and other elements with [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet). These include headers, **bold text**, *italic text*, hyperlinks, equations $A=\pi r^2$, inline code `print('Hello world!')`, bulleted lists, and more.


This is a markdown cell:
```
Hello~!
```
---


- To create a Markdown cell, select an empty cell and change the cell type from "Code" to "Markdown" in the dropdown menu on the toolbar
- To run a Markdown cell, press `Shift-Enter` or the Run button on the toolbar
- To edit a Markdown cell, you need to double-click inside it

---

## Other Notebook Basics

- Organizating cells &mdash; insert, delete, cut/copy/paste, move up/down, split, merge
- Running all cells or selected cell(s)
- Restarting and interrupting the kernel
- Caveat: Notebooks are nonlinear and running cells out of order can sometimes lead to unexpected results
  - It's good practice to periodically restart the kernel and run all cells, making sure that everything works as expected when you run the whole notebook from top to bottom
- Closing vs. shutting down a notebook &mdash; kernel process in background
- Re-opening a notebook after shutdown
  - All the code output is maintained from the previous kernel session
- Clear output of all cells or selected cell(s)

---

# Let's practice!
