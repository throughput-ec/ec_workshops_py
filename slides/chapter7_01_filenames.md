---
type: slides
---

<div><h1><img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module1/00_ec_slide1.png?raw=true" alt="EC Theme" width=25% align="left"/> Lesson 1<br>File Names</h1></div>

---

# Three principles for (file) names:

- Machine readable
- Human readable
- Plays well with default ordering

---

## Machine readable

- Regular expression and globbing friendly
- Avoid spaces, punctuation, accented characters, case sensitivity
- Easy to compute on
- Deliberate use of delimiters

---

## Machine readable Motivation 

- Easy to search for files later

- Easy to narrow file lists based on names

- Easy to extract info from file names, e.g. by splitting

- New to regular expressions and globbing? be kind to yourself and avoid
    + Spaces in file names
    + Punctuation
    + Accented characters
    + Different files named `foo` and `Foo`

---

## Human readable

- Name contains info on content

- Connects to concept of a *slug* from semantic URLs

---

## Embrace the slug

Examples of names
```
01_marshal-data.r
helper01_load-counts.r
```

---

## Human readable Motivation

Easy to figure out what a file is, based on its name

---

## Plays well with default ordering

- Put something numeric first

- Use the ISO 8601 standard for dates

- Left pad other numbers with zeros

**Examples**

Chronological order
```
```

Logical order
```
```

Dates
```
```

---

## Left pad other numbers with zeros

If you don’t left pad, you get this:

~~~
10_final-figs-for-publication.R
1_data-cleaning.R
2_fit-model.R
~~~

---
## Examples of Good and Bad Names

**BIG NO**
```
myabstract.docx
Joe’s Filenames Use Spaces and Punctuation.xlsx
figure 1.png
fig 2.png
JW7d^(2sl@deletethisandyourcareerisoverWx2*.txt
```

**YES**
```
2014-06-08_abstract-for-sla.docx
joes-filenames-are-getting-better.xlsx
fig01_scatterplot-talk-length-vs-interest.png
fig02_histogram-talk-attendance.png
1986-01-28_raw-data-from-challenger-o-rings.txt
```

Source [Data Carpentry](https://datacarpentry.org/rr-organization1/01-file-naming/index.html)
---

# Let's Practice!
