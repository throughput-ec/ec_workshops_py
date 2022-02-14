---
type: slides
---

<div><h1><img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module1/00_ec_slide1.png?raw=true" alt="EC Theme" width=25% align="left"/> Lesson 1<br>Introduction to RStudio</h1></div>

---

# What is RStudio?

RStudio is an IDE (integrated development environment) mainly used for R.

It includes tools for:
- linting
- code completion
- debugging.

You can also work with Rmd files which enable a notebook-like functionality.
You can use other language engines, such as Python.

---

## Opening RStudio

If you open *RStudio* you will encounter the following screen:

<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/00_rstudio.png?raw=true" alt="Binder" width=45% align="center">

---

## Running Rscripts in RStudio

- Launch this [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/throughput-ec/ec-binder/main?urlpath=rstudio) in a new tab and follow these steps:

- Creating a new R script: 
  * From the menu clcik on: 
      File -> New File -> R Script

- Write a simple R code the document that shows up in the editor:
```r
4 + 5
```

- Run your code clicking on the "Source" button (upper right-hand side) to run the entire document.
- To run a single line, type Ctrl+Enter (Command+Return) to run the current line or highlighted code

--

## Code output

When running R code in the console output ends up in one of to places, depending on the type of output:

* Textual output: printed to the console.

* Graphical output: displayed in the Files/Help/Plots panel *usually* at the bottom right of the Window.

---

## Getting help in RStudio

If you want to know more about what a function or package does, type a `?` followed by the function's name

```
?function_name
```

Help is going to be available in the bottom right pane of RStudio.

---

## The Files Pane Importance

When you open in RStudio a `.R` or `.Rmd` file the RStudio, the current working directory is **not** neccesarily the project working directory, or the directory of the file you opened.

---

## Where am I? (or the files pane)

**EVERY SESSION** you need to tell RStudio what your `working directory` is. Especially if you are loading different files.

You can find out where you are by:

1. typing `getwd()` in the console

2. In the files panel, click the cog/More button and then click "Go To Working Directory"

---

## Setting your Working Directory

Set your working directory to the root directory of the Git repository you are working in!

You can set the working directory using the following 3 ways:

1. In the Session menu, click Set Working Directory and then Choose Directory. Navigate the opened file browser to choose the directory. 

2. In the files panel, navigate the file structure to where you want the working directory to be. Then click the cog/More button and then click "Set As Working Directory"

3. type `setwd("PATH")` in the console.

---

## Setting the working directory is important!

If you are working in RStudio and you start feeling lost, you probably forgot to set the working directory.

We will see how to create R Projects later which will help us keep our directory clean.

**Suggestion:** Try using the [here](https://github.com/jennybc/here_here) package instead.

---

# Let's Practice!
