# -*- coding: UTF-8 -*-
import os
import tushare as ts
import numpy as np
import pandas as pd
import re
__author__ = 'shenxiangxiang@gmail.com'

basic_info_df = ts.get_stock_basics()
stock_list = basic_info_df.index

import os
this_file_path = os.path.dirname(os.path.abspath(__file__))
store_path = os.path.join(this_file_path,'data')
for stock in stock_list:
    store_file_name = os.path.join(store_path, stock+'.csv')
    ts.get_hist_data('600848',start='2014-10-01',end='2016-12-01').to_csv(store_file_name) #一次性获取全部日k线数据
#ts.get_hist_data('sh').to_csv('sh.csv')