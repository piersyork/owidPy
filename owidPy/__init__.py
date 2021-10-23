#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 14:43:26 2021

@author: piers
"""
from search import owid_search
import requests
from bs4 import BeautifulSoup
import pandas as pd
from functools import reduce
#from plotnine import ggplot, geom_line, aes, theme_538
import webbrowser


class Owid:
    def __init__(self, chart_id):
        self.chart_id = chart_id
        self.url = self.get_data_url()
        self.data = self.get_data()
        self.data_info = ""
        
    def get_data(self):
        data_url = self.url
        json_raw = requests.get(data_url).json()

        vars = json_raw['variables']

        datasets = []
        for i in vars:
            val_name = vars[i]['name']
            data_dict = {'entity_id': vars[i]['entities'],
                         'year': vars[i]['years'],
                         val_name: vars[i]['values']}
            #data = pd.DataFrame(data_dict).rename('')
            datasets.append(pd.DataFrame(data_dict))
    
        all_data = reduce(lambda x, y: pd.merge(x, y, on = ['entity_id', 'year']), datasets)
        
        entity_ids = list(json_raw['entityKey'].keys())
        codes = []
        entities = []
        
        for id in entity_ids:
            codes.append(json_raw['entityKey'][id]['code'])
            entities.append(json_raw['entityKey'][id]['name'])
    
        entity_key_dict = {'entity_id': entity_ids,
                           'entity': entities,
                           'code': codes}
    
        entity_key = pd.DataFrame(entity_key_dict)
        
        all_data['entity_id'] = all_data['entity_id'].astype(str)
        
        data = all_data.merge(right = entity_key, how = 'left', on = 'entity_id')
        
        data = data[['entity', 'code'] + [c for c in data if c not in ['entity', 'code']]]
        
        data.pop('entity_id')
    
        return data
        
        
    def get_data_url(self):
        chart_id = self.chart_id
        url = f"https://ourworldindata.org/grapher/{chart_id}"

        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        preload_link = soup.find_all('link', attrs = {'rel':'preload'})[0].get('href')
    
        full_url = f"https://ourworldindata.org{preload_link}"
    
        return full_url
    
    def view_chart(self):
        webbrowser.open(f'https://ourworldindata.org/grapher/{self.chart_id}')
    
