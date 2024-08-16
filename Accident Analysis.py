#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df=pd.read_csv("C:/Users/nitik/Downloads/US_Accidents_March23.csv")


# In[3]:


df


# In[4]:


df.columns


# In[5]:


df.info


# In[6]:


df.info()


# In[7]:


df.describe()


# In[10]:


numerics=['float64', 'int64']
numeric_df=df.select_dtypes(include=numerics)
len(numeric_df.columns)


# In[11]:


df.isna()


# In[12]:


df.isna.sum()


# In[14]:


df.isna().sum().sort()


# In[18]:


miss_percentage=df.isna().sum().sort_values(ascending=False)/len(df)


# In[21]:


miss_percentage[miss_percentage !=0].plot(kind='barh')


# In[22]:


df.columns


# In[24]:


df.City


# In[25]:


df.City.unique()


# In[10]:


cities_acci=df.City.value_counts()


# In[11]:


cities_acci


# In[12]:


cities_acci[:20]


# In[14]:


'New York' in df.City


# In[15]:


'Newyork' in df.City


# In[19]:


cities_acci[:10].plot(kind='barh')


# In[17]:


cities_acci[:20].plot(kind='barh')


# In[6]:


import seaborn as sns


# In[21]:


sns.set_style('darkgrid')


# In[25]:


sns.distplot(cities_acci)


# In[26]:


high_accident_cities=cities_acci[cities_acci>1000]
low_accident_cities=cities_acci[cities_acci<1000]


# In[27]:


len(high_accident_cities)


# In[30]:


percentage=len(high_accident_cities)/len(cities_acci)


# In[32]:


percentage*100


# In[34]:


cities_acci[cities_acci==1]


# In[36]:


df.Start_Time


# - new york data not available
# - less tha 9 percent cities has accidents > 1000
# - miami has the heighest number of accidents
# - 1023 cities has only reported one accident

# In[37]:


df.Start_Time=pd.to_datetime(df.Start_Time)


# In[39]:


df.Start_Time


# In[42]:


sns.histplot(df.Start_Time.dt.hour, bins=24)


# -high number of accidents occur between 7-9 , 5-6

# In[44]:


sns.histplot(df.Start_Time.dt.day_of_week, bins=7)


# In[1]:


df.Source.value_counts().plot(kind='pie')


# In[5]:


df.Start_Lat


# In[9]:


sample=df.sample(int(0.1*len(df)))


# In[10]:


sns.scatterplot(x=sample.Start_Lng,y=sample.Start_Lat)


# In[ ]:




