#!/usr/bin/env python
# coding: utf-8

# In[22]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as stats
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import statsmodels.formula.api as smf
import math
plt.rcParams["figure.figsize"] = [15, 10]


# In[2]:


crashes=pd.read_csv('NYPD_Motor_Vehicle_Collisions_-_Crashes_in_2018.csv')


# In[3]:


crashes.head(300)


# In[4]:


crashes.describe()


# In[5]:


crashes.info()


# In[6]:


crashes['TIME OF ACCIDENT']=pd.to_datetime(crashes['TIME'])
crashes.head()


#  There exist empty columns in my dataset like BOROUGH, ZIP CODE, LATITUDE, LOCATION. However, What call the attention about the missing data is that BOROUGH and ZIP CODE are missing  35 percent of its data. Another large percent of missing date is at columns  ON STREET NAME where the approximately 24 percent of its data is missing.  

# In[7]:


zipcodes=crashes['BOROUGH'].value_counts()


# In[23]:


zipcodes.plot.bar()
plt.title('Number of accident  by borough')
plt.ylabel('Borough')
plt.xlabel('Number of accident')
plt.show()
plt.savefig('C:/Users/789/Desktop/figure.pdf')


# In[24]:


bronx_filter=crashes['BOROUGH']=='BRONX'
bronx=crashes[bronx_filter]
bronx['ZIP CODE'].value_counts().plot.bar()
plt.title('Accident by zip code in the Bronx')
plt.xlabel('Zip code')
plt.ylabel('Number of accidents')


# In[25]:


manha_filter=crashes['BOROUGH']=='MANHATTAN'
manha=crashes[manha_filter]
zip_code_manha=manha['ZIP CODE'].value_counts()
zip_code_manha.head(25).plot.bar()
 
plt.title('Accident by zip code in Manhattan ')
plt.xlabel('Zip code')
plt.ylabel('Number of accidents')


# In[26]:


brook_filter=crashes['BOROUGH']=='BROOKLYN'
brook=crashes[brook_filter]
zip_code_brook=brook['ZIP CODE'].value_counts()
zip_code_brook.plot.bar()
plt.title('Accident by zip code in Brooklyn ')
plt.xlabel('Zip code')
plt.ylabel('Number of accidents')


# In[27]:


que_filter=crashes['BOROUGH']=='QUEENS'
que=crashes[que_filter]
zip_code_que=que['ZIP CODE'].value_counts()
zip_code_que.plot.bar()
plt.title('Accident by zip code in Queens ')
plt.xlabel('Zip code')
plt.ylabel('Number of accidents')


# In[28]:


state_filter=crashes['BOROUGH']=='STATEN ISLAND'
state=crashes[state_filter]
zip_code_state=state['ZIP CODE'].value_counts()
zip_code_state.plot.bar()
plt.title('Accident by zip code in Staten Island ')
plt.xlabel('Zip code')
plt.ylabel('Number of accidents')


# In[29]:


crashes_by_hour=crashes.groupby(crashes['TIME OF ACCIDENT'].dt.hour)
crashes_by_hour.head()


# In[ ]:





# In[30]:


values=crashes_by_hour['NUMBER OF PERSONS INJURED']
values.mean() 


# In[31]:


values.sum().plot.bar()
plt.title('Injuries in traffic accidents by hours in NYC ')
plt.xlabel('Hours')
plt.ylabel('Injureies')


# In[32]:


crashes_by_hour['NUMBER OF PERSONS KILLED'].sum().plot.bar()
plt.title(' Death in road accidents by hours in NYC ')
plt.xlabel('Hours')
plt.ylabel('Number of deaths')


# In[33]:


crashes['NUMBER OF PERSONS KILLED'].sum()


# In[34]:


s=crashes.groupby(['ZIP CODE',crashes['TIME OF ACCIDENT'].dt.hour])


# In[35]:


s.size()


# In[36]:


w.plot.hist()


# In[ ]:





# In[ ]:




