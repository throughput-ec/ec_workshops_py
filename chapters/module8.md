---
title: 'Module 8: Argoviz'
description:
  'This module will help you work with the Argoviz Database and showcase a detailed example.
  This Module has been produced by the Argoviz team.'

prev: null
next: null
type: chapter
id: 7
---

<exercise id="0" title="Intro to Argoviz">

You will learn more about the Argoviz API during the hackathon.

In order to get started, make sure that you load your libraries and  
have the URL prefix defined:

```python
# prefix to use with all API queries
URL_PREFIX = 'https://argovis-api.colorado.edu'
```

You should also pass your API key - if you don't have one, your work will be limited.
```python
# users that have an API key would use it in their code (no need to do so here)
API_KEY   = ''
```

We have defined a function `check_error_message()` for you that checks the response JSON 
from an API; it is loaded in a script called `utilities.py`

The code of the function looks as follows:

```python
# check_error_message

def check_error_message(ans,writeFlag=False):
    # ans: response JSON from an API query
    # writeFlag: bool, true == print verbose errors, if found
    # returns error code if found, or NaN if not.
    if isinstance(ans,dict) and 'message' in ans.keys() and 'code' in ans.keys():
        if writeFlag:
            print(str(ans['code']) + ': ' + ans['message'])
        ##### NOTE: we should include here below all the codes that do not return data as the user expects
        if ans['code'] >= 400 and ans['code'] != 404:
            print('Data were not returned')
            print(ans)
            raise Exception('No data')
        return ans['code']        
    elif ans:
        return np.nan

```

To run this modules properly, you must import this function by doing:

``` python
from utilities import check_error_message
```

Let's declare some space-time variables we'll use to filter our search results by in the following examples. Dates are encoded as ISO 8601 UTC datestrings, and polygons are defined as lists of [lon, lat] pairs; to construct a polygon interactively:

visit argovis.colorado.edu
draw a shape
click on the purple shaded area of the region of interest (not on a dot)
from the pop up window, go "to Selection page"
from the url of the selection shape, copy the shape, i.e. [copy_all_this_inside_outer_brackets] after 'shape='


<codeblock id="08_01">


</codeblock>

To see what this polygon looks like, scroll over [East of Africa](https://argovis.colorado.edu/ng/home?mapProj=WM&presRange=%5B0,2000%5D&selectionStartDate=2018-04-27&selectionEndDate=2018-04-28&threeDayEndDate=2022-04-05T03:45:47&shapes=%5B%5B%5B25.106205,61.096076%5D,%5B10.054482,51.933279%5D,%5B9.236052,60.37706%5D,%5B8.221804,68.777189%5D,%5B7.034482,77.130969%5D,%5B19.816425,71.404221%5D,%5B25.106205,61.096076%5D%5D%5D&includeRealtime=true&onlyBGC=false&onlyDeep=false&threeDayToggle=false)


</exercise>

<exercise id="1" title="Mapping Data">

Now that you saw the data directly on the browser, it is time to extract it in Python.

Let's use the Argovis API to query Argo profile locations of interest

*If interested in GO-SHIP data instead, use cchdo_go-ship as source in the url.*

<codeblock id="08_02">

Play around with the code, look at different columns.

</codeblock>

Using your previous pandas skills, take different views at the dataframe, explore with `describe`, `info` or view some of the columns of the information you just extracted.

<codeblock id="08_03">

Play around with the code, look at different columns.

</codeblock>

</exercise>

<exercise id="2" title="Plot with Cartopy">

Let's use the previous code to extract some latitudes and longitudes first, then, let's plot them using Cartopy.

<codeblock id="08_04">


</codeblock>

Let's finally add the Cartopy code to see the visualization:

<codeblock id="08_05">


</codeblock>

Well done! 

Remember you can run all this code in the available [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/argovis/nsf_ec_tac_edu/HEAD) as well

</exercise>
