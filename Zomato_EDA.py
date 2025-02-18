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


df = pd.read_csv(r"C:\Users\Sanskruti\Downloads\zomato_restaurants_in_India.csv")


# In[5]:


df.shape


# In[143]:


df.head(5)


# In[144]:


df.columns


# In[145]:


df.shape


# In[7]:


df[df['city'] == 'Pune']


# In[8]:


city_hotels = df['city'].value_counts()
city_hotels


# In[9]:


df.info()


# In[10]:


df.describe()


# In[12]:


#Remove Duplicates
df.duplicated()


# In[14]:


df.drop_duplicates(['res_id'],keep = 'first', inplace = True)


# In[15]:


df.shape


# In[16]:


df.isnull().sum()


# In[17]:


df['establishment'].unique()


# In[18]:


b =df['establishment'][0]#has unwanted brackets
b


# In[19]:


b[2:-2]


# In[20]:


df['establishment'] = df['establishment'].apply(lambda x: x[2:-2])

df.head()


# In[21]:


df['establishment'].unique()


# In[22]:


#df['establishment'] = df['establishment'].apply(lambda x : x == '')


# In[23]:


df['establishment'].replace(to_replace='', value = 'NA', inplace = True)


# In[24]:


df['establishment'].unique()


# In[25]:


df['city'].unique()


# In[26]:


df['city'].value_counts()


# In[43]:


df[df['city'] == 'Pune'].count()


# In[44]:


df['country_id'].value_counts()


# In[45]:


df['locality_verbose'].unique()


# In[46]:


df['locality_verbose']


# In[47]:


#cuisines              -    470 missing
df['cuisines'].unique()


# In[48]:


df['cuisines'] =df['cuisines'].fillna('No Cuisines')


# In[49]:


Cuisins_data = pd.DataFrame(df["cuisines"].value_counts())


# In[50]:


Cuisins_data.shape


# In[51]:


c = []
df['cuisines'].apply(lambda x : c.extend(x.split(', ')))
c = pd.Series(c)
c.nunique()


# In[52]:


print(df["highlights"].nunique())
print(df["highlights"].unique())


# In[53]:


df["highlights"]


# In[54]:


hl = []
df["highlights"].apply(lambda x : hl.extend(x[2:-2].split("', '")))
hl = pd.Series(hl)
print("Total number of unique highlights = ", hl.nunique())


# In[55]:


df[["aggregate_rating","votes","photo_count"]].describe().loc[["mean","min","max"]]


# Restaurant chains
# Here chains represent restaurants with more than one outlet

# In[56]:


df.columns


# In[57]:


outlets = df['name'].value_counts()
outlets


# In[58]:


chains = outlets[outlets >= 2]
chains


# In[59]:


single = outlets[outlets == 1]
single


# In[60]:


print("Total Restaurants = ", df.shape[0])
print("Total Restaurants that are part of some chain = ", df.shape[0] - single.shape[0])
print("Percentage of Restaurants that are part of a chain = ", np.round((df.shape[0] - single.shape[0]) / df.shape[0],2)*100, "%")


# In[61]:


top10_chains = chains.head(10).sort_values()
top10_chains


# In[75]:


height = top10_chains.values
bars = top10_chains.index
#y_pos = np.arange(len(bars))


#colors = ["green","blue","magenta","cyan","gray","yellow","purple","violet","orange","red","maroon"]
#random.shuffle(colors)
colors = ["#f9cdac","#f2a49f","#ec7c92","#e65586","#bc438b","#933291","#692398","#551c7b","#41155e","#2d0f41"]

plt.barh(top10_chains.index,top10_chains.values)

for i, v in enumerate(top10_chains.values):
    ax.text(v+3, i, str(v), color='#424242')
plt.title("Top 10 Restaurant chain in India (by number of outlets)")

plt.show()


# In[73]:


height = top10_chains.values
bars = top10_chains.index
y_pos = np.arange(len(bars))

fig = plt.figure(figsize=[11,7], frameon=False)
ax = fig.gca()
ax.spines["top"].set_visible("#424242")
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("#424242")
ax.spines["bottom"].set_color("#424242")

#colors = ["green","blue","magenta","cyan","gray","yellow","purple","violet","orange","red","maroon"]
#random.shuffle(colors)
colors = ["#f9cdac","#f2a49f","#ec7c92","#e65586","#bc438b","#933291","#692398","#551c7b","#41155e","#2d0f41"]
plt.barh(y_pos, height, color=colors)
 
#plt.xticks(color="#424242")

plt.yticks(y_pos, bars, color="#424242")
plt.xlabel("Number of outlets in India")

for i, v in enumerate(height):
    ax.text(v+3, i, str(v), color='#424242')
plt.title("Top 10 Restaurant chain in India (by number of outlets)")


plt.show()


# In[71]:


bars = top10_chains.index
y_pos = np.arange(len(bars))
y_pos


# Top restaurant chains (by average rating)

# In[101]:


top_5_rating = outlets[outlets > 4]
top_5_rating


# In[102]:


df.columns


# In[103]:


df['aggregate_rating']


# In[104]:


top10_chains2= df[df["name"].isin(top_5_rating.index)].groupby('name')['aggregate_rating'].mean().sort_values(ascending=False)[:10].sort_values(ascending=True)


# In[105]:


height = pd.Series(top10_chains2.values).map(lambda x : np.round(x, 2))
bars = top10_chains2.index
y_pos = np.arange(len(bars))

fig = plt.figure(figsize=[11,7], frameon=False)
ax = fig.gca()
ax.spines["top"].set_visible("#424242")
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("#424242")
ax.spines["bottom"].set_color("#424242")

#colors = ["green","blue","magenta","cyan","gray","yellow","purple","violet","orange","red","maroon"]
#random.shuffle(colors)
colors = ['#fded86', '#fce36b', '#f7c65d', '#f1a84f', '#ec8c41', '#e76f34', '#e25328', '#b04829', '#7e3e2b', '#4c3430']
plt.barh(y_pos, height, color=colors)

plt.xlim(3)
plt.xticks(color="#424242")
plt.yticks(y_pos, bars, color="#424242")
plt.xlabel("Number of outlets in India")

for i, v in enumerate(height):
    ax.text(v + 0.01, i, str(v), color='#424242')
plt.title("Top 10 Restaurant chain in India (by average Rating)")


plt.show()


# In[106]:


df.head()


# In[107]:


df['establishment'].value_counts()


# In[117]:


est_count = df.groupby('establishment').count()['res_id'].sort_values(ascending= False).head(5)


# In[118]:


est_count


# In[124]:




fig = plt.figure(figsize=[8,5], frameon=False)
ax = fig.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("#424242")
ax.spines["bottom"].set_color("#424242")

#colors = ["green","blue","magenta","cyan","gray","yellow","purple","violet","orange","red","maroon"]
#random.shuffle(colors)
colors = ["#2d0f41",'#933291',"#e65586","#f2a49f","#f9cdac"]
plt.bar(est_count.index, est_count.values, color=colors)

plt.xticks(range(0, 6), color="#424242")
plt.yticks(range(0, 25000, 5000), color="#424242")
plt.xlabel("Top 5 establishment types")

for i, v in enumerate(est_count):
    ax.text(i-0.2, v+500, str(v), color='#424242')
plt.title("Number of restaurants (by establishment type)")


plt.show()


# In[ ]:




