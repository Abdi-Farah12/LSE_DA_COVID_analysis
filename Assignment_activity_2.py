#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

uk_cases = pd.read_csv('covid_19_uk_cases.csv')

uk_cases


# In[3]:


covid_uk_vaccinated = pd.read_csv('covid_19_uk_vaccinated.csv')

covid_uk_vaccinated


# In[4]:


global_data = pd.read_csv('global_data.csv')

global_data


# In[5]:


tweets = pd.read_csv('tweets.csv')

tweets


# In[11]:


# B: number of rows and columns

print(uk_cases.shape)
print(covid_uk_vaccinated.shape)
print(global_data.shape)
print(tweets.shape)


# In[14]:


# c: Data types

print(uk_cases.dtypes)


# In[16]:


# c: Data types

print(covid_uk_vaccinated.dtypes)


# In[17]:


# c: Data types

print(global_data.dtypes)


# In[18]:


# c: Data types

print(tweets.dtypes)


# In[28]:


# D: missing values

print(uk_cases.isnull().any(axis=1).sum())
print(covid_uk_vaccinated.isnull().any(axis=1).sum())
print(global_data.isnull().any(axis=1).sum())
print(tweets.isnull().any(axis=1).sum())


# In[34]:


# 4: Filter the data for the region Gibraltar as displayed in the covid_19_uk_cases.csv


uk_cases[uk_cases['Province/State']=='Gibraltar']


# In[35]:


# print the whole DataFrame

pd.set_option("display.max_rows", None)

uk_cases 


# In[37]:


# print the whole DataFrame

pd.set_option("display.max_rows", None)

covid_uk_vaccinated 


# In[38]:


# print the whole DataFrame

pd.set_option("display.max_rows", None)

global_data


# In[39]:


# print the whole DataFrame

pd.set_option("display.max_rows", None)

tweets 


# In[41]:


#Subset the Gibraltar DataFrame that you have created consisting of the following columns: Deaths, Cases, Recovered and Hospitalised.

gibraltar_cases = uk_cases[uk_cases['Province/State']=='Gibraltar']

gibraltar_cases


# In[47]:


# 6. Subset of the Gibraltar Df (Deaths, Cases, Recovered, Hospitalised)

gibraltar_subset = gibraltar_cases[['Deaths','Cases','Recovered','Hospitalised']]

gibraltar_subset


# In[ ]:




