# How green is the media ?

## Table of Contents
1. [Abstract](#Abstract)
2. [Research questions](#Research_questions)
3. [Proposed additional datasets and files](#Proposed_additional_datasets_and_files)
4. [Methods](#Methods)
5. [Repo organization](#Repo_organization)
5. [Proposed timeline](#Proposed_timeline)
6. [Organisation within the team](#Organisation_within_the_team)

## Abstract <a name="Abstract"></a>
Earth is experiencing a climate emergency as the climate is currently changing more rapidly than ever. In the scientific world, this has already been established but what about everyone else ? The responsibility to communicate the causes, the consequences but also the means to limit global warming to normal people lies with the media. Our goal is to understand how the media has responded to this crisis by investigating the role of media sources when reporting speakers' opinion by analyzing their quotes. We will examine the quantity of quotes reported over time and their proportion compared to other topics to obtain an estimate of the relevance of the topic at hand. Moreover, we identify key characteristics of speakers in a given media source and compare these characteristics between different news sources. Opinions are shaped daily by the media and therefore we believe holding them accountable when it comes to urgent matters like this is essential. 


## Research Questions <a name="Research_questions"></a>
1. What is the most common profile among the speakers that have talked about the enviroment? Which aspects of a person are more likely to prompt him to make a statement about the enviroment? (Speaker level)
2. How does the frequency of quotes concerning climate change evolve over time in general and specifically per media source? (time level). Event studies: How do events such as Conference of the Parties or climate strikes affect the media's interest on our subject ? (time level) -> 
3. What is the magnitude of the presence of enviromental quotes compared to other significant topics ?
5. What are some main characteristics of speakers being quoted about the environment by specific news sources?

## Proposed additional datasets and files <a name="Proposed_additional_datasets_and_files"></a>
- Wikidata : Will be used to obtain information about the speakers. Since we are only interested in quotes submitted between 2015 and 2020 speakers over some age will be eliminated. Eventually, only a few of their attributes will be retained (gender, religion, education, party, nationality and age will be derived based on their date of birth). Finally, we will also add a feature indicating if the speakers have expressed their views regarding our topic or not.
- processing.py : contains helper functions for some tasks in the notebooks and is used throughout the analysis.
- Google drive : contains relevant data sets that due to their size could not be included in the repo. We saved pre-processing results in that data file.

## Methods <a name="Methods"></a>
- Topic Filtering      : A set of keywords is created based on glossaries associated with our topic ( [EPA](https://19january2017snapshot.epa.gov/climatechange/glossary-climate-change-terms_.html), [BBC](https://www.bbc.com/news/science-environment-11833685), [ipcc](https://www.ipcc.ch/sr15/chapter/glossary/)). Based on a bag-of-words we simply go through the quotes and check whether the contains at least one of the words from our bag of words. If that is the case, we label the quote as 'deals with the environemnt' which we encode by a 1.  
- Exploratory data analysis: We explore the data using aggregations and vizualisations, for example to try and identify the most common features in the speakers that talk about the environment. The main method we used here is: for a certain feature, we calculate the ratio of environmental speakers that possess this feature, divided by the total number of speakers in out dataset that possess this feature. This ratio becomes the main metric with which we measure a speaker's likelihood to speak about the environment.
- Regression Analysis  : We will implement logistic regression on the Wikidata speaker's attributes dataset . Based on this analysis we will try to understand the role of their attributes (age, etc.) to their presence in the media concerning the climate change. This step also includes possible hypothesis tests on the parameters to evaluate the significance of the attributes.
- Statistical Analysis : Besides the regression analysis, we want to obtain summary statistics and distributions. Depending on the research question, we use frequency distributions, histograms, line plots and other visualization tools to investigate different variables.

## Repo Organization <a name="Repo_organization"></a>
```
|   .gitignore
|   data_filtering.ipynb
|   README.md
|   requirements.txt
|   research_question_1.ipynb
|   research_question_4.ipynb
|   
+---Data
|   |   enviroment_keywords.txt
|   |   
|   \---Keywords
|           brexit_keywords.txt
|           data_science_keywords.txt
|           environment_keywords.txt
|           gun_control_keywords.txt
|           lgbt_keywords.txt
|           README.md
|           
+---helpers
|       processing.py
|       
\---preprocessing
        speakers_preprocessing.ipynb

```
There are **4 main notebooks**, one for each research question that deal a bit more in depth with the corresponding question. 
- `research_question_1.ipynb`: Speaker profile analyis.
- `research_question_3.ipynb`: Multiple topic analysis in comparison to climate change
- `research_question_4.ipynb`: News paper specific speaker analysis

There are also the following directories:
- `Data`: Contains keywords and other topic filtering related files.
- `preprocessing`: Directory preprocessing and cleaning date related notebooks.
- `helpers`: Directory with file defining helper functions that are used throughout the notebooks for tasks such as extracting the domain from a url.

## Organisation within the team <a name="Organisation_within_the_team"></a>
- Stephane : Research question 1 (speakers analysis),Speakers Data Cleaning & Preprocessing & Repo management.
- Santiago : Research question 2 (time analysis) and extraction of domains.  
- Nearchos : Research question 3 (multiple topics analysis), Data Labeling, Keywords Dictionaries
- Ansgar   : Research question 4 (news source specific speaker analysis), Data Labeling
- Everyone : ReadMe, Data Story 




## Extras

### Link to the data
We've grouped all the data used for our analysis in one Google Drive which you can access [here](https://drive.google.com/drive/folders/14G9_lLPwmoQB343QE1sMTtHhNjgqD2am?usp=sharing).

### Python Packages
You can find all the required python packages to run our notebooks in `requirements.txt` found in the root of the project.

### Data Story
To check out our data story for this study go to https://stefnans.github.io/ada-2021-project-data-story/
