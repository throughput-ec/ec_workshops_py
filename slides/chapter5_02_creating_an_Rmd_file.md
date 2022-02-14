---
type: slides
---

<div><h1><img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module1/00_ec_slide1.png?raw=true" alt="EC Theme" width=25% align="left"/> Lesson 2<br>Creating an R Markdown Document</h1></div>

---

## What is an R Markdown

An R Markdown document is very similar to a Jupyter Notebook.

It allows you to create and share documents that contain live code, equations, visualizations, and text.

<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module5/00_rstudio.png?raw=true" alt="Binder" width=45% align="center">

---

## Getting Started

- To create a new R Markdown: 
  * From the menu clcik on: 
      File -> New File -> R Markdown

<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module5/03_create_markdown.png?raw=true" alt="Binder" width=45% align="center">

---

- You will be asked to choose some settings for the R Markdown.
- For now, leave the default options. 
  - At the end of the module you will see which other outputs you could choose.

<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module5/04_create_markdown.png?raw=true" alt="Binder" width=45% align="center">

---

## Text and rendering R Markdown documents

In a RMarkdown document any line of text not in a code chunk will be formatted using Markdown. You can use HTML and LaTeX here to do more formatting. 

Unlike Jupyter, code and text do not render on their own; you will need to "knit" (render) the whole document in order to see the rendered output. 

Clicking the "Knit" button on the top to render the docuemnt:

<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module5/01_knit_button.png?raw=true" alt="Binder" width=45% align="center">
 
---

When you "knit" a Markdown (`.md`) file will be created and a new window will pop up with your rendered document (usually a `.pdf` or `.html` document). 

<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module5/02_rmd.png?raw=true" alt="Binder" width=45% align="center">

---

## Rendering Often

It is important to "knit" as often as you make important changes.

Otherwise, an error in a LaTeX equation or a code chunk will stop the rendering process resulting in an error. 

If you have a long document, it might be harder to identify what went wrong, so it is important to render often so that you will easily identify and fix errors. 

---

## Creating code chunks

Instead of code cells as in Jupyter, R Markdown has code chunks. 

To start a Code Chunk: 
- Write 3 backticks (\`\`\`) followed by curly braces containing the language engine you want to run (usually r): `{r}`. 
- If you want to use python, do `{python}`

- Code is entered on the lines below.

- To finish a Code Chunk, close it with 3 more backticks (\`\`\`).

---
<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module5/05_code_chunk.png?raw=true" alt="Binder" width=45% align="center">

- Code chunks are run when you knit the entire document. 
- The code in the chunk and the code output will be included in your rendered Markdown (`.md`) document. 

---

## Naming Code Chunks and Markdown sections

When you include Markdown headers (`#` symbol) R Studio automatically creates a pop-up-like menu for you to use to navigate the document:

<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module5/06_title_navigator.png?raw=true" alt="Binder" width=45% align="center">

---

You can also name Code Chunks by writing the desired name after the language engine inside the curly braces:
```{r my-name}
# This code chunk is named my-name
```

<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module5/07_code_navigator.png?raw=true" alt="Binder" width=45% align="center">

By clicking on any of the options in the pop-up-like menu, RStudio will navigate you to that section of the R Markdown document. 

WARNING: Do not duplicate code chunk names.

---

## Code Chunk Options

There are many code chunk options that you can set, for example:
- Choose whether a chunk is evaluated - allowing you to ignore code that may have errors and still render the Rmd file.
- Choose Whether to include the output in the rendered document
- Lots of ther [options](https://yihui.org/knitr/options/#chunk-options) document.

---
## Code Chunk Options

- Code Chunk options can be set at a global level or locally for a specific chunk.
- Global options are set in one chunk at the top of the document. For example:

```{r, setup, include=FALSE}
knitr::opts_chunk$set(
  comment = '', fig.width = 6, fig.height = 6
)
```

- Global chuncks are set by adding them as arguments to the function `knitr::opts_chunk$set(...)`

---

## Code Chunk Options

- Local chunk options are set by adding the options in the curly braces of a code chunk after the language engine and code chunk name. For example:

```{r correlation no warning, warning = FALSE}
cor( c( 1 , 1 ), c( 2 , 3 ) )
```

- Separate multiple options in a code chunk with a comma. 

---

## Document output options

- Besides Markdown text and code chunks, you can add an optional YAML header to your document.

- Specify a YAML header surrouding it with `---`

- Include:
  - title
  - author
  - output
  - etc
---

## Example YAML Header**

~~~
 ---
 title: "Finding coordinates in a map"
 author: "My Name"
 date: "December 07, 2021"
 output: html
 ---
~~~

---

Output options include:

- `output: github_document`
- `output: html_document`
- `output: pdf_document`
- [others](https://bookdown.org/yihui/rmarkdown/output-formats.html)