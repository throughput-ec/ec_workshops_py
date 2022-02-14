---
type: slides
---

<div><h1><img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module1/00_ec_slide1.png?raw=true" alt="EC Theme" width=25% align="left"/> Lesson 2<br>Setting a Binder Up</h1></div>

---
# Getting to the Hub

If you visit [mybinder.org](https://mybinder.org/) you will encounter the following screen:

<a href="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/00_binder.png?raw=true" target="_blank">
<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/00_binder.png?raw=true" alt="Binder" width=45% align="center" title = "Click to zoom in">
</a>

Before you can fill in the information, what do you need to create a Binder repository?

---

# What Do you Need to Build a Binder Repository?
**Git Repository**

- You will need to have a Git repository.

- The repository must be in a *public* location online. 

<a href="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/02_github.png?raw=true" target="_blank">
<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/02_github.png?raw=true" alt="Git requirements for Binder" width=35% align="center" title = "Click to zoom in">
</a>


---
# What Do you Need to Build a Binder Repository?
**Git Repository**

- You can work with other Git repository hosting manager tools such as:
    - `GitHub`, `GitLab`, `Bitbucket`, and MORE!

<a href="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/01_binder.png?raw=true" target="_blank">
<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/01_binder.png?raw=true" alt="Binder site" width=45% align="center" title = "Click to zoom in">
</a>

---

# What Do you Need to Build a Binder Repository?
**Configuration Files**

- The repository must have configuration files that specify its environment.

- These configuration files should be placed in the root of the repository or in a binder/ folder in the repository’s root.

<a href="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/03_github.png?raw=true" target="_blank">
<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/03_github.png?raw=true" alt="Configuration Files" width=45% align="center" title = "Click to zoom in">
</a>
---

# What Do you Need to Build a Binder Repository?
**A File to Share**

- The repository contains content designed for people to read.
    - A Jupyter Notebook 
    - An R script to make a visualization.

<a href="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/04_github.png?raw=true" target="_blank">
<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/04_github.png?raw=true" alt="Pointing to sharing the right file" width=45% align="center" title = "Click to zoom in">
</a>

---

# What Do you Need to Build a Binder Repository?
**Security**

- The repository **does not** require any sensitive information 
    - Passwords
    - API secrets
    - Personal information
    - Private data

---

# What Do you Need to Build a Binder Repository?
**A BinderHub**

- Binders are powered by a BinderHub, an open-source tool that deploys the Binder service to the cloud.

- There are several BinderHubs that you may use:
    - [Binder Pangeo](https://binder.pangeo.io/)
    - [mybinder.org](https://mybinder.org/)
    - [Alan Turing Institute Binder](https://turing.mybinder.org/)
    - and [others](https://mybinder.readthedocs.io/en/latest/about/federation.html)

---
# What Do you Need to Build a Binder Repository?
**A BinderHub**

<a href="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/00_binder.png?raw=true" target="_blank">
<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/00_binder.png?raw=true" alt="Binder Org" width=45% align="center" title = "Click to zoom in"> 
</a>

---

# Binder's Behind the Scenes
**repo2docker**

Binder uses a tool that mimics how humans do reproducible code **repo2docker**.

- It clones a github repository.

- It looks for configuration files 
    - These files describe the dependencies needed for the project.
    - It recognizes files named: `environment.yml`, `requirements.txt`, `install.R`, `Dockerfile`, and MORE.

- It installs the dependencies based on the configuration file.

- Starts a Jupyter Notebook / RStudio session.

---

# Let's practice what we learned!