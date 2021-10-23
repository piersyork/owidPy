#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 12:48:17 2021

@author: piers
"""
import os
os.chdir('/Users/piers/Documents/OWID/owidPy/owidPy')
os.getcwd()

from __init__ import Owid
import seaborn as sns
from owidPy import Owid

owid = Owid("legally-recognized-rights-to-land")


owid.data


owid = Owid("human-rights-scores")

owid.view_chart()

owidPy.owid_search('rights')

owid_search("legally-recognized-rights-to-land")

df = owid("legally-recognized-rights-to-land")

df

sns.lineplot(x = 'year', y = 'Fund for Peace (Fragile States Index (Human Rights Dimension))',
             hue = 'entity',
             data = df[df.entity.isin(['United Kingdom', 'United States'])])


