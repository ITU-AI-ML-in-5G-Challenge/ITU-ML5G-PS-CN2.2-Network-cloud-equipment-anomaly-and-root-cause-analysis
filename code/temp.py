# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 14:54:25 2021

@author: ZDD
"""

import numpy as np
train = ['abc',
         'acc',
         'a']
# from preprocessing import FeatureExtractor
import preprocessing
feature_extractor = preprocessing.FeatureExtractor()

x = np.array(train)
y = feature_extractor.fit_transform(x, 'tf-idf')