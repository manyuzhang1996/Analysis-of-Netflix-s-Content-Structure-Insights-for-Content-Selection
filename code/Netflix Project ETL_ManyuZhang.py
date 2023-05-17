#!/usr/bin/env python
# coding: utf-8

# ## 1. Clean the Netflix data

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


netflix = pd.read_csv('https://raw.githubusercontent.com/manyuzhang1996/DATA220-Assignment/main/' +
                      'NetflixContent.csv')


# In[3]:


netflix.head(5)


# #### 1.1 keep the first director in column 'director'

# In[4]:


def cut(char):
    i = 0
    while char[i] != ',':
        i += 1
    return char[:i]


# In[5]:


for i in range(len(netflix['director'])):
    if netflix['director'][i] != None:
        try:
            new_director = cut(netflix['director'][i])
            netflix.at[i, 'director'] = new_director
        except:
            pass


# In[6]:


netflix_director = netflix[['show_id', 'director']]


# In[7]:


netflix_director.to_csv('Netflix_director.csv', index=False)


# #### 1.2 Group rating in different audience groups

# In[8]:


netflix['new_rating'] = [None]*len(netflix['rating'])


# In[9]:


for i in range(len(netflix['rating'])):
    if netflix['rating'][i] in ['TV-Y', 'TV-Y7', 'TV-Y7-FY', 'G', 'TV-G', 'PG', 'TV-PG']:
        netflix.at[i, 'new_rating'] = 'kids'
    elif netflix['rating'][i] in ['TV-14', 'PG-13']:
        netflix.at[i, 'new_rating'] = 'teens'
    else:
        netflix.at[i, 'new_rating'] = 'adults'


# In[10]:


netflix_new_rating = netflix[['show_id', 'new_rating']]


# In[11]:


netflix_new_rating.to_csv('Netflix_new_rating.csv', index=False)


# ## 2. Clean the Rotton Tomato data

# In[12]:


tomato = pd.read_csv('rotten_tomatoes_movies.csv')


# In[13]:


tomato.head(5)


# #### 1.1 keep the first director in column 'director'

# In[14]:


for i in range(len(tomato['directors'])):
    if tomato['directors'][i] != None:
        try:
            new_director = cut(tomato['directors'][i])
            tomato.at[i, 'directors'] = new_director
        except:
            pass


# In[15]:


tomato_director = tomato[['rotten_tomatoes_link', 'directors']]


# In[16]:


tomato_director.to_csv('Tomato_director.csv', index=False)


# #### 1.2 Group rating in different audience groups

# In[17]:


tomato['new_content_rating'] = [None]*len(tomato['content_rating'])


# In[18]:


for i in range(len(tomato['content_rating'])):
    if tomato['content_rating'][i] in ['PG', 'G']:
        tomato.at[i, 'new_content_rating'] = 'kids'
    elif tomato['content_rating'][i] in ['PG-13']:
        tomato.at[i, 'new_content_rating'] = 'teens'
    elif tomato['content_rating'][i] in ['R', 'NC17']:
        tomato.at[i, 'new_content_rating'] = 'adults'
    else:
        tomato.at[i, 'new_content_rating'] = 'unrated'


# In[19]:


tomato_new_content_rating = tomato[['rotten_tomatoes_link', 'new_content_rating']]


# In[20]:


tomato_new_content_rating.to_csv('Tomato_new_content_rating.csv', index=False)


# ## 3. Clean the IMDb data

# In[21]:


imdb = pd.read_csv('IMDb_All_Genres_etf_clean1.csv')


# In[22]:


imdb.head(10)


# #### keep the first director in column 'director'

# In[23]:


def imdbcut(char):
    i, j = 0, 10
    while char[i] != ',':
        i += 1
    return char[10:i]


# In[24]:


for i in range(len(imdb['Director'])):
    if imdb['Director'][i][:10] == 'Directors:':
        try:
            new_director = imdbcut(imdb['Director'][i])
            imdb.at[i, 'Director'] = new_director
        except:
            pass


# In[25]:


imdb.head(10)


# In[26]:


imdb_director = imdb[['Movie_Title', 'Director']]


# In[27]:


imdb_director.to_csv('IMDB_director.csv', index=False)


# #### 1.2 Group rating in different audience groups

# In[28]:


imdb['new_censor'] = [None]*len(imdb['Censor'])


# In[29]:


for i in range(len(imdb['Censor'])):
    if imdb['Censor'][i] in ['U', 'G', 'PG', '7', 'UA 7+', 'All', 'M/PG', 'UA', 'U/A']:
        imdb.at[i, 'new_censor'] = 'kids'
    elif imdb['Censor'][i] in ['PG-13', '16', '13', 'UA 16+', '15+', 'UA 13+', '12+', '12']:
        imdb.at[i, 'new_censor'] = 'teens'
    elif imdb['Censor'][i] in ['A', 'R', '18', '(Banned)', '18+', 'NC-17']:
        imdb.at[i, 'new_censor'] = 'adults'
    else:
        imdb.at[i, 'new_censor'] = 'unrated'


# In[30]:


imdb_new_censor = imdb[['Movie_Title', 'new_censor']]


# In[31]:


imdb_new_censor.to_csv('IMDB_new_censor.csv', index=False)

(END)