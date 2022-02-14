---
type: slides
---

<div><h1><img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module1/00_ec_slide1.png?raw=true" alt="EC Theme" width=25% align="left"/> Lesson 3<br>Data Workflows</h1></div>

---
## Dealing with Data

Data Science is the study, development and practice of reproducible and auditable processes to obtain insight from data. $^1$

From this definition, we must also define reproducible and auditable analysis:

Reproducible analysis:
reaching the same result given the same input, computational methods and conditions. $^2$

~~~
input = data
computational methods = computer code
conditions = computational environment (e.g., programming language & it's dependencies)
Auditable/transparent analysis,
a readable record of the steps used to carry out the analysis as well as a record of how the analysis methods evolved .
~~~

1. [National Academies of Sciences, 2019](https://www.nap.edu/catalog/25303/reproducibility-and-replicability-in-science)
2. [Parker, 2017](https://peerj.com/preprints/3210/) and [Ram, 2013](https://scfbm.biomedcentral.com/articles/10.1186/1751-0473-8-7)

---
## Motivation

Data products can be built via other methods, but we lack confidence in how the results or products were created.

We believe this stems from non-reproducible and non-auditable analyses:

- lacking evidence that the results or product could be regenerated given the same input computational methods, and conditions

- lacking evidence of the steps taken during creation

- having an incomplete record of how and why analysis decisions were made

---

## Making Data Science Trustworthy

- It should be reproducible and auditable
- It should be correct
- It should be fair, equitable and honest

---

## When Research Goes Wrong

An example with large impact

RETRACTED ARTICLE: Safety and efficacy of favipiravir versus hydroxychloroquine in management of COVID-19: A randomised controlled trial

A research paper was published in March 2021 that claimed that a drug, Favipiravir, was a safe and effective alternative to another drug, hydroxychloroquine (a medication commonly used to prevent or treat malaria), in mild or moderate COVID-19 infected patients.

---

## When Research Goes Wrong

In September, 2021 the paper we retracted by the editors - in part due to reproducibility issues:

"After concerns were brought to the Editors' attention after publication, the raw data underlying the study were requested. The authors provided several versions of their dataset. Post-publication peer review confirmed that none of these versions fully recapitulates the results presented in the cohort background comparisons, casting doubt on the reliability of the data. Additional concerns were raised about the randomisation procedure, as the equal distribution of male and female patients is unlikely unless sex is a parameter considered during randomisation. However, based on the clarification provided by the authors, sex was not considered during this process. The Editors therefore no longer have confidence in the results and conclusions presented."

---

## When Research Goes Wrong

The problem doesn't just stop once the article is retracted. Between the time the article was published and retracted, the article was cited 17 times!

The use of non-reproducible tools can impact government and industry as well! 

---

## Workflows Importance

- It makes it easier to collaborate with your most imporant collaborator - YOU in 6 months!
- It makes others think you know what you are doing.

---

## Workflows & complex projects

Complex projects have at least one item of the following list:

- two, or more, people directly working on the analysis
- projects that involve two or more coding documents
- projects that involve analysis of medium/large data
- projects where you are working on a remote machine
- projects that have many software or environment dependencies

As a project accumulates more of these features it grows further in complexity.

---

Complex projects without intentional Data Science workflows can result in:

- An result that you cannot recreate.
- Spare files of information related to the project that only you have access to.
- A small change to the analysis code requires re-running the entire program taking several hours.
- Code that can only be run on one machine (The "But it runs on my computer" problem)

---

## Avoiding the Chaos
Use:
- Version Control (Git & GitHub)
- Write Executable analysis scripts & pipelines (Python/R scripts)
- Defined & shippable dependencies as we saw (Docker)


---

## Version Control

- Use GitHub Issues for communications related to the project
- Version control contributes to better communication & team work
- All collaborators/team members know where to find the latest (or earlier) version of the analysis (code and output)

All collaborators/team members have access to all communications associated with the analysis

---

## Executable analysis scripts & pipelines

As analysis grows in length and complexity, one literate code document generally is not enough

To improve code report readability (and code reproducibility and modularity) it is better to abstract at least parts of the code away (e.g, to scripts)

These scripts save figures and tables that will be imported into the final report

Example problem solved by executable analysis scripts & pipelines
Problem: A small change to the analysis code requires re-running the entire thing, and takes hours.

Solution: Use a smart dependency tree tool to only re-run the parts that needs to be updated.

---

## Defined & shippable dependencies

Dependencies are other things one need to install to run your code, and includes:
- programming languages (e.g., R, Python, Julia, etc)
- packages from programming languates (e.g., tidyverse, scikit-learn)
- Dependencies include versions too

Example problem solved by defined & shippable dependencies
Problem: Code that can only be run on one machine, and you don't know why.

---

## Life cycle of a data analysis project

It is also critical that you match the correct data science methods to the type of statistical question you are asking.

---

## Descriptive

One that seeks to summarize a characteristic of a set of data. No interpretation of the result itself as the result is a fact, an attribute of the data set you are working with.

Examples:

How many people live in each US state?

---

## Exploratory

One in which you analyze the data to see if there are patterns, trends, or relationships between variables looking for patterns that would support proposing a hypothesis to test in a future study.

Examples:

Does air pollution correlate with life expectancy in a set of data collected from groups of individuals from several regions in the United States?

---

## Inferential

One in which you analyze the data to see if there are patterns, trends, or relationships between variables in a representative sample. We want to quantify how much the patterns, trends, or relationships between variables is applicable to all individuals units in the population.

Examples:

Is eating at least 5 servings a day of fresh fruit and vegetables is associated with fewer viral illnesses per year?

---

## Predictive

One where you are trying to predict measurements or labels for individuals (people or things). Less interested in what causes the predicted outcome, just what predicts it.

Examples:

How many viral illnesses will someone have next year?

---

## Causal

Asks about whether changing one factor will change another factor, on average, in a population. Sometimes the underlying design of the data collection, by default, allows for the question that you ask to be causal (e.g., randomized experiment or trial)

Examples:

Does smoking lead to cancer?

---

## Mechanistic

One that tries to explain the underlying mechanism of the observed patterns, trends, or relationship (how does it happen?)

Examples:

How does how airplane wing design changes air flow over a wing, leading to decreased drag?

---

## What happens next?

Knowing the kind of question you are trying to answer, helps narrow down the possibilities of the kind of analysis you might want to do.

For example, if you have the question: "How many viral illnesses will someone have next year?" and you identify that it is predictive. You could narrow down that some kind of statistical or machine learning model might help you answer that.

Then you need to go a step deeper and look at the data that you have, and see which kind of statistical or machine learning model is most suitable for your data.

---

# Let's Practice What We Learned