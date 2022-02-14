---
title: 'Module 5: Working with RMarkdown'
description:
  'In this module you will create, edit and run reproducible R code documents using RMarkdown.
  '
prev: /module4
next: /module6
type: chapter
id: 5
---

<exercise id="0" title="Learning Outcomes" type="slides">

<slides source="chapter5_00_learning_outcomes">
</slides>

</exercise>

<exercise id="1" title="Introduction to RStudio" type="slides">

<slides source="chapter5_01_introduction_to_Rstudio">
</slides>

</exercise>

<exercise id="2" title="Creating an Rmd file" type="slides">

<slides source="chapter5_02_creating_an_Rmd_file">
</slides>

</exercise>

<exercise id="3" title="Creating a Presentation" type="slides">

<slides source="chapter5_03_creating_a_presentation">

</slides>

</exercise>

<exercise id="4" title="My First Presentation Task">

1. Go to [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/throughput-ec/ec-binder/main?urlpath=rstudio)

2. Open a new Rmd file.

3. Copy and paste the following text

````markdown
---
title: "My First Deck of Slides"
author: "My Name"
date: "12/12/2021"
output: ioslides_presentation
---

# Title Slide

---
## Slide with Bullets

- Bullet 1
- Bullet 2
- Bullet 3

---
No Header Slide

---
## Slide with R Output

This is some code

```{r code demo, echo = TRUE}
x <- 5
y <- 10
(x <- x + y)
``` 
````



4. Click on the Preview / Knit button.

**Remember:** Do not leave a white space between the `---` and the next line


</exercise>

<exercise id="5" title="Creating an R Project" type="slides">

<slides source="chapter5_04_R_project">
</slides>

</exercise>

<exercise id="6" title="First Steps in R">

For a simple introduction, we are going to use the Gapminder dataset.

We will apply our knowledge of tidyverse functions. 

## About the Dataset

[Gapminder Foundation](https://www.gapminder.org/) is a non-profit organization in Stockholm, Sweden, that promotes sustainable global development and achievement of the United Nations Millennium Development Goals by increased use and understanding of statistics and other information about social, economic and environmental development at local, national and global levels.

## Let's learn some functions in R!

**glimpse()**  
The `gapminder` dataframe has been previously loaded for you. You just need to call it.
Let’s take a quick look at it to learn about its structure. 

We can do this using the `glimpse()` command, which will display the structure and the first few rows of our data frame.

<codeblock id="05_01">


</codeblock>


**select**  
The first function we’ll be using is `select()`. 
This function let’s us pick columns from our dataframe, based on name (e.g. year) or index (e.g. 3).

<codeblock id="05_02">

</codeblock>

Observe that the new dataframe contains only a subset of the columns from the original dataframe. 


**head()**  
As we saw from our `glimpse()` observations, the `gapminder` dataframe has 1,704 rows...

What if we would like to see some of the first few rows, just to have an idea of what the dataframe looks like? We can do that with `head()`.

<codeblock id="05_03">

</codeblock>

**Pipe: %>%**  

The pipe symbol `%>%` “pipes” an object INTO a function. We could `pipe` for example, the gapminder data into the `select()` function

We could rewrite code the following way:

<codeblock id="05_04">

</codeblock>


## Challenge 1

Reorder the code below to create a code that uses `select()` and `%>%`  to choose the columns continent, GDP per capita, life expectancy, and year from the gapminder data. 

Save it to a new variable named `result`.
Display the results using `glimpse()`.

<codeblock id="05_05">

</codeblock>


**filter()**  
Now that we can select columns, how do we choose rows? `filter()` allows us to choose rows from our dataframe using logical criteria. 

For example, using the `gapminder` dataframe, we could filter rows in which country is "USA". 

This can also be applied to numerical values, such as the year being equal to 1977, or life expectancy greater than 80.

**REMEMBER** In R, an equality is done using a double equals sign `==`.

<codeblock id="05_06">

</codeblock>

We can also filter several arguments at a time.

Let's try it!

<codeblock id="05_07">

</codeblock>


## Challenge 2

Use `filter()` to choose data for all Asian countries, from the year 1975 onwards.

Assign them to a variable called `gapminder_asia`


<codeblock id="05_08">

`>=` is used for the greater than or equal to symbol.

</codeblock>


**mutate()**  
Now that we can filter rows and columns, let's say we would like to start making some summaries of our data.
Let’s say we now want to calculate the total GDP, which is done by mutiplying the GDP per capita by the population. 
`mutate()` will perform this calculation on each row in the data frame, one row at a time (row-wise).

<codeblock id="05_09">

</codeblock>

**Combining Functions**  
Pipes `%>%` can be used to send an object such as a data frame into a function, such as select(), or filter(). 

However, their real power is that they can also be used to send the output of one function into another function. This allows us to chain together multiple commmands, without the need for intermediate variables.

<codeblock id="05_10">

</codeblock>

**Calculations with `group_by()` and `summarise()`**  
These functions allow us to work on our data in specific groups. 
For example, we can use `group_by()` to group observations by country, then calculate the `maximum`, `minimum`, and `average` life expectancy for each country.

<codeblock id="05_11">

</codeblock>

## Challenge 3

Calculate the mean `mean()` and standard deviation `sd()` of the total GDP for all counties in the Americas from 2000 and onwards.

<codeblock id="05_12">

Remember to use the `%>%` operator.
`filter()` can help you select which rows interest you
`mutate()` can help you create new columns with mathematican operations that you need
`group_by()` helps you specify groups within your data and along with `summarise()` you 
can calculate several statistics.
</codeblock>

## Well done!

You finished learning how to use the most popular functions in the `tidyverse` package.

We are still going to use some of these functions to organize our datasets. Let's move to plotting the data.


To practice more even more:

Go to <a href="https://mybinder.org/v2/gh/sedv8808/R_Wrangling/main?urlpath=rstudio" target="_blank"> Binder </a> and complete the exercises.

</exercise>

<exercise id="7" title="Plotting Data">

In the previous section, we did some exercises using the `Gapminder` Dataset.

As you could see, although tables are useful, they can be hard to understand. Here is where plotting can come in handy.

Plotting our data is one of the best ways to quickly explore it and the various relationships between variables.

There are three main plotting systems in R:
- The base plotting system
- The `lattice` package
- The `ggplot2` package

We’ll be learning about the `ggplot2` package, because it is the most effective for creating publication quality graphics. 
`ggplot2` is built on the grammar of graphics. A plot can be expressed from the same set of components: 
- A dataset
- A coordinate system
- A set of geoms (the visual representation of data points)

The key to understanding `ggplot2` is thinking about a figure in layers. 
This idea may be familiar to you if you have used image editing programs like Photoshop, Illustrator, or Inkscape.

## Simple ggplot

Run the following code, we are going to use the `Gapminder` dataset to visualize the relationship between `gdpPercap` and `lifeExp`
<codeblock id="05_13">

</codeblock>

Notice that the first command we call is `ggplot()`. `ggplot()` allows R know that we want to create a new plot. The `arguments` that we give the `ggplot()` function are the global options for the plot: they apply to all layers on the plot.

We passed in two arguments to `ggplot()`
- `gapminder` or the data that we want to show on our figure
- `aes()` that tells which columns from the data we want to use. On the `x-axis` we are passing the `gdpPercap` column and on the y-axis the `lifeExp` column.

By itself, `ggplot()` only has the perameters of what to draw, but does not know how to draw the data.

For that, we need to indicate the data representation using the `geom_()` layers. In our example, we used `geom_point()` to visually represent the relationship between x and y as a scatterplot of points

<codeblock id="05_13">

</codeblock>

**Layers**  
Using a scatterplot `geom_point()` probably isn’t the best for visualizing change over time. We can choose `geom_line()` to visualize the data as a line plot. 
Here we’ll also shorten our code by omitting some of the declarations (e.g. x = year). By default, the first object passed to ggplot() is assumed to be the data argument. Similarly, the first two column names of aes() are assumed to be the x and y arguments.

## Challenge 1
Another aesthetic property we can change in `aes()` is the `colour`.

Using your previous chapter, group the data by continent and year. 

Then, plot using `ggplot()` and a `geom_line()` - `year` should be on your x-axis and `mean(lifeexp)` on your y-axis. Colour by `continent` column.

What trends do you see in the data? Are they what you expected?

<codeblock id="05_14">

</codeblock>

**Transformations and Statistics**  
`ggplot2` makes it easy to overlay statistical models over the data. 
For example:

<codeblock id="05_15">

</codeblock>

Currently it is hard to see the relationship between the points due to some strong outliers in GDP per capita. 
We can change the scale of units on the x-axis using the `scale()` functions. These control the mapping between the data values and visual values of an aesthetic. 
We can also modify the transparency of the points, using the `alpha` function, which is especially helpful when you have a large amount of data which is very clustered.

<codeblock id="05_16">

</codeblock>

The `log10` function applied a transformation to the values of the gdpPercap column before rendering them on the plot, so that each multiple of 10 now only corresponds to an increase in 1 on the transformed scale, e.g. a GDP per capita of 1,000 is now 3 on the y axis, a value of 10,000 corresponds to 4 on the y axis and so on. This makes it easier to visualize the spread of data on the x-axis.

**Fitting a relationship**  
We can fit a simple relationship to the data by adding another layer, `geom_smooth()`:

<codeblock id="05_17">

</codeblock>

**Multi-panel figures**  
Earlier we visualized the change in life expectancy over time across all countries in one plot. Alternatively, we can split this out over multiple panels by adding a layer of facet panels. Here we will first make a smaller version of the data to make it easier to work with. The %in% operator just means that country must be equal to one of the four specified countries.

<codeblock id="05_18">

</codeblock>

</exercise>

<exercise id="8" title="Plotting Geographical Data">

**Plotting the world with `geom_map()`**  
Let's create the visualization of the continents. 

We will use the `geom_map` geom. `geom_map` takes a map argument, which is a dataframe that specifies the `longitude` and `latitude` of different regions of the world.

In order to do that, we take the `map_data` function, which allows use to create a dataframe with the longitude and latitude of every country of the world. 

The major problem we need to solve is how to add the name of the `continent` to the dataframe. There is no continent variable in the dataframe provided by `map_data("world")`. 

However, the package `countrycode` has a function `countrycode()`, which enables us to extract the continent from each country name.

<codeblock id="05_22">

</codeblock>

Let's plot the world

<codeblock id="05_23">

</codeblock>


</exercise>

<exercise id="9" title="Intro to Leaflet">

`Leaflet` is one of the most popular open-source JavaScript libraries for interactive maps. It’s used by websites ranging from The New York Times and The Washington Post to GitHub and Flickr, as well as GIS specialists like OpenStreetMap, Mapbox, and CartoDB.

This R package makes it easy to integrate and control Leaflet maps in R.

## Basic Usage
You create a `Leaflet` map with these basic steps:

1. Create a map widget by calling `leaflet()`.
2. Add `layers` (i.e., features) to the map by using layer functions (e.g. `addTiles`, `addMarkers`, `addPolygons`) to modify the map widget.
3. Repeat step 2 as desired.
4. Print the map widget to display it.

Here’s a basic example:

*Find a point with coordinates (long = -123.241999032 , lat = 49.267665596) on a Leaflet map.*

<codeblock id="05_25">

</codeblock>

Of course, we may want to plot more than a single point. With `leaflet`, we can pass a dataframe that has `latitude` and `longitude` columns to plot all desired points.

For example, we are going to use the  `quakes` data in `R`.

Let's plot only the first 20 rows.

<codeblock id="05_24">

</codeblock>

You might want to learn more about `leaflet`

Take the time to check out their [documentation](https://rstudio.github.io/leaflet/)
This is a recommended [tutorial](https://poldham.github.io/abs/mapgbif.html) for Paleosciences 

</exercise>

<exercise id="10" title="Paleoecological Analysis with Leaflet and Neotoma">

**Warning** neotoma2 will be released soon and this code will be updated with its new code.

Taken from:
[Advanced Neotoma for Fun and Profit](http://www.goring.org/resources/neotoma_lab_meeting.html#)
by [Simon Goring](http://www.goring.org/)

**What we’ll learn**
This tutorial is intended to act as a more complete vignette of the neotoma package’s functionality. 

**Data Exploration Made Easy**
It’s a bit of a pain to download lots of records and then visualize them in R, or at least, it had been. In building the package I wanted to try to limit the need to install lots of other packages, so the basic plot() method isn’t all that helpful.

<codeblock id="05_30">

</codeblock>

All Neotoma data points in Wisconsin, with symbols identifying dataset type.

So, we can see the different dataset types. You can pretty much make out Wisconsin, but it doesn’t look that great, and it’s certainly not publication quality. We can make a better map, an interactive map, using leaflet. 

<codeblock id="05_31">

</codeblock>

**2.1 Plotting stratigraphic diagrams**  
Let’s say we’re looking for all records from Wisconsin with Larix pollen, that must have some samples within the middle Holocene:

<codeblock id="05_32">

</codeblock>

You have all the advantages of the `Stratiplot()` function now, and the wrapper for the neotoma package makes it more useful directly with download objects.

</exercise>

<exercise id="11" title="Summary and Conclusions" type="slides">

<slides source="chapter5_05_summary_and_conclusions">

</slides>

</exercise>

