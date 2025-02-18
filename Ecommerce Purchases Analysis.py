#!/usr/bin/env python
# coding: utf-8

# In[98]:


import pandas as pd


# Dataset: https://www.kaggle.com/datasets/utkarsharya/ecommerce-purchases/data

# In[7]:


data = pd.read_csv('Ecommerce Purchases')
data


# 
# # 1. Display top 10 rows of the dataset
# 

# In[8]:


data.head(10)


# # 2. Check last 10 rows of the dataset

# In[9]:


data.tail(10)


# # 3. Check Datatype of each coloumn

# In[11]:


data.dtypes


# # 4. Check Null values in the dataset
# 

# In[13]:


data.isnull().sum()


# # 5. How many rows and columns there in the dataset
# 

# In[17]:


len(data.columns)


# In[19]:


len(data)


# In[20]:


data.info()


# # 6. Highest and lowest Purchase Prices

# In[27]:


#On what coloumn we should work on?
print(data.columns)
print('We need to work on Purchase Price')


# In[28]:


data['Purchase Price']


# In[32]:


print('Highest Purchase Price : ',data['Purchase Price'].max())
print('Lowest Purchase Price : ',data['Purchase Price'].min())


# # 7. Average Purchase Price

# In[34]:


print('Average Purchase Price : ',data['Purchase Price'].mean())


# # 8. How many people have French 'fr' as their language

# In[36]:


data.columns


# In[40]:


len(data[data['Language'] =='fr'])


# In[42]:


data[data['Language'] =='fr'].count()


# # 9. Find Job Title which contain Engineer

# In[43]:


data['Job']


# In[49]:


len(data[data['Job'].str.contains('Engineer',case=False)])


# # 10. Find email of the person with the following IP Address : 132.207.160.22
# 

# In[53]:


data.columns


# In[55]:


data[data['IP Address']=='132.207.160.22']


# # 11. How many people have Mastercard as their Credit card provider and made a purchase above 50?

# In[64]:


len(data[(data['CC Provider']=='Mastercard') & (data['Purchase Price']>=50)])


# # 12. Find email of the person with the following Credit card number : 4664825258997302

# In[69]:


data[data['Credit Card'] == 4664825258997302]['Email']


# # 13. How many people purchase during the AM and how many people purchase during PM? 

# In[76]:


data['AM or PM'].value_counts()


# # 14. How many people have a credit card that expires in 2020?

# In[77]:


data['CC Exp Date']


# In[86]:


def func():
    count=0
    for date in data['CC Exp Date']:
        if date.split('/')[1]=='20':
            count=count+1
    print(count)


# In[87]:


func()


# In[90]:


data['CC Exp Date'].apply(lambda x:x[3:]=='20').sum()


# # 15. Top 5 most polpular email providers

# In[93]:


list1=[]
for email in data['Email']:
    list1.append(email.split('@')[1])


# In[94]:


data['temp']=list1


# In[95]:


data.head(1)


# In[96]:


data['temp'].value_counts().head(5)


# In[ ]:




