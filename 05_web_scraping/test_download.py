#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install requests-html


# In[1]:


from requests_html import HTMLSession


# In[2]:


session = HTMLSession()


# In[3]:


resp = session.get("https://www.gutenberg.org/files/52484/52484-h/52484-h.htm")


# In[4]:


resp.html.links


# In[6]:


imgs = resp.html.find('img')


# In[7]:


len(imgs)


# In[15]:


type(imgs[0])


# In[25]:


imgs[0].attrs['src']


# In[27]:


imgs[0].base_url


# In[35]:


img = session.get(imgs[0].base_url + imgs[0].attrs['src'], stream=True)


# In[38]:


with open('img.png', 'wb') as out_file:
    shutil.copyfileobj(img.raw, out_file)
del img


# In[37]:


import shutil


# In[ ]:




