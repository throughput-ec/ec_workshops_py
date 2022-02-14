---
type: slides
---
  
<div><h1><img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module1/00_ec_slide1.png?raw=true" alt="EC Theme" width=25% align="left"/> Lesson 3<br>Setting Up the Python Binder</h1></div>

---

# Step 1

- Create a **public** GitHub repository.
- You can name your GitHub repository as you like.
- Initialize your repository with a README!
- Clone the repository to your local machine.

<a href="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/02_github.png?raw=true" target="_blank">
<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/02_github.png?raw=true" alt="Git requirements for Binder" width=45% align="center" title="Click to zoom in"> 
</a>

---

# Step 2

- Inside your Github repository folder:
    - Create a Jupyter notebook.
    - Open a new code cell and write:
    ```
    import folium
    import pandas

    m = folium.Map(location=[49.267665596, -123.241999032], zoom_start=12)
    tooltip = "Click Here For More Info"

    marker = folium.Marker(
        location=[49.267665596, -123.241999032],
        popup="<stong>UBC</stong>",
        tooltip=tooltip)
    marker.add_to(m)
    m
    ```
    - Save the Jupyter notebook. 

---

# Step 3 

— Create an `environment.yml` file into your Github repository.

For our previous example, our dependencies are `folium` and `pandas`.

Our `environment.yml` file should look like this:

```
name: my-example-environment
channels:   
  - conda-forge 
dependencies:
  - pandas
  - folium
```

You can find a template in the next "activity"

---

# Step 4 

- Push all your repository changes back to GitHub.
- Your repository should look now like this:

<a href="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/05_github.png?raw=true" target="_blank">
<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/05_github.png?raw=true" alt="First py binder repo" width=45% align="center" title="Click to zoom in"> 
</a>

---

# Step 5

- Go to my binder.
- Type the URL of your repo into the "GitHub repo or URL" box. It should look like this:
```
https://github.com/your-username/my-first-python-binder
```

- Where it says Git ref type in `main` or the branch that you woud like to use.
- Where it says "URL to open (optional)" type in the notebook file name and choose "file". 

- As you type, the webpage generates a link in the "Copy the URL below..." box. It looks like this:
```
https://mybinder.org/v2/gh/your-username/my-first-python-binder/HEAD
```

---

<a href="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/06_binder.png?raw=true" target="_blank">
<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/06_binder.png?raw=true" alt="Zero to Binder" width=65% align="center" title="Click to zoom in"> 
</a>


---

# Step 5b

- Once this is done simply hit the launch button. 
- My Binder will create your binder repo in a few minutes.
- Be patient. The first time it might take some while to build.

<a href="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/07_binder.png?raw=true" target="_blank">
<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/07_binder.png?raw=true" alt="Binder Process" width=40% align="center" title="Click to zoom in"> 
</a>

---

# Step 6

- Copy the generated link, open a new browser tab and visit that URL.

- You will see a "spinner" as Binder launches the repository.

<a href="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/08_binder.png?raw=true" target="_blank">
<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/08_binder.png?raw=true" alt="Spinner" width=45% align="center" title="Click to zoom in"> 
</a>


---

# Step 7

- Go to the link provided by Binder. 
- You should now be able to work and navigate the last version of your pushed Jupyter notebook.

<a href="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/09_binder.png?raw=true" target="_blank">
<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/09_binder.png?raw=true" alt="Binder from Git" width=45% align="center" title="Click to zoom in"> 
</a>

---

# Step 8

- Once built, you can share the link to this with anybody you want to run your project on their machine.

- Save your LaunchBinder Badge and share it! [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sedv8808/my-first-python-binder/main?labpath=my-folium-map-notebook.ipynb)


<a href="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/10_binder.png?raw=true" target="_blank">
<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/10_binder.png?raw=true" alt="Binder Badge" width=45% align="center" title="Click to zoom in"> 
</a>

---

# Let's practice!