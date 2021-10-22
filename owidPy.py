#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 16:59:37 2021

@author: piers
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_data_url(chart_id):
    url = f"https://ourworldindata.org/grapher/{chart_id}"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    preload_link = soup.find_all('link', attrs = {'rel':'preload'})[0].get('href')

    full_url = f"https://ourworldindata.org{preload_link}"
    
    return full_url
    


def owid(chart_id):
    data_url = get_data_url(chart_id)

    json_raw = requests.get(data_url).json()

    vars = json_raw['variables']

    datasets = []
    for i in vars:
        data_dict = {'entity': vars[i]['entities'],
                     'year': vars[i]['years'],
                     'value': vars[i]['values']}
        datasets.append(pd.DataFrame(data_dict))
        print(datasets)  

    
owid("human-rights-scores")








    
    
    
    
    
    
    
    