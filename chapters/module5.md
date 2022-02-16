---
title: 'Module 5: Working with RMarkdown'
description:
  'In this module you will create, edit and run reproducible R code documents using RMarkdown.
  '
prev: /module4
next: /module6
type: chapter
id: 5
---

<exercise id="0" title="Learning Outcomes" type="slides">

<slides source="chapter5_00_learning_outcomes">
</slides>

</exercise>

<exercise id="1" title="Introduction to RStudio" type="slides">

<slides source="chapter5_01_introduction_to_Rstudio">
</slides>

</exercise>

<exercise id="2" title="Creating an Rmd file" type="slides">

<slides source="chapter5_02_creating_an_Rmd_file">
</slides>

</exercise>

<exercise id="3" title="Creating a Presentation" type="slides">

<slides source="chapter5_03_creating_a_presentation">

</slides>

</exercise>

<exercise id="4" title="My First Presentation Task">

1. Go to [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/throughput-ec/ec-binder/main?urlpath=rstudio)

2. Open a new Rmd file.

3. Copy and paste the following text

````markdown
---
title: "My First Deck of Slides"
author: "My Name"
date: "12/12/2021"
output: ioslides_presentation
---

# Title Slide

---
## Slide with Bullets

- Bullet 1
- Bullet 2
- Bullet 3

---
No Header Slide

---
## Slide with R Output

This is some code

```{r code demo, echo = TRUE}
x <- 5
y <- 10
(x <- x + y)
``` 
````



4. Click on the Preview / Knit button.

**Remember:** Do not leave a white space between the `---` and the next line


</exercise>

<exercise id="5" title="Creating an R Project" type="slides">

<slides source="chapter5_04_R_project">
</slides>

</exercise>

<exercise id="6" title="First Steps in R">

For more exercises in R, visit our [EC Workshops R Version](https://throughput-ec.github.io/ec-workshops/module5)


</exercise>

<exercise id="11" title="Summary and Conclusions" type="slides">

<slides source="chapter5_05_summary_and_conclusions">

</slides>

</exercise>

