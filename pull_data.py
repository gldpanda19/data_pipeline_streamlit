#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import packages and create connection to database; sensitive information redacted
import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote
db = create_engine("FLAVORsql+psycopg2://<db_username>:%s<your_db_address>/<your_database_name>" % quote('<db_password>'))
query = '''
SELECT ... FROM ...
'''
df = pd.read_sql(query,db)
df.to_csv('data.csv', index = False)


# In[ ]:




