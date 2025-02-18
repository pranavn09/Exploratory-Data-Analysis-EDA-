#!/usr/bin/env python
# coding: utf-8

# In[201]:


import pandas as pd


# Dataset : https://www.kaggle.com/datasets/kaggle/sf-salaries

# In[202]:


data= pd.read_csv('Salaries.csv')
data


# # 1. Display top 10 Rows of the dataset

# In[203]:


data.head(10)


# # 2. Display Last 10 Rows of the dataset

# In[204]:


data.tail(10)


# # 3. Find Shape of our dataset (Number of rows and number of columns)

# In[205]:


data.shape


# In[206]:


print("Number of Rows : ", data.shape[0])
print("Number of Columns : ", data.shape[1])


# # 4. Getting information about our dataset like total number rows, Total number of columns, datatypes of each coloum and memory requirments

# In[207]:


data.info()


# # 5. Check null values in the dataset

# In[208]:


data.isnull().sum()


# # 6. Drop ID, notes, Agency and status columns 

# In[209]:


data= data.drop(['Id' ,'Notes' ,'Agency', 'Status'], axis=1) #axis=1 to drop columns and to drop rows use axis=0


# In[210]:


data


# # 7. Get overall Statistics of the Dataframe

# In[211]:


data.describe(include='all')


# # 8. Find occurence of the employee name(top 5)

# In[212]:


data.columns


# In[213]:


data['EmployeeName'].value_counts().head()


# # 9. Find the number of unique job titles 

# In[214]:


data.columns


# In[215]:


data['JobTitle'].nunique()


# # 10 Total number of job titles which contain Captain

# In[216]:


len(data[data['JobTitle'].str.contains("Captain", case=False )])


# # 11. Display all the employee names from the fire department

# In[217]:


data.columns


# In[218]:


data[data['JobTitle'].str.contains("Fire", case=False)]['EmployeeName']


# # 12. Find Minimum, Maximum, and Average BasePay 

# In[219]:


data['BasePay'].describe()


# # 13. Replace 'not provided' in Employee name column as NaN

# In[220]:


data.columns


# In[221]:


data[data['EmployeeName'].str.contains('Not Provided')].count()


# In[222]:


import numpy as np 
data['EmployeeName']=data['EmployeeName'].replace('Not provided', np.nan)


# In[223]:


data['EmployeeName']


# # 14. Drop the rows having 5 missing values

# In[224]:


data[data.isnull().sum(axis=1)==5]


# # 15. Find job title of ALBERT PARDINI

# In[225]:


data.columns


# In[226]:


data[data['EmployeeName']=='ALBERT PARDINI']['JobTitle']


# # 16. How much ALBERT PARDINI make (include benifit)

# In[227]:


data[data['EmployeeName']=='ALBERT PARDINI']['TotalPayBenefits']


# # 17. Display name of the person having the highest pay

# In[228]:


#data[data['BasePay'].max()==data['BasePay']] ['EmployeeName']


# In[229]:


# Assuming 'BasePay' is the column of interest in your DataFrame 'data'
data['BasePay'] = pd.to_numeric(data['BasePay'], errors='coerce')

# Find the employee name(s) with the maximum 'BasePay'
max_basepay_names = data.loc[data['BasePay'].idxmax(), 'EmployeeName']

# Print or use the employee name(s) as needed
print(max_basepay_names)


# # 18. Find average basepay of all employee per year

# In[230]:


data.groupby('Year').mean()['BasePay']


# # 19.  Find average basepay of all employee per Job title

# In[231]:


data.groupby('JobTitle').mean()['BasePay']


# # 20. Find average basepay of employee having job title ACCOUNTANT

# In[232]:


data[data['JobTitle'] == 'ACCOUNTANT']['BasePay'].mean()


# # 21. Find Top 5 most common jobs 

# In[233]:


data.columns


# In[234]:


data['JobTitle'].value_counts().head()


# In[ ]:




