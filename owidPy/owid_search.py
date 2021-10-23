#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 16:59:37 2021

@author: piers
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_datasets():
    response = requests.get('https://ourworldindata.org/charts')
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all(['section', 'a'])
    
    titles = []
    urls = []
    for link in links:
        titles.append(link.text)
        urls.append(link.get('href'))
        
    dic = {'title': titles,
           'chart_id': urls}
    
    datasets = pd.DataFrame(dic)
    datasets = datasets[datasets.chart_id.str.contains('grapher') > 0].drop_duplicates()
    datasets.chart_id = datasets.chart_id.str.split(pat = '/').str[2]
    return datasets
    
def owid_search(term):
    datasets = get_datasets()
    
    return datasets[datasets.title.str.contains(term, case = False, regex = False) > 0]
    
    
    
    



    
    
    
    
    
    
    
    