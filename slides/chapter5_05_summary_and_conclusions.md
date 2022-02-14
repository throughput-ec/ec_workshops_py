---
type: slides
---

<div><h1><img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module1/00_ec_slide1.png?raw=true" alt="EC Theme" width=25% align="left"/> What We Learned</h1></div>

--- 

## RStudio

- RStudio is an integrated development environment (IDE) mainly for R. 
- It includes 4 panels, including:
  - an editor that supports direct code execution
  - tools for plotting, history, debugging
  - a console.

- It allows us to create Rmd files which work as Jupyter Notebooks
- We can create self contained code projects using R projects.

---

## An R Markdown File

- A file format for making dynamic documents with R. 
- An R Markdown document is written in markdown (an easy-to-write plain text format) and contains chunks of embedded R code and markdown text.
- R Markdown files are the source code for reproducible documents. You can transform an R Markdown file in two ways:
  * `knit` - knitr will run each chunk of code in the document and append the results of the code to the document next to the code chunk. This workflow facilitates reproducible reports.

  * `convert` - The rmarkdown package will use the pandoc program to transform the file into a new format such as: HTML, PDF, or Microsoft Word file. This is defined in the YAML header.
---

# Let's practice what we learned!