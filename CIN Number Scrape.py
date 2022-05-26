#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scrapy
import time
import pandas as pd
from scrapy.crawler import CrawlerProcess
import numpy as np


# In[2]:


links = []
for i in range(1,13334):
    links.append('https://www.zaubacorp.com/company-list/p-{}-company.html'.format(i))

cins=[]
names=[]
area=[]
status=[]
all_data=[]


# In[3]:


class CINsScrape(scrapy.Spider):
    name='CIN_scraper'
    
    def start_requests(self):
        for link in links:
            print(link)
            yield scrapy.Request(url=link,callback=self.get_cin)
        
    def get_cin(self,response):
        data = response.xpath('//td//a/@href').extract()
        for i in data:
            all_data.append(i)


# In[4]:


process= CrawlerProcess()
process.crawl(CINsScrape)
process.start()


# In[7]:


try1=[]
for i in all_data:
    try:
        try1.append(i.replace('https://www.zaubacorp.com/company/',''))
    except:
        print(i)


# In[13]:


names_c=[]
cin_c=[]
for i in try1:
    a=(i.split('/'))
    names_c.append(a[0])
    cin_c.append(a[1])
dic= {'Name':names_c,'CIN':cin_c}
corrected = pd.DataFrame(dic)
print(corrected.head())
corrected.to_excel('corrected_cin.xlsx')

