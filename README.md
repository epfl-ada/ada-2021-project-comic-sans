# Climate change : The media's perspective

## Table of Contents
1. [Abstract](#Abstract)
2. [Research questions](#Research_questions)
3. [Proposed additional datasets and files](#Proposed_additional_datasets_and_files)
4. [Methods](#Methods)
5. [Proposed timeline](#Proposed_timeline)
6. [Organisation within the team](#Organisation_within_the_team)
7. [Questions for TAs](#Questions_for_TAs)

### Required libraries: numpy, pandas, matplotlib, seaborn, transformers, pytorch, tensorflow, pyarrow
If any of the above listed packaged are not installed, please pip install them.

## Abstract <a name="Abstract"></a>
Earth is experiencing a climate emergency as the climate is currently changing more rapidly than ever. In the scientific world, this has already been established but what about everyone else ? The responsibility to communicate the causes, the consequences but also the means to limit global warming to normal people lies with the media. Our goal is to understand how the media has responded to this crisis by investigating the role of media sources when reporting speakers' opinion by analyzing their quotes. We will examine the quantity of quotes reported over time and their proportion compared to other topics to obtain an estimate of the relevance of the topic at hand. Moreover, we identify key characteristics of speakers in a given media source and compare these characteristics between different news sources. Opinions are shaped daily by the media and therefore we believe holding them accountable when it comes to urgent matters like this is essential. 


## Research Questions <a name="Research_questions"></a>
1. What is the most common profile among the speakers that have talked about the enviroment and climate change ?
2. Which aspects of a person are more likely to prompt him to make a statement about the enviroment ?
3. How does the frequency of quotes concerning climate evolve over time in general and specifically per media source?
4. Event studies: How do events such as Conference of the Parties or climate strikes affect the media's interest on our subject ?
5. What is the magnitude of the presence of enviromental quotes compared to other significant topics ?
6. What are some differences concerning the representation of the climate change from one media to another ? 

## Proposed additional datasets and files <a name="Proposed_additional_datasets_and_files"></a>
- Wikidata : Will be used to obtain information about the speakers. Since we are only interested in quotes submitted between 2015 and 2020 speakers over some age will be eliminated. Eventually, only a few of their attributes will be retained (gender, religion, education, party, nationality and age will be derived based on their date of birth). Finally, we will also add a feature indicating if the speakers have expressed their views regarding our topic or not.
- ml.py : Python script with a class that is responsible for the regression analysis. Contains functions such as loading and splitting the data into training and test sets, applying logistic regression and calculating the accuracy of the results based on the test set.


## Methods <a name="Methods"></a>
- Data processing      : Starting with the Quotebank dataset, 2 different kinds of subsets will be created.  Firstly, a subset will contain all quotes whose speaker is identified. This dataset will be used in combination with the Wikidata in the regression analysis as a part of our effort to estimate the profile of the speakers that have gone on record regarding their views. Secondly, we want some subsets where they have all the quotes from a specific media source. These datasets will later be used to compare the attitude of the equivalent medias towards climate change. 
- Topic Filtering      : A set of keywords is created based on glossaries associated with our topic ( [EPA](https://19january2017snapshot.epa.gov/climatechange/glossary-climate-change-terms_.html), [BBC](https://www.bbc.com/news/science-environment-11833685), [ipcc](https://www.ipcc.ch/sr15/chapter/glossary/)). Based on them a [pre-trained model](https://huggingface.co/transformers/main_classes/pipelines.html#transformers.ZeroShotClassificationPipeline) will determine the degree of confidence for which the quote is associated to climate change. The result of this process will be a Quotebank-derived dataset where all quotes are associated with the climate change. 
- Regression Analysis  : We will implement logistic regression on the Wikidata speaker's attributes dataset . Based on this analysis we will try to understand the role of their attributes (age, etc.) to their presence in the media concerning the climate change. This step also includes possible hypothesis tests on the parameters to evaluate the significance of the attributes.
- Statistical Analysis : Besides the regression analysis, we want to obtain summary statistics and distributions. We would like to infer how the overall distribution of quotes per news article has evolved over time (number of quotes per month in th New York Times for example). Further, we visualize the key characteristics that speakers have per news source independent of the topic addressed to get an impression of whether a news source might be biased towards citing people with certain views or characteristics.

## Proposed timeline <a name="Proposed_timeline"></a>
### Week 09 (12/11/21 - 18/11/21) : 
- Load data : Gather Quotebank and Wikidata datasets and extract the desired information.
- Feature processing for Quotebank : Clean data (Remove inessential features, quotes without speaker, etc).
- Topic Filtering : Gather all quotes associated with climate change using the transformers pipeline. 
### Week 10 (19/11/21 - 25/11/21) : 
- Feature processing for Wikidata : Get the speaker attributes ready to be used as a training set, investigate potential dublicates of features for one speaker.
- Logistic regression : Train our model, optimize parameters based on accuracy and/or MLE from standard packages.
- Data exploration/Observational studies : Try to derive information in other ways than regression analysis by looking at distributions, histograms, line plots, averages and other statistical estimates.
### Week 11 (26/11/21 - 02/12/21) : 
- Results : Explore and interpret our results.
- Conclusions : Draw conclusions from our results and find efficient ways to present them.
### Week 12 (03/12/21 - 09/12/21) : 
- Visualization : Visual our results.
- Statistical analysis and hypothesis testing.
- Commence our report/data story
### Week 13 (10/12/21 - 17/12/21) : 
- Double check everything.
- Finalize Data story.

## Organisation within the team <a name="Organisation_within_the_team"></a>
Communication : 
- Zoom meetings every Thursday at 20:00.
- Every day whatsapp/zulip availability.

Responsibilities for each member : 
- Ansgar   : Regression Analysis, Visualization, Data story, 
- Nearchos : Data cleaning/handling ,Statistical analysis, Visualization, Data story, 
- Santiago : Topic Filtering, Visualization, Data story, 
- Stephane : Data analysis/exploration,Visualization, Data story, 
