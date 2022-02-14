---
type: slides
---

<div><h1><img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module1/00_ec_slide1.png?raw=true" alt="EC Theme" width=25% align="left"/> Lesson 2<br>Launching Docker</h1></div>

---

## Installation

- Follow the installation instructions. [Get Docker](https://docs.docker.com/get-docker/). 

- You will be directed to several tutorials. Feel free to take a look at them.

---

## Launching Our First Docker Image

1. Launch Docker is to open a Unix Shell:
  - On Mac or Windows, use the `Docker Quickstart Terminal` that you installed.
  - On a Linux machine, use a terminal prompt.

2. We are going to use a pre-existing image: [rocker/geospatial](https://hub.docker.com/r/rocker/geospatial). 

3. In the `Docker Quickstart Terminal` type:

```
docker run --rm -p 8787:8787 rocker/geospatial
```

---

## Launching Our First Docker Image

`*p` and `--rm` are flags that customize how the container is run. 

`-p` : This is the port that you need to specify where you will be working.  
Since we specified that we wanted to use port 8787 in our command line, we need to go to:
http://localhost:8787/

`-–rm`: delete the container when it is quitted. Otherwise, a version of it will be saved to our local computer.  
Containers can occupy a lot of disk space.

---
## Launching Our First Docker Image

- You should see:
````markdown
                        ##         .
                  ## ## ##        ==
               ## ## ## ## ##    ===
           /"""""""""""""""""\___/ ===
      ~~~ {~~ ~~~~ ~~~ ~~~~ ~~~ ~ /  ===- ~~~
           \______ o           __/
             \    \         __/
              \____\_______/
docker is configured to use the default machine with IP 192.168.99.100
For help getting started, check out the docs at https://docs.docker.com
Thus, you would enter http://192.168.99.100:8787 in your browser as the url.
````
---

## The Hub

Where did `rocker/geospatial` came from? 
- If you try to run a Docker container which you have not installed locally, Docker will automatically search for the container on Docker Hub (an online repository for docker images).
- If it exists, it will download it.
- In our case, this is the <a href="https://hub.docker.com/r/rocker/geospatial" target="_blank"> Docker repository </a>
- You can notice that it contains some instructions and all the dependencies that are included in this image.

---

- The command above will lead RStudio-Server to launch invisibly. 
- To connect to it, open a browser and enter `http://localhost:8787/`
- You should see RStudio welcome screen. Log in using:

```
username: rstudio 
password: # given in terminal
```

---

- You are able to work with RStudio in your browser in much the same way as you would on your desktop.

- Look at your terminal, the password is there. You can change the password with the flag `-e PASSWORD`

- Exercise: Change the login password.

```
docker run --rm -e PASSWORD=<YOUR_PASS> -p 8787:8787 rocker/geospatial
```
---

## Linking Volumes

1. Given that we used the `--rm` flag when we launched the Docker container, anything we create on the machine will be gone. Let’s verify this.

2. Open a new R script.

3. Enter the following code in the script, run it and save it:

```
# make x the numbers from 1 to 5, and y the numbers from 6-10
x <- 1:5
y <- 6:10

# plot x against y
plot(x, y)
```
---

## Linking Volumes

4. In your files panel, you will see the new script file.

5. Close the browser tab where you have RStudio open, and then go to your terminal window from where you launched the Docker container and type Contol+C. This shuts down the Docker container.

6. Relaunch a Docker container using the RStudio image as you did previously:
```
docker run --rm -p 8787:8787 rocker/geospatial
```

7. Go to `http://localhost:8787/` in your browser.

8. The R script you created ... is... gone.

---

## Linking Volumes

- Linking a volume allows to access data and save files in our local machine.

- When launching a container, add the `-v` flag along with the path to your project’s root directory and the path to the container: 
```
docker run --rm -p 8787:8787 -v /Users/your_user/Documents/r_docker_tutorial:/home/rstudio/r_docker_tutorial rocker/geospatial
```

- Go then to `http://localhost:8787/` in your browser.

- Set the working directory to the directory called `r_docker_tutorial`

- You can load data from your computer into the launched RStudio tab.

- You can save your analysis into the `r_docker_tutorial` directory.

- If you created a document, when you close the RStudio browser and exit your Docker container look inside the `r_docker_tutorial` directory to find them.

---

# Let's Practice!