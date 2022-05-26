#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')
import time
# importing webdriver from selenium
from selenium.webdriver.support.expected_conditions import staleness_of

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import selenium.webdriver.support.select

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


# In[2]:


get_ipython().system('pip install html-table-parser-python3')


# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


import urllib.request

# pretty-print python data structures
from pprint import pprint

# for parsing all the tables present 
# on the website
from html_table_parser.parser import HTMLTableParser

# for converting the parsed data in a
# pandas dataframe
#print(driver.current_url)


# In[5]:


def url_get_contents(url):
 
    # Opens a website and read its
    # binary contents (HTTP Response Body)
 
    #making request to the website
    req = urllib.request.Request(url=url)
    try:
      f = urllib.request.urlopen(req)
      return f.read()
    except:
      return ""


# In[6]:


n=0


# In[9]:


driver=webdriver.Chrome()
driver.get('https://drt.etribunals.gov.in/front/drt_case_status.php')
m=0
drt=driver.find_element_by_id("schemaname")
drt_select=Select(drt)
options = [x for x in drt.find_elements_by_tag_name("option")]

for element in options:
     
    if m<=29:
        m=m+1
        pass
    else:
        #driver.implicitly_wait(15)
        drt_select.select_by_value(element.get_attribute("value")) 
#drt_select.select_by_value("102")
        
        case=driver.find_element_by_id("case_type")
        case_select=Select(case)
        case_select.select_by_value("7")
            #case_no=driver.find_element_by_id('cno')
            
        for i in range(2018,2022):
            year=driver.find_element_by_id('case_year')
            year.clear()
            year.send_keys(i)
            
            k=0
                
                #year=driver.find_element_by_id('case_year')
                
            for j in range(1,10000):
                case_no=driver.find_element_by_id('cno')
                case_no.clear()
                case_no.send_keys(j)
                    #driver.implicitly_wait(10)


                driver.find_element_by_id("submit1").click()
                time.sleep(1)

                main_window_handle = None
                while not main_window_handle:
                    main_window_handle = driver.current_window_handle

                try:
                    
                    driver.find_element(By.XPATH,"//a[text()='MORE DETAIL']").click()
                        #driver.implicitly_wait(10)
                    signin_window_handle = None
                    while not signin_window_handle:
                        for handle in driver.window_handles:
                            if handle != main_window_handle:
                                signin_window_handle = handle
                                break
                    driver.switch_to.window(signin_window_handle)
                
                        
                    
                    n=n+1
                    if n==1:
                        k=0
                        xhtml=url_get_contents(driver.current_url).decode('utf-8')
                        p = HTMLTableParser()
                        p.feed(xhtml)
                        l = driver.find_elements_by_xpath ("//*[@class= 'table table-bordered']/tbody/tr")
#num_cols = len (driver.find_elements_by_xpath("//*[@class='table table-bordered table-extra-condensed']/tbody/tr[2]/td"))
#print(driver.current_url)
                        ct=0
                        example_list=[]
                        for lines in l:
                            #print (i.text)
                            if ct==1 or ct==3 or ct==6:
                                example_list.append(lines.text)
                            ct=ct+1
                    
                        ex_df=pd.DataFrame(example_list)
                        ex_df=ex_df.transpose()
                        
                        
                        l2 = driver.find_elements_by_xpath ("//*[@class='table table-striped']/tbody/tr")
