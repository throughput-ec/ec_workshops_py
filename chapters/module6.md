---
title: 'Module 6: Introduction to Docker'
description:
  'This module will teach you about Docker and containerization. You will be able to launch third party containers and write your own Dockerfile.
  '
prev: /module5
next: /module7
type: chapter
id: 6
---

<exercise id="0" title="Learning Outcomes" type="slides">

<slides source="chapter6_00_learning_outcomes">
</slides>

</exercise>

<exercise id="1" title="Introduction to Docker" type="slides">

<slides source="chapter6_01_introduction_to_docker">
</slides>

</exercise>

<exercise id="2" title="Trivia Time!">

A Docker container allows us to:

<choice id="1">
<opt text="Run the exact same code and get the same results making our analysis reproducible."  correct="true">

Good job!

</opt>

<opt text="Run the exact same code and same data with the possibility of getting different results, which would allow us to catch bugs.">

This is what you are trying to avoid.

</opt>

<opt text="Ship a whole Virtual Machine">

We create Docker containers, which are more lightweight than VMs.

</opt>
</choice>

What is a Docker Image?

<choice id="2">
<opt text= "What we ultimately build: the application that is completely interactable by users and administrators." >
 
This is a Docker Container.

</opt>

<opt text="A whole CPU, storage, memory, and access to the internet." >

This is a Virtual Machine.

</opt>

<opt text = "Source code for binaries, libraries, tools, dependencies that are required to function as an application." correct="true">

Good job!

</opt>

</choice>

</exercise>

<exercise id="3" title="Lauching a Docker Container" type="slides">

<slides source="chapter6_02_launching_a_docker">
</slides>

</exercise>

<exercise id="4" title="Trivia Time!">

Why do we use the --rm tag?

<choice id="1">
<opt text="If we do not use it, the Docker container cannot be loaded.">

Try again!

</opt>

<opt text="Docker containers can be very heavy. This allows us to remove a container once we have finished using it." correct="true">

Good job!

</opt>

<opt text="It allows us to use volumes so that we can retrieve our data analysis in our local machine.">

Nice try! But there is a different tag for this.

</opt>
</choice>

How can you change a password in a rocker image?

<choice id="2">
<opt text= "Using the -e flag plus the word PASSWORD" correct="true" >
 
That's right. Although there is no particular flag for passwords, you can use additional arguments with the flag `-e`.


</opt>

<opt text="Using the flag -v" >

This flag is for setting volumes, another very important task in the Docker ecosystem.

</opt>

<opt text = "Using the flag -p">

This flag is for setting the port.

</opt>
</choice>

What happens if we do not use the `-v` flag?

<choice id="3">

<opt text="If not set up, your Docker tasks will not be linked to your local machine. This will cause that anything that you do in Docker will be lost as soon as you close the container. The flag -v stands for volume and links to a local directory in your machine." correct="true">

Good job!

</opt>

<opt text="If not set up, your Docker tasks will still be linked to your local machine. However anything that you do in Docker will be saved in a default place in your local machine.">

Nice try! But unfortunately, it won't be saved - not even in a default location.

</opt>
</choice>


</exercise>

<exercise id="5" title="The Docker Hub" type="slides">

<slides source="chapter6_03_pushing_pulling_dockerhub">

</slides>

</exercise>

<exercise id="6" title="Dockerfiles" type="slides">

<slides source="chapter6_04_Dockerfiles">

</slides>

</exercise>

<exercise id="7" title="Template of a Dockerfile">

Use this template as your `Dockerfile` file.  
You can place it in the `root` directory of your project or Git repository.

This will help you create the environment needed to run your program. 

Remember, this is just a template of some steps that you may want in your Dockerfile.  
You do not need to have all of them - it depends on what your usecase is.

```
# image where you are basing yourself from
FROM rocker/verse:latest  

# libraries that you want to have in your image
RUN R -e "install.packages('htmlwidgets')"   
RUN R -e "install.packages('leaflet')"

# creating the directory where your app will live
RUN mkdir /home/my_docker  

# setting the working directory 
WORKDIR /home/my_docker    

# copying scripts that you might want in your image
COPY my_analysis.R /home/my_docker/my_analysis.R     

# running the scripts
CMD R -e "source('/home/my_docker/my_analysis.R')"  
```
</exercise>

<exercise id="8" title="Summary and Conclusions" type="slides">

<slides source="chapter6_05_summary_and_conclusions">
</slides>

</exercise>