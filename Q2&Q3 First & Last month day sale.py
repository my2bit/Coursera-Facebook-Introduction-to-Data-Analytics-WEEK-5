#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[33]:


df_cleaned = pd.read_csv('data/inu_neko_orderline_clean.csv')
df_cleaned


# In[34]:


df_cleaned.info()


# #### Question 2: Alpha and Omega I
# What was the month and day of the first sale? Store as a tuple in that order and assign the tuple to the variable `first_date`.

# In[35]:


# 1. Make a new dataframe comprised of variables of interest: 'trans_month', 'trans_day'

df_sorted_ascending = df_cleaned[['trans_month', 'trans_day']]
print(df_sorted_ascending) # Print to verify


# In[36]:


# 2. Sort the new dataframe first on 'trans_month' and then on 'trans_day'.
# just like we do in spreadsheet, when we add levels

df_sorted_ascending = df_cleaned[['trans_month', 'trans_day']].sort_values(by = ['trans_month','trans_day'] )
print(df_sorted_ascending) # Print to verify


# In[37]:


# locate the row with least 'trans_month' and 'trans_day' values
# That means locate the value at index position 0.
first_date = df_sorted_ascending[['trans_month','trans_day']].iloc[0]
print(first_date)
type(first_date)


# In[42]:


# convert the first_date to a tuple.
first_date = (tuple(first_date))

first_date


# # Do the same for Q3 to locate the last value

# In[39]:


# Q3 - LATEST ORDER
df_sorted_ascending = df_cleaned.sort_values(by = ['trans_month','trans_day'] )
last_date = tuple(df_sorted_ascending[['trans_month','trans_day']].iloc[-1])
print(last_date)

print(type(last_date))


# In[40]:


# Q2 Test Cases
assert len(first_date) == 2
assert str(first_date[0]).isnumeric() 
assert str(first_date[1]).isnumeric() 





