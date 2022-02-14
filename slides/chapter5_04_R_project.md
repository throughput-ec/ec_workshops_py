---
type: slides
---

<div><h1><img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module1/00_ec_slide1.png?raw=true" alt="EC Theme" width=25% align="left"/> Lesson 4<br>Creating an RStudio Project</h1></div>

---

# What is an R Project?

- A directory containing a special file: `*.Rproj`

- Allows you to do the following:

  - use RStudio as a Git client

  - stop using `setwd()` to set your working directory

---

## Getting Started

- To create a new R Project: 
  * From the menu clcik on: 
      File -> New Project

<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module5/09_rproj.png?raw=true" alt="RProject" width=45% align="center">

---

- A pop up will show up.

<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module5/10_rproj.png?raw=true" alt="RProject" width=45% align="center">

---

## Creating RStudio projects

You can choose if you want to start a new project from:
- A GitHub repository
- An existing directory
- A completely new directory

---

## Creating from a completely new directory

- Click on `New Directory`

<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module5/11_rproj.png?raw=true" alt="RProject" width=45% align="center">

---

- Name the project and browse where would you like to set it up.

- Optionally, you can also set up a new git repository from here.

<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module5/12_rproj.png?raw=true" alt="RProject" width=45% align="center">

---

If you already have a git repository

1. Click on `Version Control`

<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module5/10_rproj.png?raw=true" alt="RProject" width=45% align="center">


2. Fill in:
  - Repository URL
  - Create Project as a subdirectory of
  
---

## Motivation - avoid using setwd()

So what’s wrong with:

```
setwd("~/USER/my_awesome_project/sub_project_1/data")
read_data("data_shared_with_everyone.csv")
```

- The chance of the `setwd()` command making the file paths work for anyone besides its author is 0%. Even the future author might have issues down the line.

- Your data analysis project is not self-contained and portable, which makes recreating your work impossible.

---

## Solution - Where is your working directory?

- After you created an R project, your working directory should now be the R Project's root directory. 

**Verify that by typing `getwd()` in your R console**

---

## Using RStudio to drive Git

- RStudio can be used as a Git GUI to `add`, `commit`, `push` and `pull` your changes. 

- This only works IF you have a `.Rproj` file.

- You can find the Git tab in the upper right panel of RStudio.

---

## Use `.Rproj` to open Rstudio

- You can double click on the `.Rproj` file of an RStudio project to open RStudio.

- When you do this, it also sets the currentl working directory to be the RStudio project's working directory.

---

## Organizing projects:

- A data analysis task can be organized using RStudio Project. 

- A suggestion on how to organize a project directory is:

```
data/
results/
scripts/
.Rproj
```
where `data/`, `results/`, and `scripts/` are directories as well.

- When you need to share an analysis, you can share the entire project over. 

- This will keep the structure of your project.

---

# Let's Practice What We Learned