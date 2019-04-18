#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import pandas as pd
import requests
import json

# EIA developer API key
from config import api_key

# Build the endpoint URL
# http://api.eia.gov/series/?api_key=YOUR_API_KEY_HERE&series_id=PET.EMD_EPD2D_PTE_R10_DPG.A
url='https://api.eia.gov/series/?'
sid='PET.EMD_EPD2D_PTE_R10_DPG.W'
query_url = url + "api_key=" + api_key + "&series_id=" + sid


# In[2]:


# Run a request to endpoint and convert result to json
Fuel_data = requests.get(query_url).json()

# Print the json
#print(json.dumps(Fuel_data, indent=4, sort_keys=True))


# In[3]:


day=[]
rate=[]
day.append(Fuel_data["series"][0]["data"][0][0])
rate.append(Fuel_data["series"][0]["data"][0][1])
print(Fuel_data["series"][0]["data"][0][0])
print(Fuel_data["series"][0]["data"][0][1])


# In[4]:


d={
    "Date":day,
    "Price":rate
}
rate_df=pd.DataFrame(data=d)
#rate_df.head()


# In[5]:


rate_df.to_csv('rate.csv',index=False)

