#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Set up dashboard
import pandas as pd #for data wrangling
import streamlit as st #base streamlit library
from pandasql import sqldf #sql for pandas dataframe, for ease
import plotly.express as px #for charting
#Read csv into dataframe
df = pd.read_csv('data.csv')
#Converting timestamp to date
df['Timestamp'] = pd.to_datetime(df['Timestamp']).dt.date
#declaring psql globals
psql = lambda q: sqldf(q,globals())
#Aggregating dataset
dfHisto = psql('''
select
    ...
,   ...
,   ...
from df
group by Timestamp, Type
''')
#Getting a plotly histogram of dataset
fig = px.bar(variable, x='Timestamp', y='count', color='Type', text_auto=True)
fig.update_traces(textfont_size=6,textangle=0, textposition="outside", cliponaxis=False)
#display chart on frontend
st.title(' ... Dashboard')
st.plotly_chart(fig)


# In[ ]:




