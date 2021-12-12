"""
This is a file cointaing functions to help us process the datasets
"""
from tld import get_tld
import pandas as pd
import os
from tld import get_tld

def topic_filtering(df, topic_name, word_list):
    """
    Recieves a pandas.Dataframe (df) to which it adds a column with the topic's name (topic_name)
    indicating if the quote has a keyword that is included in the word_list (1) or not (0).
    
    inputs
        df : :Quotebank dataframe
        topic_name : Name of the topic that we investigate
        word_list : Text file including a list of words associated with the topic
    """
    with open(word_list) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    
    column_name = topic_name + "_related"
    df[column_name] = 0
    df.loc[df["quotation"].str.contains('|'.join(lines),case = False),column_name]=1
    

def get_domain(url):
    """
    Recieves the url as a string (url) and returs it's domain 
    eg. google.co.uk --> google
    
    inputs 
        url : The url as a string 
    outputs
        domain : The domain of the url
    """
    res = get_tld(url, as_object=True)
    domain = res.domain
    return domain 

def set_domains(urls):
    """
    Recieves a pd.Series of urls (urls) and returns a new pd.Series (domains)
    with the domains of those urls
    
    inputs
        urls : "urls" column from Quotebank dataset
    outputs
        domains : "domains" column for Quotebank dataset
    """
    domains = []
    for url in urls :
        tld = get_domain(url)
        domains.append(tld)
    return domains