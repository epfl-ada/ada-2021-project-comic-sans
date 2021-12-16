# Climate change : The media's perspective

## Table of Contents
1. [Abstract](#Abstract)
2. [Research questions](#Research_questions)
3. [Proposed additional datasets and files](#Proposed_additional_datasets_and_files)
4. [Methods](#Methods)
5. [Repo organization](#Repo_organization)
5. [Proposed timeline](#Proposed_timeline)
6. [Organisation within the team](#Organisation_within_the_team)


### Required libraries: numpy, pandas, matplotlib, seaborn, statsmodels, pytorch, tensorflow, pyarrow, datetime
[TODO: remove]

## Abstract <a name="Abstract"></a>
Earth is experiencing a climate emergency as the climate is currently changing more rapidly than ever. In the scientific world, this has already been established but what about everyone else ? The responsibility to communicate the causes, the consequences but also the means to limit global warming to normal people lies with the media. Our goal is to understand how the media has responded to this crisis by investigating the role of media sources when reporting speakers' opinion by analyzing their quotes. We will examine the quantity of quotes reported over time and their proportion compared to other topics to obtain an estimate of the relevance of the topic at hand. Moreover, we identify key characteristics of speakers in a given media source and compare these characteristics between different news sources. Opinions are shaped daily by the media and therefore we believe holding them accountable when it comes to urgent matters like this is essential. 


## Research Questions <a name="Research_questions"></a>
1. What is the most common profile among the speakers that have talked about the enviroment and climate change ? (speaker level) -> Santiago, Stephane
2. Which aspects of a person are more likely to prompt him to make a statement about the enviroment ? (speaker level) -> 
3. How does the frequency of quotes concerning climate change evolve over time in general and specifically per media source? (time level) 
4. Event studies: How do events such as Conference of the Parties or climate strikes affect the media's interest on our subject ? (time level) -> 
5. What is the magnitude of the presence of enviromental quotes compared to other significant topics ?
4. What are some main characteristics of speakers being quoted about the environment by specific news sources?

## Proposed additional datasets and files <a name="Proposed_additional_datasets_and_files"></a>
- Wikidata : Will be used to obtain information about the speakers. Since we are only interested in quotes submitted between 2015 and 2020 speakers over some age will be eliminated. Eventually, only a few of their attributes will be retained (gender, religion, education, party, nationality and age will be derived based on their date of birth). Finally, we will also add a feature indicating if the speakers have expressed their views regarding our topic or not.
- processing.py : contains helper functions for some tasks in the notebooks and is used throughout the analysis.
- Google drive : contains relevant data sets that due to their size could not be included in the repo. We saved pre-processing results in that data file.

## Methods <a name="Methods"></a>
- Topic Filtering      : A set of keywords is created based on glossaries associated with our topic ( [EPA](https://19january2017snapshot.epa.gov/climatechange/glossary-climate-change-terms_.html), [BBC](https://www.bbc.com/news/science-environment-11833685), [ipcc](https://www.ipcc.ch/sr15/chapter/glossary/)). Based on a bag-of-words we simply go through the quotes and check whether the contains at least one of the words from our bag of words. If that is the case, we label the quote as 'deals with the environemnt' which we encode by a 1.  
- Regression Analysis  : We will implement logistic regression on the Wikidata speaker's attributes dataset . Based on this analysis we will try to understand the role of their attributes (age, etc.) to their presence in the media concerning the climate change. This step also includes possible hypothesis tests on the parameters to evaluate the significance of the attributes.
- Statistical Analysis : Besides the regression analysis, we want to obtain summary statistics and distributions. Depending on the research question, we use frequency distributions, histograms, line plots and other visualization tools to investigate different variables.

## Repo Organization <a name="Repo_organization"></a>
There are **4 main notebooks**, one for each research question that deal a bit more in depth with the corresponding question. We also have a data folder that contains the files that have been created while preprocessing the data and are used for furhter analysis. Moreover, a processing.py file contains some useful functinos that are used throughout the notebooks for tasks such as extracting the domain from a url.
- `milestone_2.ipynb`: project notebook
- `helpers`: package with python files defining helper functions
- `old`: directory with unused and draft notebooks
- `colab`: contains the google colab notebook template

## Organisation within the team <a name="Organisation_within_the_team"></a>
- Ansgar   : Research Question 4, ReadMe
- Nearchos : Research Question 3(?), Data Labeling
- Santiago : Research Question 2(?)  
- Stephane : Research Question 1, Data Cleaning and Processing

### Link to the data
We've grouped all the data used for our analysis in one Google Drive which you can access [here](https://drive.google.com/drive/folders/14G9_lLPwmoQB343QE1sMTtHhNjgqD2am?usp=sharing).
