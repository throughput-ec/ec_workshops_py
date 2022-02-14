---
type: slides
---

<div><h1><img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module1/00_ec_slide1.png?raw=true" alt="EC Theme" width=25% align="left"/> Lesson 3<br>The Docker Hub</h1></div>

---
## What is the Docker Hub?
- We used it last module.
- Docker Hub is the place where open Docker images are stored. 
- When we ran our first image by typing
```
docker run --rm -p 8787:8787 rocker/geospatial
```
Docker checked if this image is available on your computer.

- If not, the image is downloaded "automatically" from the Docker Hub. 

- If you just want to pull the image but not run it, you can also do
```
docker pull rocker/verse
```

---

## Pushing an image to Docker Hub
What happens if you want to design your own image so that others can use it?

With the Docker Hub, you can easily share your image in https://hub.docker.com/.  
After verifying your email you are ready to go and upload your first docker image.

Let's get started!

---

## Setting an account in Docker Hub

1. Create an account and log in on https://hub.docker.com/
2. Click on Create Repository.
3. Choose a name and a description for your repository and click on `Create`.
4. Now, log into the Docker Hub from the command line
```
docker login --username=yourhubusername --email=youremail@company.com
```
5. Enter your password when prompted. 
6. If everything worked you will get a message similar to
```
WARNING: login credentials saved in /home/username/.docker/config.json
Login Succeeded
```
---

## Getting an image reaady

1. Check the image ID using
```
docker images
```
and what you will see will be similar to

```
REPOSITORY                         TAG       IMAGE ID       CREATED         SIZE
course-starter-python_gatsby       latest    8ec687baf514   3 weeks ago     1.38GB
ec_workshops_gatsby                latest    8ec687baf514   3 weeks ago     1.38GB
rocker/rstudio                     latest    1878e29db52f   3 months ago    1.93GB
rocker/verse                       latest    0168d115f220   3 days ago      1.954 GB
ds-toolbox_gatsby                  latest    c7a440cb78ff   3 months ago    2.25GB
sedv8808/unacquired_sites_db_app   latest    a8a671927478   10 months ago   1.26GB
sedv8808/unacquired_sites_ml_app   latest    6dd7e4093508   10 months ago   1.39GB
```

---
## Tagging your Image

- Tag your image doing:
```
docker tag 0168d115f220 yourhubusername/changed_verse:firsttry
```

- The number must match the image ID and `:firsttry` is the tag. 
- A good tag will help you understand what this particular image is intended for.
- Examples of good tags:
    - A paper’s DOI or journal-issued serial number
    - A particular version of a code or data version control repo

---

## Push your image 

- To push your image, type:
```
docker push yourhubusername/verse_gapminder
```

Your image is now available for everyone to use.

---

## Saving your images locally

- To save a Docker image after you have pulled, committed or built it you use the docker save command. 
```
docker save verse_gapminder > verse_gapminder.tar
```

- To load that Docker container from the archived tar file in the future, we can use the docker load command:
```
docker load --input verse_gapminder.tar
```

---

# Let's Practice What We Learned