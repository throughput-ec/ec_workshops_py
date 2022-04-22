---
type: slides
---

<div><h1><img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module1/00_ec_slide1.png?raw=true" alt="EC Theme" width=25% align="left"/> Lesson 1<br>Introduction to Docker</h1></div>

---

## What is Docker?
**Motivation**

<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--lIJpZE9A--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://user-images.githubusercontent.com/34328907/78120341-7b56f900-7429-11ea-9b3f-1a5e17b813da.png" alt="Motivation Docker" width=45% align="center">

[Source](https://res.cloudinary.com/practicaldev/image/fetch/s--lIJpZE9A--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://user-images.githubusercontent.com/34328907/78120341-7b56f900-7429-11ea-9b3f-1a5e17b813da.png)

---

## What is Docker?
**Motivation**

Imagine the following scenario:
- You are working on an analysis in R / python and you send your code to a colleague.

- Your colleague runs exactly this code on exactly the same data but they get a different result or even worse, an error. 

- Some reasons for this to happen: A different operating system, a different version of R or of an R package. 

- Docker is trying to solve problems like that. 

- Docker is an open-source containerization platorm.

---

## What is Docker?

- A Docker container can be seen as a computer inside your computer. 

- You can send this "inside computer" to your colleagues.

- Your colleagues will use this "virtual computer" and run your code. They will get exactly the same results.

- Docker allows you to wrangle dependencies (from the operating system up to details such as R, python and Latex package versions).

- It makes sure that your analyses are reproducible.

- It makes your analysis **portable**  and **sharable**.

---
## Important Vocabulary

Through our journey with Docker, the following terms might come often:

- Virtual Machine
- Container
- Docker Image
- Docker Container

---

### Virtual Machine
- Not different from your tangible computer/phone/server.

- A VM has its own CPU, storage, memory, and access to the internet.

- software-based versions of a computer sorted in a file tipically called an **image**

- A *VM image* is a set of instructions on how exactly to assemble the code and achieve a desired software configuration.

---

### Container
- Software executable bundles where the bins, libraries, and dependencies are packaged alongside their code under a standardized framework.

- Lightweight images of application can then be run anywhere: desktop, cloud, etc...

- This avoids the "It works on my machine" problem.

- "docker" and "containers" are terms that currently, people use interchaingeable.

---

### Docker Image

- Source code for binaries, libraries, tools, dependencies that are required to function as an application.

- When Docker runs an image, it becomes a container.

- One image can be the base for multiple containers that share commonalities.

- You can add several "layers" of images on top of the container layer. 

---

### Docker Container

- What we ultimately build: the application that is completely interactable by users and administrators.

- Remember Docker Images are a set of instructions to build a container.

- This is the "background service" that runs the Docker operations.

- Keeps track of Docker operations and assigns them with proper tags.

---

# Let's Practice!
