#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
import random


# In[3]:


data = pd.read_csv(r"C:\Users\Pranav\Downloads\Projects\Netflix-EDA-Practice-master\Netflix-EDA-Practice-master\netflix_titles.csv")


# In[3]:


data


# In[4]:


data.shape


# In[5]:


data.columns


# In[6]:


df = data.copy()


# In[7]:


df.shape


# Task.1) Is there any Duplicate Record in this dataset ? If yes, then remove the duplicate records.

# In[8]:


df.duplicated().sum()


# In[9]:


df.drop_duplicates()


# Task. 2) Is there any Null Value present in any column ? Show with Heat-map.

# In[10]:


null_values = df.isnull()
null_values


# In[11]:


null_values.sum()


# In[12]:


sns.heatmap(null_values)


# Q. 1) For 'House of Cards', what is the Show Id and Who is the Director of this show ?

# In[13]:


df.columns


# In[14]:


df[df['title'] =='House of Cards'][['show_id','director','title']]


# In[15]:


df[df['title'].isin(['House of Cards'])]


# In[16]:


df[df['title'].str.contains('House of Cards')]


# Q. 2) In which year the highest number of the TV Shows & Movies were released ? Show with Bar Graph.

# In[17]:


df['release_year'].value_counts()


# In[18]:


counts_sns = df.groupby('release_year')['show_id'].count().reset_index().sort_values(by='show_id', ascending = False)
counts_mat = df['release_year'].value_counts()


# In[19]:


sns.barplot(x='release_year', y='show_id', data=counts_sns, palette='viridis')


# In[20]:


plt.figure(figsize=(10, 6))
counts_mat.plot(kind='bar', color='skyblue')


# Q. 3) How many Movies & TV Shows are in the dataset ? Show with Bar Graph.
# 

# In[21]:


df.columns


# In[22]:


type_counts = df.groupby('type')['show_id'].count()
type_counts


# In[23]:


type_counts.plot(kind = 'bar')


# Q. 4) Show all the Movies that were released in year 2000.

# In[24]:


df[(df['release_year'] == 2000) & (df['type'] == 'Movie')][['title']]


# In[25]:


df['type'].unique()


# Q. 5) Show only the Titles of all TV Shows that were released in India only.

# In[26]:


df[(df['country'] == 'India') & (df['type'] == 'TV Show')][['title']]


# Q. 6) Show Top 10 Directors, who gave the highest number of TV Shows & Movies to Netflix ?

# In[27]:


df.columns


# In[28]:


df.groupby('director')['show_id'].count().sort_values(ascending = False).head(10)


# In[29]:


df['director'].value_counts().head(10)


# Q. 7) Show all the Records, where "Category is Movie and Type is Comedies" or "Country is United Kingdom".
# 
# 

# In[30]:


df.columns


# In[31]:


df[(df['listed_in'] == 'Comedies') & (df['type'] == 'Movie') | (df['country'] == 'United Kingdom')]


# Q. 8) In how many movies/shows, Tom Cruise was cast ?

# In[32]:


df['cast'].isnull().sum()


# In[33]:


df['cast'] = df['cast'].fillna("")


# In[34]:


df['cast'].isnull().sum()


# In[35]:


df[df['cast'].str.contains('Tom Cruise')]['title'].count()


# Q. 9) What are the different Ratings defined by Netflix ?

# In[36]:


df.columns


# In[37]:


df['rating'].unique()


# In[38]:


df['rating'].nunique()


# Q 9.1) How many Movies got the 'TV-14' rating, in Canada ?

# In[39]:


df[(df['rating'] == 'TV-14') & (df['type'] == 'Movie') & (df['country'] == 'Canada')]


# Q. 9.2) How many TV Shows got the 'TV-MA' rating, after year 2018 ?

# In[40]:


df[(df['rating'] == 'TV-MA') & (df['type'] == 'TV Show') & (df['release_year'] > 2018)]


# 10) What is the maximum duration of a Movie/Show on Netflix ?

# In[41]:


df.columns


# In[42]:


df['duration'].unique()


# In[43]:


df


# In[44]:



df[['duration']]


# In[45]:


df[['mins','units']] = df['duration'].str.split(" ",expand=True)


# In[46]:


df


# In[47]:


df['mins'].dtypes


# In[48]:


df['mins'] = pd.to_numeric(df['mins'])


# In[49]:


df['mins'].dtypes


# In[50]:


df['mins'].max()


#  Q 11) Which individual country has the Highest No. of TV Shows ?

# In[51]:


df[df['type'] == 'TV Show']['country'].value_counts().head(1)


# In[52]:


df


# Q. 12) How can we sort the dataset by Year ?

# In[53]:


df.sort_values(by = 'release_year',ascending=False)


# 13) Find all the instances where: Category is 'Movie' and Type is 'Dramas' or Category is 'TV Show' & Type is 'Kids' TV'

# In[54]:


df[(df['type'] == 'Movie') & (df['listed_in'] == 'Dramas') |(df['type'] == 'TV Show') & (df['listed_in'] == "Kids' TV")]


# In[55]:


df.columns


# In[56]:


df['listed_in'].unique()


# In[57]:


#Replacing Null with NA
df.isnull().sum()


# In[58]:


df['director'].fillna(' ', inplace = True)


# In[59]:


df.isnull().sum()


# In[60]:


df['country'].fillna('No Data', inplace = True)


# In[61]:


df.isnull().sum()


# In[66]:





# In[ ]:




