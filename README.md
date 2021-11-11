# Climate change : The media's perspective

## Abstract
-> A bit hasty, will review this before tonight\
Earth is experiencing a climate emergency as the climate is currently changing more rapidly than ever before. People have to act but to do that first they have to understand the severity of the situation. In the scientific world, this has already been established years ago but what about the rest of the world ? The responsibility to communicate the causes, the consequences but also the means to limit global warming to normal people lies with the media. Our goal is to understand how the media has dealt with this situation by analyzing the quotes they reported about it. We will examine the quantity of quotes reported over time and their proportion compared to other topics. Moreover, we will explore how political movements such as climate strikes and conferences influence these quotes. Finally, we want to investigate the profile of the speakers quoted by the media when it comes to this issue. 


## Research Questions
1. What is the most common profile among the speakers that have talked about the enviroment ?
2. Which aspects of a person are more likely to prompt him to make a statement about the enviroment ?
3. How does the frequency of quotes concerning climate evolve over time ?
4. How do events such as Conference of the Parties affect the media's interest on our subject ?
5. What is the magnitude of the presence of enviromental quotes compared to other significant topics ?
6. What are some differences concerning the representation of the climate change from one media to another ? 

## Proposed additional datasets
- Wikidata : Will be used to obtain information about the speakers. Since we are only interested in quotes submitted between 2015 and 2020 speakers over some age will be eliminated. Eventually, only a few of their attributes will be held (gender, religion, education, party, nationality and age will be derived based on their date of birth). Finally, we will also add a column indicating if the speakers have expressed their views regarding our topic or not.


## Methods
- Data processing      : Starting with the Quotebank dataset 2 different kinds of subsets will be created. Firstly, we want a subset with all the quotes that we are certain about the speaker. This dataset will be used in combination with the Wikidata in the regression analysis as a part of our effort to estimate the profile of the speakers that have gone on record regarding views. Secondly, we want some subsets where they have all the quotes from a specific media. These datasets will later be used to compare the attitude of the equivalent medias towards climate change. 
- Topic Filtering      : A set of keywords is created based on glossaries associated with our topic ( [EPA](https://19january2017snapshot.epa.gov/climatechange/glossary-climate-change-terms_.html), [BBC](https://www.bbc.com/news/science-environment-11833685), [ipcc](https://www.ipcc.ch/sr15/chapter/glossary/)). Based on them a [pre-trained model](https://huggingface.co/transformers/main_classes/pipelines.html#transformers.ZeroShotClassificationPipeline) will determine the degree of confidence for which the quote is associated to climate change. The result of this process will be a Quotebank-derived dataset where all quotes are associated with the climate change. 
- Regression Analysis  : We will implement logistic regression on the Wikidata speaker's attributes dataset . Based on this analysis we will try to understand the role of their attributes (age, etc.) to their presence in the media concerning the climate change.
- Statistical Analysis :

## Proposed timeline
### Week 09 (12/11/21 - 18/11/21) : 
- Load data : Gather Quotebank and Wikidata datasets and extract the desired information
- Feature processing for Quotebank : Clean data (Remove inessential features, quotes without speaker, etc)
- Topic Filtering : Associate each quote with a topic 
- Topic Filtering : Gather all quotes associated with a certain topic 
### Week 10 (19/11/21 - 25/11/21) : 
- Feature processing for Wikidata : Get the speaker attributes ready to be used as a training set
- Logistic regression : Train our model, Optimize parameters based on accuracy
- Data exploration/Observational studies : Try to derive information in other ways than regression analysis
### Week 11 (26/11/21 - 02/12/21) : 
- Results : Explore and interpret our results
- Conclusions : Draw conclusions from our results and find efficient ways to present them 
### Week 12 (03/12/21 - 09/12/21) : 
- Visualization : Visual our results 
- Statistical analysis
- Commence our report/data story
### Week 13 (10/12/21 - 17/12/21) : 
- Double check everything
- Finalize Data story

## Organisation within the team
Communication : 
- Zoom meetings every Thursday at 20:00
- Every day whatsapp availability

Responsibilities for each member : 
- Ansgar   : 
- Nearchos : 
- Santiago :
- Stephane :

Matters to address : Topic Filtering, Regression Analysis, Data analysis/exploration, Visualization, Data story, Data handling, Data cleaning,Statistical analysis

## Questions for TAs
