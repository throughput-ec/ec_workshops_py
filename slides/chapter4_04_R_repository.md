---
type: slides
---

<div><h1><img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module1/00_ec_slide1.png?raw=true" alt="EC Theme" width=25% align="left"/> Lesson 4<br>Setting Up the R Binder</h1></div>

---

# Step 1

- Create a **public** GitHub repository.
- You can name your GitHub repository as you like.
- Initialize your repository with a README!
- Clone the repository to your local machine.

<a href="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/11_github.png?raw=true" target="_blank">
<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/11_github.png?raw=true" alt="Binder Process" width=45% align="center" title="Click to zoom in"> 
</a>

---

# Step 2

- Inside your Github repository folder:
    - Create an Rmd file.
    - Copy and paste the following slide. (We'll learn more about Rmd files in the next module.)
    - Save the Rmd file. 

---

'''

    ```{r setup, include=FALSE}  
    knitr::opts_chunk$set(echo = TRUE)  
    library(leaflet)  
    leaflet(options = leafletOptions(minZoom = 0, maxZoom = 18))  
    ```

    ## My Leaflet Map

    **TASK:** Find UBC in a Leaflet map.
 

    ```{r}
    map1 <- leaflet() %>%  
                addProviderTiles(providers$Stamen.TerrainBackground) %>%  
                addTiles() %>%  
                addCircleMarkers(lng =-123.241999032 , lat = 49.267665596,  
                popup = paste0("UBC"))  
    map1  
    ```
'''

---

# Step 3 

You will need two files in your repository:
1. `runtime.txt` Specify the R version by date. The easiest day, write today's date (e.g. r-2021-12-07). 

    ```
    r-2021-12-07
    ```

2. `install.R` A list of `install.packages('package_name')` commands, one per line.
    For our example
    ```
    install.packages(c("leaflet", "tidyverse"
                       "knitr", "rmarkdown",
                       "caTools", "bitops"))
    ```
    
You can find a template for both files in the next section.

---

# Step 4 

- Push all your repository changes back to GitHub.
- Your repository should look now like this:

<a href="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/12_github.png?raw=true" target="_blank">
<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/12_github.png?raw=true" alt="R repo" width=45% align="center" title="Click to zoom in"> 
</a>

---

# Step 5

- Go to my binder.
- Type the URL of your repo into the "GitHub repo or URL" box. It should look like this:
```
https://github.com/your-username/my-first-R-binder
```

- Where it says Git ref type in `main` or the branch that you woud like to use.
- Where it says "URL to open (optional)", choose URL and type `rstudio`
- As you type, the webpage generates a link in the "Copy the URL below..." box. It should look like this:
```
https://mybinder.org/v2/gh/your-username/my-first-R-binder/main?urlpath=rstudio
```

---

<a href="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/13_binder.png?raw=true" target="_blank">
<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/13_binder.png?raw=true" alt="Binder Page" width=65% align="center" title="Click to zoom in"> 
</a>

---

# Step 5b

- Once this is done simply hit the launch button. 
- My Binder will create your binder repo in a few minutes.
- Be patient. The first time it might take some while to build.

<a href="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/14_binder.png?raw=true" target="_blank">
<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/14_binder.png?raw=true" alt="Binder loading" width=45% align="center" title="Click to zoom in"> 
</a>

---

# Step 6

- Copy the generated link, open a new browser tab and visit that URL.

- You will see a "spinner" as Binder launches the repository.

<a href="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/08_binder.png?raw=true" target="_blank">
<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/08_binder.png?raw=true" alt="Binder Spinner" width=45% align="center" title="Click to zoom in"> 
</a>


---

# Step 7

- RStudio will open in your browser.
- You will have to open your `.Rmd` file manually by clicking on it.
    - You can find it on the bottom right panel.

<a href="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/15_binder.png?raw=true" target="_blank">
<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/15_binder.png?raw=true" alt="Binder from Git" width=45% align="center" title="Click to zoom in"> 
</a>

---

# Step 8

- Once built, you can share the link to this RStudio instance with anybody you want to run your project on their machine.

- Save your LaunchBinder Badge and share it!

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sedv8808/my-first-R-binder/main?urlpath=Rstudio)

<a href="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/16_binder.png?raw=true" target="_blank">
<img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module4/16_binder.png?raw=true" alt="Binder from Git" width=45% align="center" title="Click to zoom in"> 
</a>

---

# Let's practice!