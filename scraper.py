# -*- coding: utf-8 -*-
"""
Created on Thu May 28 18:12:33 2020

@author: lance
"""
#https://www.liebertpub.com/toc/trgh/0/0

#import everything
import time
from flask import Flask
import selenium
from selenium import webdriver
from selenium.common import exceptions
import pandas as pd

import math
from math import pi
import requests
import bs4
from bs4 import BeautifulSoup as soup
import urllib.request
from urllib.request import urlopen as uReq
#get the web page
URL = 'https://pubmed.ncbi.nlm.nih.gov/?term=covid'
uClient = uReq(URL)
page_html = uClient.read()
uClient.close()
#make some soup and parse the page
page = soup(page_html, 'html.parser')
page_soup = soup(page_html, 'html.parser')
my_list = []
articles = page_soup.findAll("article", {"class":"labs-full-docsum"})
for article in articles:
    title = article.find("a", {"class": "labs-docsum-title"}).get_text()
    authors = article.find("span", {"class": "labs-docsum-authors full-authors"}).get_text()
    citation = article.find("span", {"class":"labs-docsum-journal-citation full-journal-citation"}).get_text()
    snippet = article.find("div", {"class": "full-view-snippet"}).get_text()
    permalink = article.find("input", {"class": "permalink-text"})["value"]
    Dict = {'Title': title, 'Authors': authors, 'Citation': citation, 'Snippet': snippet, 'Permalink': permalink}
    my_list.append(Dict)
#make an excel document
print(my_list)