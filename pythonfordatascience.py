#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 20:03:38 2017

@author: gabbycastillo
"""

import pandas as pd

import pandas_datareader.data as web

import matplotlib.pyplot as plt

import datetime

from datetime import date


start = date(2016,1,1)

end = date.today()


stock_price = web.Datareader("TWTR", "google", start, end)

stock_price.tail()