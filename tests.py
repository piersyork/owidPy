#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 12:48:17 2021

@author: piers
"""
import os
os.chdir('/Users/piers/Documents/OWID/owidPy/owidPy')
os.getcwd()

#from __init__ import Owid
import seaborn as sns
import matplotlib.pyplot as plt
from owidPy import Owid, owid_search
from plotnine import ggplot, aes, geom_line, theme, theme_538, labs, element_line, element_rect
from random import sample

owid_search("agric")


agric = Owid("agricultural-water-withdrawals")

agric.data


owid = Owid("legally-recognized-rights-to-land")


owid.data


owid = Owid("human-rights-scores")

owid.plot()

df = owid.data

sns.lineplot(x = 'year', y = 'Human Rights Score (Schnakenberg & Fariss, 2014; Fariss, 2019)',
             hue = 'entity',
             data = df[df.entity.isin(['United Kingdom', 'United States'])])
plt.title('Human Rights Score (Schnakenberg & Fariss, 2014; Fariss, 2019)')
ax = plt.axes()

plt.show()

(ggplot(df[df.entity.isin(['United Kingdom', 'United States'])],
        aes(x = 'year', y = 'Human Rights Score (Schnakenberg & Fariss, 2014; Fariss, 2019)',
            colour = 'entity'))
 + geom_line()
 + theme_538() 
 + labs(title = 'Human Rights Score (Schnakenberg & Fariss, 2014; Fariss, 2019)',
        x = '', y = '', colour = '')
 + theme(axis_line_x = (element_line(size = 0.5)), axis_ticks_major_x = (element_line()),
         legend_position = "bottom", legend_box_background = element_rect(fill = 'black'),
         aspect_ratio=(0.45))).draw()


entities = owid.data.entity.unique()
entities
owid.view_chart()

sample(list(entities), 5)

owidPy.owid_search('rights')

owid_search("legally-recognized-rights-to-land")

df = owid("legally-recognized-rights-to-land")

df

sns.lineplot(x = 'year', y = 'Fund for Peace (Fragile States Index (Human Rights Dimension))',
             hue = 'entity',
             data = df[df.entity.isin(['United Kingdom', 'United States'])])


