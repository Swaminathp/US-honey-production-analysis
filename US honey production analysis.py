#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import important library

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv('US_honey_dataset (5).csv')
df.head()


# In[3]:


# Droping the unnecessary columns

df = df.drop(columns = "Unnamed: 0", axis = 1)


# In[4]:


df.head()


# # Understanding the data

# In[5]:


df.shape


# In[6]:


df.info()


# In[7]:


df['state'].value_counts()


# # Statistical Analysis

# In[8]:


df.describe(include='all')


# # Top honey producing states

# In[42]:


df_2 = df.sort_values('production', ascending = False)
df_2


# # Visualization

# In[13]:


plt.figure(figsize = (30,30))
sns.barplot(x= df_2['production'], y = df_2['state'])
plt.xlabel('Honey Production')
plt.ylabel('States')
plt.show


# As per our findings, 'California', 'NorthDakota', 'SouthDakota', 'Florida' and 'Montana' are the top five 
# honey producing states

# In[14]:


plt.figure(figsize = (30,30))
sns.barplot(x= df_2['production'], y = df_2['state'])
plt.xlabel('Honey Production')
plt.ylabel('States')
plt.show


# # Least Honey producing States

# In[17]:


df_3 = df.sort_values('production')
df_3.head()


# # Change in average price of honey from 1995 to 2021

# In[21]:


df_4 = df.groupby('year', as_index=False)['average_price'].mean()
df_4
plt.figure(figsize = (30,30))
sns.barplot(x='year', y='average_price', data=df_4, palette='coolwarm')


plt.xlabel('year')
plt.ylabel('average_price')
plt.title('Bar Plot of Average Price by Year')


plt.show()


# In[33]:


plt.figure(figsize = (30,30))
sns.lineplot(x='year', y='average_price', data=df_4)


plt.xlabel('year')
plt.ylabel('average_price')
plt.title('Bar Plot of Average Price by Year')


plt.show()


# In[32]:


x= df_4['year']
y = df_4['average_price']
plt.figure(figsize = (30,30))
sns.barplot(x=x, y=y)
for i in range(len(x)):
    plt.text(i, y[i],str(round(y[i],2)), ha = 'center', va = 'bottom')




plt.show()


# # Highest honey producing year

# In[52]:


df_high = df_2.groupby('year', as_index=False)['production'].mean()
df_high[df_high['production'] == df_high['production'].max()]


# # Visualizing Pie Chart

# In[61]:


plt.figure(figsize= (30,30))
myexplode = [0.1]*df_high['year'].count()

plt.pie(df_high['production'], labels = df_high['year'], autopct = '%1.2f%%', explode = myexplode)
plt.show()


# # Highest price of honey 

# In[63]:


df[df['average_price'] == df['average_price'].max()]


# # Highest number of colonies

# In[73]:


df[df['colonies_number'] == df['colonies_number'].max()]


# # Visualize highest number of colonies

# In[72]:


plt.figure(figsize=(30,30))
sns.barplot(x= df['state'], y= df['colonies_number'])
plt.xticks(rotation=90)
plt.xlabel('States')
plt.ylabel('No. of colonies')
plt.show()


# # Important findings
# 
# This is the honey production data of US, from 1995 to 2021
# 
# The key insights are as below:
# 
# Highest honey producing States = "North Dakota", "California", "South Dakota", "Folrida', "Montana"
# 
# Highest honey production year = 2000 (production = 5.123721e+06)
# 
# Highest average price for honey = 2017 (874)
# 
# Highest number of colonies = 	NorthDakota	(550000)
#  
