---
title: 'Module 1: Intro to Python and Jupyter Notebooks'
description:
  'In this module, you will learn how to write basic Python code 
  and how to use your Jupyter Notebooks.'
prev: null
next: /module2
type: chapter
id: 1
---
<exercise id="1" title="Why Python?">

You might be wondering why you should be learning Python.

Python is widely used in the scientific community and it is a great tool to help you further advance your geosciences research.

We will present you with the most important reasons to start using Python in the following [link](https://foundations.projectpythia.org/foundations/why-python.html).

</exercise>

<exercise id="2" title = "Getting Started with Python">

Now that you know why you should be learning Python, let's get started!

Read the [Quickstart zero to Python](https://foundations.projectpythia.org/foundations/quickstart.html) article and try to run the code using Binder.

*Tip*: Make sure you open the Binder link under the "Rocket Ship" in another window. This may take a while to build so you may want to have it run in the background while you read the article).

But what exactly is Binder? Binder allows you to run code in a pre-defined environment without installing anything on your computer. The environment is installed on the Binder servers. One of the features of Binder is that it has no memory. So once you close your Binder session, none of the variables or files you download on the server will be there. Remember this as you work through the exercises. Each block of code launches a different Binder. Therefore, if you create a variable in Exercise 3, it's not available in Exercise 4 unless you create it again.

Once you are done with the tutorials, complete the exercises below to test your understanding!

Be patient - it might take a few minutes the first time you run the code. But it usually speeds up.

**Question:**

1. Print "I love doing paleoclimate research with Python" on the console.

<codeblock id="01_01">

Remember to use the print command!

</codeblock>

</exercise>

<exercise id="3" title = "Playing with lists">

**Question:**

Lists are one of the basic elements in Python and allows you to build more sophisticated objects. It is common to rely on this data structure for some of its functionalities. Lists are also a great way to loop through information.

1. Create a list with the following archives: `Marine Sediment`, `Coral`, `Ice`, `Wood`
2. Loop over the list to print: "I study paleoclimate using " [archive]

<codeblock id="01_02">
Remember that lists are defined between `[]`

Lists can have any kind of elements in it - `strings` included.

You can concatenate strings using `+`.

For example,

```
str1 = "I love Python"
str2 = " and I can't wait to use it in paleoclimate research"

str = str1 + str2
```
str is now "I love Python and I can't wait to use it in paleoclimate research"

</codeblock>

</exercise>

<exercise id="4" title = "Playing with dictionaries">

A dictionary is a map between key-value pairs.

For example:

A location has a `latitude` and a `longitude`.
`latitude` and `longitude` are the keys and the coordinate numbers are the values.

How does this look in terms of a data structure?

```python
location = {'latitude': 49.26, 'longitude' : -123.24}
```

**Question:**

1. Create a dictionary called `dataset1`, that have the following keys: `archiveType`, `geo`, `data`.
2. Set the value for archiveType to `marinesediment`
3. Set the value for `geo` to another dictionary with keys `lat` and `lon`. The `lat` value is `-5` and the `lon` value is `140`
4. Set the value for `data` to a dictionary with keys `values` (set to a list of `[1,2,3]`) and `units` (set to `N/A`)
5. Return the value of the latitude information into a new variable called `latitude`

<codeblock id="01_03">

When using nested dictionaries, you can access the value in the nested dictionary by chaining the keys.

</codeblock>

What happens if you don't know which keys are available to you? You can print it out as follows:

<codeblock id="01_04">

</codeblock>

</exercise>

<exercise id="5" title="Introduction to Basic NumPy">

~~~
NumPy is the fundamental package for scientific computing in Python.   
It is a Python library that provides a multidimensional array object,  
various derived objects (such as masked arrays and matrices), and an  
assortment of routines for fast operations on arrays, including 
mathematical, logical, shape manipulation, sorting, selecting, I/O,  
discrete Fourier transforms, basic linear algebra, basic statistical  
operations, random simulation, and much more. 
- NumPy Documentation
~~~

This section contains Project Pythia's tutorials on array computing with NumPy.  
We recommend using the provided Binder link to run the code.

[NumPy Basics](https://foundations.projectpythia.org/core/numpy/numpy-basics.html)  
[NumPy Basics Binder](https://mybinder.org/v2/gh/ProjectPythia/pythia-foundations/main?urlpath=lab/tree/core/numpy/numpy-basics.ipynb)

**Question:**

1. Create a NumPy array that starts at 0, ends at 1000, with 1001 points and save it into a variable called `time`
2. What is the value of time at index 20? Return this value into the variable `time_index`

<codeblock id="01_05">

1-D NumPy arrays can be indexed the same way as lists.

</codeblock>

If you are new to programming, your first question might be: "What is an array?". An array is a collection of values (numbers, strings, or such), whose position in the computer's memory is such that it can be computed from its given key. Coming from the Excel world, you could regard a spreadsheet as a 2D array; a single column of that spreadsheet would be a 1D array. Arrays, however, are far more general, and can assume any dimension, which makes them great for storing large quantities of information.

**Question:**

It is often useful to create pseudo-data to test out a function. For instance, it could be useful to pass a timeseries with known periodicities to look at the effect of noise or uneven sampling on the different methods. In this case, you may need to create a time and value axis that would mimic a time series.

Let's start by creating a perfect series:
1. Create a time vector that starts at year 1, ends at year 2000 and is annually resolved. Use `numpy.arange` to do so
2. Create a sinusoidal signal corresponding to the time vector with a periodicity of 20 years.

<codeblock id="03_01">
To create a sine wave, look whether numpy has a functionality to do so in [their documentation](https://numpy.org/doc/stable/index.html).

The mathematical formula is: sin(2 pi * freq * time)

</codeblock>

**Question:**

Let's add noise to our series.
1. Create a time vector that starts at year 1, ends at year 2000 and is annually resolved. Use `numpy.arange` to do so
2. Create a perfect sinusoidal signal corresponding to the time vector with a periodicity of 20 years.
3. Use [`numpy.random.Generator.normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html) to create a white noise that samples from a normal distribution with zero mean and half the variance in the signal.
4. Add the noise vector to your signal

Look at the first line after package import. This allows you to use the same seed for the random number generator, which makes your results reproducible.

<codeblock id="03_02">

Remember that the variance is the square of the standard deviation.

So the scale will be `np.sqrt(np.var(value)/2)`

</codeblock>

</exercise>

<exercise id="6" title="Intermediate NumPy">

Now that you have the basics if NumPy, let's move on to more advanced functionalities. Review the article below from Project Pythia and use the associated Binder for training exercises.

[Intermediate NumPy](https://foundations.projectpythia.org/core/numpy/intermediate-numpy.html)

[Intermediate NumPy Binder](https://mybinder.org/v2/gh/ProjectPythia/pythia-foundations/main?urlpath=lab/tree/core/numpy/intermediate-numpy.ipynb)

Question:

One of the most routine manipulations of paleoclimatology is to take a timeslice of the data. Let's do this using NumPy.

1. Create a time vector that starts at year 1, ends at year 2000 and is annually resolved. Use `numpy.arange` to do so
2. Create a perfect sinusoidal signal corresponding to the time vector with a periodicity of 20 years.
3. Slice the value data for the 200-400 year period, inclusive

<codeblock id="03_03">

To get the indexes of the slice, you can use [this function](https://numpy.org/doc/stable/reference/generated/numpy.where.html).

Remember that slice notation is **exclusive** of the final index.

</codeblock>

**Question:**

Another task we love to perform is wrangling age models. You can think of each age model being stored along one dimension of a NumPy array. Therefore, it is possible to wrangle them the same way you would any other array. Let's build a fake age model, add some noise to create an ensemble and take the mean (in reality, you may only need to perform the last operation but it's good practice to play with the random generator you used in exercise 1).

1. Create a time vector between 0 and 10000 in 100 years increments
2. Use a seed of 30 to initialize the random generator
3. Duplicate the time vector to obtain 1000 copies. The resulting array should have each model stored in the column. The rows should correspond to 'depth'
4. Create a noise vector with standard deviation 200 years
5. Add the noise vector to the original ensemble
6. Take the mean

<codeblock id="03_04">

</codeblock>

</exercise>

<exercise id="7" title="Introduction to Pandas">

Pandas is a very powerful library for working with tabular data (i.e. anything you might put in a spreadsheet – a common data type in the geosciences). It allows us to use labels for our data so that we can write expressive and robust code to manipulate the data.

Key features of Pandas are the ability to read in tabular data, slice and dice data, and exploratory analysis tools native to the library.

Follow this Project Pythia tutorial on Pandas.

[Introduction to Pandas](https://foundations.projectpythia.org/core/pandas/pandas.html)

[Introduction to Pandas Binder](https://mybinder.org/v2/gh/ProjectPythia/pythia-foundations/main?urlpath=lab/tree/core/pandas/pandas.ipynb)

In the materials above, you have seen how to download a dataset and open it with Pandas. You can also pass the dataset directly into the `read_csv` functionality. Try the code below:

<codeblock id="04_01">
</codeblock>

**Question:**

1. Open the ENSO dataset (you may copy and paste the answer from above)
2. Create a `Pandas.Series` object using the Nino12 Series
3. Slice for the 1982-2010 period
4. Plot the timeseries for the sliced Nino12 series

<codeblock id="04_02">

Remember that they are more than one way to skin a cat with Pandas. Choose the slicing method that is the most convenient (index, label)

</codeblock>


</exercise>

<exercise id="8" title="Introduction to Matplotlib">

~~~
Matplotlib is a comprehensive library for creating static, animated, and 
interactive visualizations in Python.
- Matplotlib documentation
~~~

Matplotlib is the go-to library for plotting within Python, with many functionalities and names reminiscent of Matlab's plotting libraries. Matplotlib comes with very good default parameters, so you can get visualizing within a few minutes of installing it. It is also extensively customizable, and can be used to make publication-quality graphics.

if you were to learn a single plotting tool to keep in your toolbox, this is the package.

The key feature to Matplotlib is its extensibility and the extensive [documentation](https://matplotlib.org) available to the community. Matplotlib underlies many other graphics libraries, including Cartopy (next chapter), and Pyleoclim, so it is essential that you understand a bit about it.


As before, we recommend looking over the [Pythia Matplotlib tutorial](https://foundations.projectpythia.org/core/matplotlib/matplotlib-basics.html) first. 

We recommend that you use the provided [Binder link](https://mybinder.org/v2/gh/ProjectPythia/pythia-foundations/main?urlpath=lab/tree/core/matplotlib/matplotlib-basics.ipynb) to follow along the article.


### A First Plot 

We start by loading and plotting the [NINO3 sea-surface temperature](https://climatedataguide.ucar.edu/climate-data/nino-sst-indices-nino-12-3-34-4-oni-and-tni) data. Notice that the code uses pandas (see Chapter 4) to load it; your job is to plot NINO3 vs time and annotate the plot by giving it appropriate labels (with units) and title.


<codeblock id="05_01">

Look up the documentation at https://matplotlib.org/stable/index.html!

</codeblock>

Notice that this call to the `subplots` method created:
-  a [figure](https://matplotlib.org/stable/api/figure_api.html?highlight=figure#module-matplotlib.figure) object `fig`
-  an [axes](https://matplotlib.org/stable/api/axes_api.html?highlight=axes#module-matplotlib.axes) object `ax`, to which the plot method is applied.  

For such a simple chart, the distinction is immaterial, but it will soon be important to distinguish between figure and axes, particularly when we create figures with multiple subplots.

If you wanted to change the size of the figure to 10 by 6 inches, say, you would replace the first line of the figure by:
```
fig, ax = plt.subplots(figsize=(10, 6))
```

We now explore Matplotlib's infinite customizability. All default parameters are stored in a dictionary called `rcParams`.
rc stands for "runtime configuration" and any changes to `plt.rcParams` will stay for all subsequent plots in your session. These parameters can be customised and [saved for later use](https://matplotlib.org/stable/tutorials/introductory/customizing.html#customizing-with-matplotlibrc-files).

For instance, the default figure size can be found as:
```
plt.rcParams['figure.figsize']
```
Typing this in your Binder should return `[6.0, 4.0]`

Let us now customize our plot. First, we might want to remove [chart junk](https://www.darkhorseanalytics.com/blog/data-looks-better-naked) (visual elements that clutter the display without bringing any data-related information to the table. The top and right spines of the chart, for instance, are totally useless, so let's remove them.

You can see how to do so [here](https://matplotlib.org/stable/api/spines_api.html?highlight=spines#matplotlib.spines.Spines)

Apply this to the code from the previous block and see the result:

<codeblock id="05_02">
https://stackoverflow.com/questions/925024/how-can-i-remove-the-top-and-right-axis-in-matplotlib
</codeblock>


If you want to make this a general feature of all your plots, it is more convenient to set this property as part of the rcParams, like so:

```
plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.top'] = False
```

In a Jupyter notebook or another iPython session (e.g. in Spyder), those spines would then be removed from all subsequent plots.


</exercise>

<exercise id="9" title="Intermediate Matplotlib">

### Making and customizing compound figures

In many instances, figures are composed of several subplots. Here you learn how to make and customize such plots in Matplotlib. First, let's add another panel to plot the second series, All India Rainfall, and label everything so someone might actually be able to interpret these plots.

```
fig, ax = plt.subplots(2,1,figsize=(10, 6),sharex = True)
ax[0].plot(t,nino3)
ax[0].set_ylabel('NINO3 SST (K)')
ax[0].set_title('NINO3 and All India Rainfall')
ax[1].plot(t,air)
ax[1].set_ylabel('AIR (mm/month)')
ax[1].set_xlabel('Year AD')
```

Notice that we used `sharex = True` to tell the `figure` command that the two subplots had a common x axis, to remove some redundancy. If you're curious, try removing that and see what it does.

Now we want to customize the appearance of the plot a bit more:
- look up the [documentation](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_fontdict.html#sphx-glr-gallery-text-labels-and-annotations-text-fontdict-py) to see how to make the font bold and set its size to 18.
- change the font of the y-axes labels to 'Helvetica'.

<codeblock id="05_03">
Look up the documentation at https://matplotlib.org/stable/index.html!
</codeblock>


### A plot with two y axes

Let's preface this exercise by saying that including multiple axes on the same graph is [one of the surest ways to lie with data](https://www.callingbullshit.org/tools/tools_misleading_axes.html). However, when done responsibly, it can save space and allow to compare comparable timeseries.  Here's how to do it for those series:

```# plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(t,nino3,label='NINO3',color='C0')
ax.set_ylabel('NINO3 SST (K)')
ax.set_title('NINO3 and All India Rainfall',fontweight='bold')
ax.legend()
# twin object for two different y-axis on the sample plot
ax2=ax.twinx()
ax2.plot(t,air,label='AIR',color='C1')
ax2.set_xlabel('Year AD')
ax2.legend()
```
Type `?plt.plot` or search StackOverflow to figure out how to repeat the figure above but change the line colors to red and green and adjust the transparency of the top curve to 0.6 so both are clearly visible.

<codeblock id="05_04">
Look up the documentation at https://matplotlib.org/stable/index.html!
</codeblock>

### Using Style Sheets

Making publication-quality plots can involve quite a bit of customization, which gets tedious after a while. Thankfully, Matplotlib has implemented a number of [styles](https://matplotlib.org/3.5.1/gallery/style_sheets/style_sheets_reference.html), which are predefined dictionaries of plotting parameters governing just about every imaginable aspect of plots. Here we demonstrate how to apply these pre-defined styles to the previous plot. There are two main ways to do so:
1. Setting a style for a whole kernel/session, which will affect the graphical style of all subsequent plots.
1. Setting a style as context for a particular plot, not affecting the graphical style of all subsequent plots in your notebook.

First, we create a _function_ to avoid repeating too many lines of code:

```
def nino3_air_plot(plot_title):
    fig, ax = plt.subplots()
    ax.plot(t,nino3,label='NINO3',color='C0')
    ax.set_ylabel('NINO3 SST (K)')
    ax.set_title(plot_title)
    ax.legend()
    # twin object for two different y-axis on the sample plot
    ax2=ax.twinx()
    ax2.plot(t,air,label='AIR',color='C1')
    ax2.set_xlabel('Year AD')
    ax2.legend()
```
The function produces that double y-axis plot with NINO3 and AIR with all the relevant information (variable names, units) but no customization. Use code below to loop through available styles and illustrate them on this particular plot:

<codeblock id="05_05">
https://www.dunderdata.com/blog/view-all-available-matplotlib-styles
</codeblock>

### Visualizing Relationships

So far we have only played with line plots, but if the goal is to compare two series, one might also explore a [scatterplot](https://matplotlib.org/3.5.1/api/_as_gen/matplotlib.pyplot.scatter.html?highlight=scatter#matplotlib.pyplot.scatter). Let's do this below, using the `ggplot` style.

Edit the code block to produce a scatterplot with AIR on the y axis and NINO3 on the x axis. In order to see overlapping points, give each one an opacity of 30%.

<codeblock id="05_06">
The parameter regulating transparency/opacity is called alpha, and this is how you use it: https://www.adamsmith.haus/python/answers/how-to-change-the-transparency-of-lines-in-matplotlib-in-python.
</codeblock>

### Adding color as an extra dimension

The plot is interpretable, but we have lost an opportunity for insight by giving each dot the same color. Wouldn't it be nice if each dot's color reflected the time it represents? Luckily we can do this very simply by specifying `c = t` in the call to `scatter`. The colormap argument is `cmap`, and you can pick any [colormap](https://matplotlib.org/stable/tutorials/colors/colormaps.html).

Repurpose the code above to do this with:
- a 12 by 8 in size
- [seaborn-whitegrid](https://python-graph-gallery.com/104-seaborn-themes) plot style
- scatter plot circles with 70% opacity colored by year, using a viridis colormap.

<codeblock id="05_07">
https://stackoverflow.com/questions/17682216/scatter-plot-and-color-mapping-in-python
</codeblock>

</exercise>

<exercise id="10" title="Introduction to Cartopy">

~~~
Cartopy is a Python package designed for geospatial data processing in order
to produce maps and other geospatial data analyses.

Cartopy makes use of the powerful PROJ.4, NumPy and Shapely libraries and
includes a programmatic interface built on top of Matplotlib for the creation of
publication quality maps.

Key features of Cartopy are its object-oriented projection definitions, and its
ability to transform points, lines, vectors, polygons and images between those
projections.
- Cartopy documentation
~~~

Before doing the tutorials, make sure that you already have a basic familiarity with Matplotlib.

Cartopy’s cartographic features library includes shapefiles directly served by Natural Earth. It sometimes takes a minute for the code to access those databases behind the scenes, so be prepared for that.

This tutorial will lead you through some basics of creating maps with specified projections with Cartopy, and adding geographic features like coastlines, borders, topography, and landmarks. We will cover:

1. Basic concepts: map projections and `GeoAxes`
2. Explore some of Cartopy's map projections
3. Mapping a record's site

Before we dive in, please look at:

[Introduction to Cartopy](https://foundations.projectpythia.org/core/cartopy/cartopy.html)
[Introduction to Cartopy Binder](https://mybinder.org/v2/gh/ProjectPythia/pythia-foundations/main?urlpath=lab/tree/core/cartopy/cartopy.ipynb)

### A basic map

Recall that in Matplotlib, what we might traditionally term a *figure* consists of two key components: a `figure` object and an associated `axes` object.

By importing Cartopy, we can convert the `axes` into a `GeoAxes` by specifying a projection that we have imported from *Cartopy's Coordinate Reference System* class as `ccrs`. This will effectively [*georeference*](https://www.usgs.gov/faqs/what-does-georeferenced-mean) the subplot.

Here we'll create a GeoAxes that uses the `PlateCarree` projection (basically a global lat-lon map projection, which translates from French to "flat square" in English, where each point is equally spaced in terms of degrees).

<codeblock id="06_01">
This is just a demo. Relax and enjoy!
</codeblock>

Although the figure seems empty, it has in fact been georeferenced, using one of Cartopy's map projections that is provided by Cartopy's `crs` (coordinate reference system) class. We can now add in cartographic features, in the form of *shapefiles*, to our subplot. One of them is `coastlines`, which is a callable `GeoAxes` method that can be plotted directly on our subplot.

<codeblock id="06_02">
This is just a demo. Relax and enjoy!
</codeblock>

Cartopy provides other cartographic features via its `features` class, which are imported as `cfeature`. These are also shapefiles, downloaded on initial request from https://www.naturalearthdata.com/. Once downloaded, they "live" in your `~/.local/share/cartopy` directory (note the `~` represents your _home_ directory). We add them to our subplot via the `add_feature` method. We can define attributes for them in a manner similar to Matplotlib's `plot` method. A list of the various Natural Earth shapefiles appears in https://scitools.org.uk/cartopy/docs/latest/matplotlib/feature_interface.html .

<codeblock id="06_03">
This is just a demo. Relax and enjoy!
</codeblock>

Finally, we can add topography as a "stock image". Notice how cartopy has the good taste to plot it _under_ administrative boundaries, so the latter are visible:

<codeblock id="06_04">
This is just a demo. Relax and enjoy!
</codeblock>

Pretty, isn't it? You are now ready to explore the dizzying world of projections.

### Projections

As you probably know, it is impossible to represent a 3-dimensional object like Earth on a 2D surface (a map) without tear or deformation (try it with an [orange](https://rabernat.github.io/research_computing_2018/maps-with-cartopy.html#The-major-problem-with-map-projections)). A plethora of projections are available, each with different pros and cons, deforming distances, areas, or angles in different ways. The default "Plate Carrée" projection used above is a so-called [equirectangular projection](https://en.wikipedia.org/wiki/Equirectangular_projection), in which meridians and parallels are always at right angles, but distances and areas can be severely distorted: for instance, on such a map Greenland (410,450 km^2) appears to have the same size as Australia, which in reality is an order of magnitude larger (7,741,220 km2). To quantify this effect, Cartopy's `tissot` method allows to plot the Tissot's ellipses of distortion (["indicatrix"](https://en.wikipedia.org/wiki/Tissot%27s_indicatrix)), like so:

<codeblock id="06_05">
This is just a demo. Relax and enjoy!
</codeblock>

You can find a list of supported projections in Cartopy, with examples, https://scitools.org.uk/cartopy/docs/latest/reference/crs.html.

Let us try the Mollweide projection, which is appropriate for thematic world maps illustrating area characteristics and analysis requiring accurate areas. This time, we'll define an object to store our projection definition. Any time you wish to use this particular projection later in a notebook, you can use the object name rather than repeating the same call to `ccrs`.

<codeblock id="06_06">
This is just a demo. Relax and enjoy!
</codeblock>

**Exercise 6.1**
Pick another projection, plot the globe with topography + administrative boundaries, and represent the projection's distortion using Tissot's indicatrix. Can you find a projection that accurately represents the area ratio between Greenland and Australia?

<codeblock id="06_07">
Look up projections at https://scitools.org.uk/cartopy/docs/latest/reference/crs.html !
</codeblock>

### Local Maps

Now, let's go back to PlateCarree, but let's use Cartopy's `set_extent` method to restrict the map coverage. Let's also choose a lower resolution for coastlines, just to illustrate how one can specify that. And we'll plot lat/lon lines as well, for good measure. The reference for Natural Earth's three resolutions (10m, 50m, 110m; higher is coarser) is at https://www.naturalearthdata.com/downloads/.

<codeblock id="06_08">
This is just a demo. Relax and enjoy!
</codeblock>

 Note the in the `set_extent` call, we specified a **PlateCarree** projection. This ensures that the values we passed into `set_extent` will be _transformed_ from degrees into the values appropriate for the projection we use for the map (numbers between 0 and 1, in Matplotlib).

Let us now use these features to create a regional map centered over Ukraine in Lambert Conformal projection. Be patient: with a limited regional extent as specified here, the highest resolution (10m) shapefiles are used; as a result (as with any `GeoAxes` object that must be transformed from one coordinate system to another), this will take longer to plot, particularly if you haven't previously retrieved these features from the Natural Earth shapefile server.

<codeblock id="06_09">
This is just a demo. Relax and enjoy!
</codeblock>

To highlight the country we use [this geopandas solution](https://stackoverflow.com/a/47885128/4984978), and to save ourselves a lot of repeating, we define a function:

<codeblock id="06_10">
This is just a demo. Relax and enjoy!
</codeblock>

A common use case for mappping in the paleosciences is to display the location of a point of interest, e.g. the site of sample collection. This is done very easily by re-using Matplotlib functions like [text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html?highlight=text#examples-using-matplotlib-axes-axes-text). On the map below we add a dot and a label for the city of Kyiv:

<codeblock id="06_12">
This is just a demo. Relax and enjoy!
</codeblock>

Now that you know to do it for cities, you can do it for any geolocated sample.

### Plotting a field on the sphere

In addition to plotting the location and geographic context of a sampling site, or of a collection of sites, one might want to plot climate fields (e.g. temperature), which vary continuously over time and space.  To simplify matters, let us use NumPy to define a field of our own on a bespoke lat-lon grid, then plot it with (you guessed it) Matplotlib:

<codeblock id="06_14">
This is just a demo. Relax and enjoy!
</codeblock>

Plotting data on a Cartesian grid is equivalent to plotting data in the Plate Carrée projection, where meridians and parallels are all straight lines with constant spacing. As a result of this simplicity, the global datasets we use often begin in the Plate Carrée projection.

Once we create our map again, we can plot this data as a contour map. We also need to specify the projection we are transforming _from_ (i.e. the projection our data is currently in) using the `transform` argument. Let's plot our data in the Mollweide projection to see how shapes change under a transformation.

<codeblock id="06_15">
This is just a demo. Relax and enjoy!
</codeblock>

Note that [contourf](https://matplotlib.org/3.5.1/api/_as_gen/matplotlib.pyplot.contourf.html) and [colorbar](https://matplotlib.org/3.5.1/api/_as_gen/matplotlib.pyplot.colorbar.html) are standard Matplotlib functions. As usual, Cartopy only offers a mapping from the regular display on a rectangular set of axes to a projection on the sphere, by specifying `projection` in the creation of the `Axes` object (here, with `plt.subplot`, but there are other ways) and by specifying a coordinate mapping (`transform=ccrs.PlateCarree()`) in the call to the plotting function itself (here, `contourf`). The lesson is that _any_ Matplotlib function can be used on top of Cartopy, allowing to represent virtually anything on the sphere. Oh, and it works on [other planets](https://github.com/eleanorlutz/mars_geology_atlas_of_space), too.

### The plot thickens: Uniting Time and Space into Cohesive Narratives

Maps need not be standalone objects; they are often interwoven with other displays to create a cohesive graphical narrative. In other words, every figure tells a story, and as [Edward Tufte](https://www.edwardtufte.com/tufte/) reminds us, stories are often about time and place. In this last exercise we revisit the dataset NINO3 and All-India Rainfall to add a spatial dimension to what was (so far) a purely temporal narrative.  

We start by plotting the two series, and adding a map underneath to provide spatial context:

<codeblock id="06_16">
This is just a demo. Relax and enjoy!
</codeblock>

This is an OK plot; that is to say, it is labeled enough to be interpretable, but it won't make the cover of Nature. Notice how we foolishly used different colors for the variables and their geographic context between the two subplots. Wouldn't it be _so_ much better if the colors echoed each other from subplot to subplot, to assert correspondences at the subconscious level? Also, topography is not terribly useful here, and needlessly clutters the plot.

**Exercise 6.4**
Color-coordinate the two plots, using the [Cn notation](https://matplotlib.org/stable/tutorials/colors/colors.html?highlight=cn). Also, flip the map and the timeseries, so the map is on top, and remove topography.

<codeblock id="06_17">
See the previous codeblock and re-use at will! Only a few minor tweaks are needed.
</codeblock>

</exercise>

<exercise id="11" title="Getting Started with Jupyter">

Read the following [article](https://foundations.projectpythia.org/foundations/getting-started-jupyter.html) to know more about what Jupyter is.


Then, read this [link](https://foundations.projectpythia.org/foundations/jupyterlab.html) to learn particularly about JupyterLab. Follow the exercises on an extra tab/window using the provided [Binder](https://mybinder.org/v2/gh/ProjectPythia/pythia-foundations/main?urlpath=lab/tree/foundations/jupyterlab.ipynb)

</exercise>