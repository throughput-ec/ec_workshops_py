---
type: slides
---

<div><h1><img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module1/00_ec_slide1.png?raw=true" alt="EC Theme" width=25% align="left"/> Lesson 4<br>Dockerfiles</h1></div>

---

## What is a Dockerfile?

- Dockerfiles are a set of instructions on how to add things to a base image. 

- They build custom images up in a series of layers. 

- It is a configuration file that describes several things: 
    - from what previous Docker image you are building this one
    - how to configure the OS
    - what happens when you run the container

---
## Writing a Dockerfile

Let’s build a very basic Dockerfile for R. 

The task to solve is:  
```
I have today an analysis that works in a .R file. 
I want to make sure that this analysis will always work in the future, 
regardless of any update to the packages used.
```

Create a project folder. Then, inside this folder, in the `root`, create a new text file.

Save this now empty text file as `Dockerfile`

---

Let's use a modified R script from module 4.
This is the main analysis that we will want to reproduce.

Save it as `my_analysis.R`

```
library(leaflet)  
library(htmlwidgets)

leaflet(options = leafletOptions(minZoom = 0, maxZoom = 18))  

## My Leaflet Map

map1 <- leaflet() %>%  
  addProviderTiles(providers$Stamen.TerrainBackground) %>%  
  addTiles() %>%  
  addCircleMarkers(lng =-123.241999032 , lat = 49.267665596,  
                   popup = paste0("UBC"))  

map1  

## 'leaflet' objects (image above)
saveWidget(map1, file="m.html")
```

---

1. In your new Dockerfile, write the following:

```
FROM rocker/verse:latest
```

Every Dockerfile starts with a `FROM`.  
This tells Docker to start with the rocker/verse base image.   
There are a lot of other official images, and you can also build from a local one.

This FROM is, in a way, describing the dependency of your image.

**REMEMBER**
The `FROM` command must always be the first thing in your Dockerfile.

---

2. Add a layer on top of our verse. Install `leaflet` and `htmlwidgets`.
```
RUN R -e "install.packages('leaflet')"
RUN R -e "install.packages('htmlwidgets')" 
```

`RUN` commands in your Dockerfile execute shell commands to build up your image. 

You can see that, since we are working with `R`, we use the same commands that we would use in R console.

---

## Building a Dockerfile

4. Return to the Docker terminal.

5. Build the image by doing:
```
docker build -t my-r-image .
```

`-t my-r-image` names the image (use only lower case)  
`.` says all the resources we need to build the image are in our current directory. 

This step will probably take a few minutes. Depending on the complexity of your image, how long it will delay. You will see lines being printed on the Docker terminal.

Wait until it is done.

---

6. List your images via:
```
docker images
```
7. You should see `my-r-image` in the list. 

<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module6/00_docker_images.png?raw=true" alt="Docker Images" width=45% align="left"/>

---

## Launch your new image 

- Simply do the commands that you already know:
```
docker run --rm -p 8787:8787 my-r-image
```

Then in the RStudio terminal in the browser, try the library `leaflet` again:

```
library('leaflet')

```

You will see the library is loaded. This means `leaflet` is pre-installed and ready to go in your new docker image.

---

You can also tart the container with a mounted volume to save the output.

```
docker run --rm -p 8787:8787 -v /Users/your_path/r_docker_tutorial:/home my-r-image
```

---

## Adding Data

- You may also want some some static files inside our Docker image - such as data.

- Add a line in the Dockerfile:
```
ADD data/gapminder-FiveYearData.csv /home/rstudio/
```
Rebuild your Docker image:
```
docker build -t my-r-image .
```
And launch it again:
```
docker run --rm -p 8787:8787 my-r-image
```
Go back to RStudio in the browser, and `gapminder-FiveYearData.csv` will be, present in the files visible to RStudio. 

---
## Data Security

- For you to load the data, you must have the CSV file in your project's root directory (or in a directory called data/ inside your root directory) in order to push it to the image. 

- Be careful when uploading sensitive data.

---

## Advanced Dockerfiles

Sometimes, we only want to send a Docker image that reproduces all the analysis and just outputs the results' files.

We can add a few more lines to our Dockerfile to achieve this goal.

---

## RUN mkdir and WORKDIR

The `mkdir` command is used to make a new directory. 
You can use it to create the `app` or a main directory in your Dockerfile.

Most importantly is the `WORKDIR` command, which will allow you to set what your working directory within Docker.

Add the following two lines to your Dockerfile

```
RUN mkdir /home/my_docker
WORKDIR /home/my_docker
```

---

## Copy

Let's get our analysis script from our host machine to the container. 

For that, we’ll need to use `COPY` localfile pathinthecontainer.   
Note that here, the my_analysis.R has to be in the same folder as the Dockerfile on your computer.

Add this line to your Dockerfile

```
COPY my_analysis.R /home/my_docker/my_analysis.R
```

---

## CMD

Finally `CMD`

This command will be run every time you’ll launch the docker. 

We want `my_analysis.R` to be sourced. Add this line to your Dockerfile
```
CMD R -e "source('/home/my_analysis.R')"
```

Save the Dockerfile, rebuild, and reload.

---

## Final Complete Dockerfile

```
FROM rocker/verse:latest  # image where you are basing yourself from

RUN R -e "install.packages('htmlwidgets')"   # libraries that you want to have in your image
RUN R -e "install.packages('leaflet')"

RUN mkdir /home/my_docker  # creating the directory where your app will live
WORKDIR /home/my_docker    # setting the working directory 

COPY my_analysis.R /home/my_docker/my_analysis.R     # copying scripts that you might want in your image

CMD R -e "source('/home/my_docker/my_analysis.R')"   # running the scripts
```

---

# Let's practice what we learned!
