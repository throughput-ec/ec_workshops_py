---
title: 'Module 4: Introduction to Binder'
description:
  'This module will teach you how to use the Binder properly guaranteeing reproducibility of your notebooks and repositories.
  '
prev: /module3
next: /module5
type: chapter
id: 4
---

<exercise id="0" title="Learning Outcomes" type="slides">

<slides source="chapter4_00_learning_outcomes">
</slides>

</exercise>

<exercise id="1" title="Introduction to Binder" type="slides">

<slides source="chapter4_01_introduction_to_binder">
</slides>

</exercise>

<exercise id="2" title="Trivia Time!">

A Binder allows us to:

<choice id="1">
<opt text="Reproduce the environment we are working in and allow others to run our Jupyter Notebooks or R scripts."  correct="true">

Good job!

</opt>

<opt text="Deploy code, graphs, and text and allow others to run our code." correct = "true">

This is also correct!

</opt>

<opt text="Teach the users of our code how to install dependencies">

A Binder helps the useres run the code without having to figure out all the dependencies.

</opt>
</choice>

True or False? 

<choice id="2">
<opt text= "Sharing a Binder repository with another user is complicated" >
 
You only need to give them a link and they will be able to run your code.

</opt>

<opt text="With Binder, you can spend the time understanding the code rather than  understanding how to set up the environment to run the code." correct="true">

That's correct! Binder allows us to focus on what matters!

</opt>

</choice>

</exercise>

<exercise id="3" title="What Does a Binder Need?" type="slides">

<slides source="chapter4_02_what_does_a_binder_repo_need">
</slides>

</exercise>

<exercise id="4" title="Trivia Time!">

In order to create a Binder you need:

<choice id="1">
<opt text="Any Git repository, a file to share, a password.">

You need a public repository - not any repository.

</opt>

<opt text="A public Git repository, a file to share, security measures, and configuration files, a Binder Hub" correct="true">

This is the correct answer!

</opt>

<opt text="A file to share, security measures, a Binder Hub">

You are still missing some items.

</opt>
</choice>

True or False? Select the answers that are True.

<choice id="2">
<opt text= "Binder mimics human behaviour in how we clone our repositories." correct="true">
 
That's right! The process a Binder goes through is similar to what you would do when cloning a repo, looking for configuration files, install the dependencies and start a Jupyter Notebook / RStudio session.

</opt>

<opt text="With Binder, your users have to write a lot of configuration files before being able to see your work.">

That's not correct. Binder helps your users focus only on the code that you wrote rather than having them worry about installations.

</opt>

</choice>

</exercise>



<exercise id="5" title="Setting Up a Python Binder" type="slides">

<slides source="chapter4_03_python_repository">
</slides>

</exercise>

<exercise id="6" title="environment.yml template" >

Use this template as your `environment.yml` file
If you are not using `pypi` only packages, then remove the two last lines.

```
name: my-example-environment
channels:
  - conda-forge
dependencies:
  - numpy
  - matplotlib
  - pandas
  - pip
  - pip:
    - some_pypi_only_pkg
```

Save it on the `root` folder of your repository. Otherwise, save it in a folder named `binder` which must be located in the `root` folder.

</exercise>

<exercise id="7" title="Setting Up an R Binder" type="slides">

<slides source="chapter4_04_R_repository">
</slides>

</exercise>

<exercise id="8" title="runtime.txt and install.R template" >

Use this template as your `runtime.txt` file

```
# Today's date
r-2021-12-07
```

Use this template as your `install.R` file

```
install.packages("tidyverse")
install.packages("rjson")
```

Save it on the `root` folder of your repository.

</exercise>

<exercise id="9" title="Summary and Conclusions" type="slides">

<slides source="chapter4_05_summary_and_conclusions">
</slides>

</exercise>