#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 15:44:44 2022

@author: sergio
"""

import numpy as np
import pandas as pd

ref_labels = pd.read_csv('categories.csv')
classes = np.asarray(ref_labels['class'])
image = np.asarray(ref_labels['filename'])
labels = np.asarray(ref_labels['label'])

for a,b,c in zip(classes,image,labels):
    print(a,b,c)