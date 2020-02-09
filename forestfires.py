# -*- coding: utf-8 -*-

import pandas as pd

path = 'D:/Study/Data Analysis/dataset/forestfires.csv'

obj = pd.read_csv(path)
print(obj.head())