#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import packages, push data to Github for control
from github import Github
import datetime
token = "<your_github_token>"
g = Github(token)
user = g.get_user()
repo = g.get_repo("<github_username>/<your_repository_name>")
ct = str(datetime.datetime.now())
commit_msg = "AWS EC2 Auto Commit -" + ct
data = open("data.csv", "r")
data_read = data.read()
git_data = repo.get_contents("data.csv")
repo.update_file(git_data.path, commit_msg, data_read, git_data.sha)


# In[ ]:




