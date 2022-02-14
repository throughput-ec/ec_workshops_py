---
type: slides
---

<div><h1><img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module1/00_ec_slide1.png?raw=true" alt="EC Theme" width=25% align="left"/> Lesson 1<br>Introduction to Binder</h1></div>

<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Page Title</title>
<style>
    /* The . with the boxed represents that it is a class */
    .boxed {
    background: white;
    color: black;
    border: 3px solid black;
    margin: 0px auto;
    width: 700px;
    padding: 10px;
    border-radius: 10px;
    }
</style>
</head>

---

# What is Binder?
**Motivation: Going Beyond Paper**

- Binder is a Jupyter tool for sharing interactive notebooks with others.

- When publishing an article in paper, text and images might not suffice for the reader to understand all the expressed concepts.

- Luckily, a lot of researchers publish their workflow on GitHub as well. 

- If we ran their code, we would probably understand their ideas better.

- However, we might encounter difficulties while trying to read/reproduce other's people code...

---

# What is Binder?
**Motivation: Reading Other People's Code**

<img src="https://www.explainxkcd.com/wiki/images/8/89/code_quality_3.png" alt="Other people code map" width=65% align="center">

[Source: XKCD cartoon](http://xkcd.com/1833/)

---

# What is Binder?
**Motivation: Sharing Code**

Sharing and reproducing other people's code may come with some challenges.

Because of this, there are different tools to share code that is reproducible:

- Creating Virtual Environments
- Creating a Docker Image
- Writing a very precise manual on how to create the right environment to run your code

Each of these methodologies come with each own set of challenges and it might be complicated or require some expertise.
Furthermore, they will still require some efforts from your user.

---

# What is Binder?
**Motivation: Sharing Code**

With Binder, we can:

- Get/Provide one link with a prebuilt environment where we can run the Jupyter notebook or Rmd smoothly.

- Spend the time understanding the code rather than setting up the environment to execute the code.

---

# What is Binder?
**Sharing a Single Link**

That way, our emails can transition from this: 

<body>
<div class="boxed">

Hi Jane,  
I am so happy that you like our project and that you want to run our code to understand our  figures better! 
To run our code without installing dependencies, you will need to:  
- Install Docker and repo2docker   
- Download the image from the DockerHub - you can find the link in the repo.
- Run from your terminal  
```
repo2docker https://github.com/throughput-ec/ec-workshops
```
That will generate a long output and at the end there will be a URL. Copy that ULR and paste it into your browser.  Send me an email if you have any issues with the installations.
Best,  
S

</div>
</body>

---

# What is Binder?
**Sharing a Single Link**

to this:

<div class="boxed">

Dear Jane,  
I am so happy that you like our project and that you want to run our code to understand our  figures better! 
Please click on this link to start executing our code.  
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/throughput-ec/ec-workshops/binder)   
Best,  
S

</div>

---

# Uses of Binder
**Motivation: Your Next Project**

If your intent is to share a Notebook or an Rmd file, consider using Binder.

Other popular uses for Binder include:

- Sharing computational work or papers
- Sharing educational material
- Generating interactive open-source package documentation
- Creating live demonstrations

---

# Let's review what we learned!