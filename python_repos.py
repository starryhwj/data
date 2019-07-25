# -*- coding: utf-8 -*-
# filename: python_repos.py

import requests
import pygal

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print ("Status code:", r.status_code)

response_dict = r.json()

print ('total repositories:', response_dict['total_count'])

repo_dicts = response_dict['items']

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

chart = pygal.Bar(x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')
