#!/usr/bin/env python
# coding: utf-8

# In[18]:


# Dependencies
import pandas as pd
import numpy as np
import requests
import json

# EIA developer API key
from config import api_key

# Build the endpoint URL
# http://api.eia.gov/series/?api_key=YOUR_API_KEY_HERE&series_id=PET.EMD_EPD2D_PTE_R10_DPG.A
url='https://api.eia.gov/series/?'
sid='PET.EMD_EPD2D_PTE_R10_DPG.W'
query_url = url + "api_key=" + api_key + "&series_id=" + sid


# In[19]:


# Run a request to endpoint and convert result to json
Fuel_data = requests.get(query_url).json()

# Print the json
# print(json.dumps(Fuel_data, indent=4, sort_keys=True))


# In[20]:


# PADD 1B CENTRAL ATLANTIC
sid='PET.EMD_EPD2D_PTE_R1Y_DPG.W'
Padd1b_url = url + "api_key=" + api_key + "&series_id=" + sid


# In[21]:


# Run a request to endpoint and convert result to json
padd1b_data = requests.get(Padd1b_url).json()

# Print the json
# print(json.dumps(padd1b_data, indent=4, sort_keys=True))


# In[22]:


day=[]
rate1=[]
rate1b=[]
day.append(Fuel_data["series"][0]["data"][0][0])
rate1.append(Fuel_data["series"][0]["data"][0][1])
rate1b.append(padd1b_data["series"][0]["data"][0][1])
print(Fuel_data["series"][0]["data"][0][0])
print(Fuel_data["series"][0]["data"][0][1])
print(padd1b_data["series"][0]["data"][0][1])


# In[23]:


d={
    "Date":day,
    "PADD_1":rate1,
    "PADD_1B":rate1b
}
rate_df=pd.DataFrame(data=d)
rate_df.head()


# In[24]:


rate_df.to_csv(f'diesel-rate-{day[0]}.csv',index=False)

