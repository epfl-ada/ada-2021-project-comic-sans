"""
This is a file cointaing functions to help us process the datasets
"""
from tld import get_tld
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

def check_domain(domains, media):
    """
    This function checks if a media domain (string) is in given domains (list of strings)
    
    inputs
        domain : Quotebank column containing the domains of the quotes
        media : Specific media source eg. "nytimes"
    output
        Bool : Is the media in the given domains (True) or not (False) 
    """
    return media in domains

def subcategorybar(X, vals, colors_, number_of_figure,media, width=0.8):
    """
    This function is meant to plot a bar plot with different values (vals) for the same categorical variables (X). 
    It was designed with intention to plot the percentage of quotes about among certain topics for a specific media 
    and compare them with the overall percentages
    
    inputs
        X : Names of categorical variables (list of strings)
        vals : Different values for each categorical variable (list of list of ints)
        media : Name of the media for which the bar plot is designed
        width : Width of each bar
    ouput
        Plots the desired graph
    """
    plt.subplots(tight_layout=True)
    n = len(vals)
    _X = np.arange(len(X))
    colors = []
    for key in colors_:
        colors.append(colors_[key])
    for i in range(n):
        plt.bar(_X - width/2. + i/float(n)*width, vals[i]/vals[i].sum(), 
                width=width/float(n), align="edge", color = colors[i])   
    plt.xticks(_X, X)        
    labels = list(colors_.keys())
    handles = [plt.Rectangle((0,0),1,1, color=colors_[label]) for label in labels]
    plt.legend(handles, labels)
    title = "Topic distribution comparison for " + media
    xlabel_string = "Figure " + number_of_figure +"."
    #plt.xlabel(xlabel_string)
    plt.title(title)
    plt.savefig("topic_distribution.jpg")
    
def plot_env_group_percentage(df, attributes_to_plot, interested_attribute):
    """
    This function is used to plot the percentage of the quotes related to the environment
    made by a group of people in comparison to the total quotes made by the same group.
    
    inputs 
        df : Quotebank Dataframe
        attributes_to_plot : Groups of people that we're interested in
        interested_attribute : Attribute with which the groups are being formed (eg. nationality)
        
    outputs
        Plots the desired graph
    """
    percentages=[]
    for attribute in attributes_to_plot : 
        temp =  df[df[interested_attribute].apply(check_domain, args = (attribute,))]
        percentage = temp[temp.Environment_related ==1].shape[0] / temp.shape[0] * 100
        percentages.append(percentage)
    plt.figure(figsize = (2*len(attributes_to_plot),4))  
    #plt.subplots(tight_layout=True)
    colors = ["tab:green", "tab:orange", "tab:blue", "tab:red", "tab:purple",
              "tab:brown" ,"tab:pink" ,"tab:grey", "tab:olive", "tab:cyan"] 
    plot_total = plt.bar(attributes_to_plot, percentages,ec = "black",color = colors)
    plt.xlabel("Group of people")
    plt.ylabel("Percentage (%)")
    plt.title("Percentage of quotes related with the environment")
    save_title = interested_attribute + "_percentages.jpg"
    plt.savefig(save_title)
    
def check_qids(qids):
    """
    This function is used to determine if the qids for a given quote is 1 or more.
    
    inputs
        qids : List of qids
    output
        bool : 1 if the there is only 1 qid, 0 otherwise
    """
    return len(qids)==1