#num_cols = len (driver.find_elements_by_xpath("//*[@class='table table-bordered table-extra-condensed']/tbody/tr[2]/td"))
#print(driver.current_url)
                        ct2=0
                        example_list2=[]
                        for lines in l2:
    
                            #print (i.text)
                            if ct2>1:
                                example_list2.append(lines.text)
                            ct2=ct2+1
                        
                        ex2_df=pd.DataFrame(example_list2)
                        ex2_df=ex2_df.transpose()
                        
                        
                        
                        sample_df=pd.DataFrame(p.tables[0])
                        sample_df=sample_df.transpose()
                        sample_df['Petitioner']=ex_df.iloc[0][0].replace('\n', ' ')
                        sample_df['Respondent']=ex_df.iloc[0][1].replace('\n', ' ')
                        sample_df['Court']=ex_df.iloc[0][2].replace('\n', ' ')
                        
                        try:
                            sample_df['Property Type Detail Of Property']=ex2_df.iloc[0][0].replace('\n', ' ')
                        except:
                            pass
                        
                        driver.close()

                #Switch back to the old tab or window
                        driver.switch_to.window(main_window_handle)
                        temp_drt=driver.find_element_by_id("schemaname")
                        temp_drt_select=Select(temp_drt)
                        selected_option = temp_drt_select.first_selected_option
                        sample_df['Tribunal']=selected_option.text
                        #print (selected_option.text)
                        
                        
                    else:
                        k=0
                        xhtml=url_get_contents(driver.current_url).decode('utf-8')
                        p = HTMLTableParser()
                        p.feed(xhtml)
                        l = driver.find_elements_by_xpath ("//*[@class= 'table table-bordered']/tbody/tr")
#num_cols = len (driver.find_elements_by_xpath("//*[@class='table table-bordered table-extra-condensed']/tbody/tr[2]/td"))
#print(driver.current_url)
                        ct=0
                        example_list=[]
                        for i in l:
                            #print (i.text)
                            if ct==1 or ct==3 or ct==6:
                                example_list.append(i.text)
                            ct=ct+1
                    
                        ex_df=pd.DataFrame(example_list)
                        ex_df=ex_df.transpose()
                        
                        
                        l2 = driver.find_elements_by_xpath ("//*[@class='table table-striped']/tbody/tr")
#num_cols = len (driver.find_elements_by_xpath("//*[@class='table table-bordered table-extra-condensed']/tbody/tr[2]/td"))
#print(driver.current_url)

                        ct2=0
                        example_list2=[]
                        for lines in l2:
    
                            #print (i.text)
                            if ct2>1:
                                example_list2.append(lines.text)
                            ct2=ct2+1
                        
                        ex2_df=pd.DataFrame(example_list2)
                        ex2_df=ex2_df.transpose()
                        
                        
                        sample2_df=pd.DataFrame(p.tables[0])
                        sample2_df=sample2_df.transpose()
                        sample2_df['Petitioner']=ex_df.iloc[0][0].replace('\n', ' ')
                        sample2_df['Respondent']=ex_df.iloc[0][1].replace('\n', ' ')
                        sample2_df['Court']=ex_df.iloc[0][2].replace('\n', ' ')
                        
                        try:
                            sample2_df['Property Type Detail Of Property']=ex2_df.iloc[0][0].replace('\n', ' ')
                        except:
                            pass
                        
                        driver.close()
                        driver.switch_to.window(main_window_handle)
                        temp_drt=driver.find_element_by_id("schemaname")
                        temp_drt_select=Select(temp_drt)
                        selected_option = temp_drt_select.first_selected_option
                        sample2_df['Tribunal']=selected_option.text
                        #print (selected_option.text)  
                        
                        sample2_df=sample2_df.drop([0, 0])
                        sample_df = pd.concat([sample_df, sample2_df], ignore_index=True)
                        
                    
                
                    #driver.close()

                #Switch back to the old tab or window
                    #driver.switch_to.window(main_window_handle)
                    #temp_drt=driver.find_element_by_id("schemaname")
                    #temp_drt_select=Select(temp_drt)
                    #selected_option = temp_drt_select.first_selected_option
                    #print (selected_option.text)    
            
                except:
                    k=k+1
                    if k>30:
                        break
                    else:
                        pass
                    #break
                    
  
                
                


# In[10]:


sample_df.head(5000)
len(sample_df)


# In[11]:


sample_df.to_excel('drt_data_29.xlsx')

