# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 20:35:03 2023

@author: RyanD
"""

from bs4 import BeautifulSoup
from splinter import Browser
from time import sleep 
from numpy import arange
import pandas as pd

yearlist = arange(2001,2021,1)

baseurl = 'https://www.cdc.gov/westnile/statsmaps/historic-data.html#tabs-2-2'
browser = Browser('chrome')
browser.visit(baseurl)
sleep(3)


counties = []
infections = []
years = []

for yr in yearlist:
    xpath = f'//div[@id="accordionTabs_2"]//section[@class="dashboard-filters-section"]//option[@value="{yr}"]'
    element = browser.find_by_xpath(xpath).first.click()
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    container = soup.find("div",id="accordionTabs_2").find('section',class_='cdc-map-inner-container md').find('section',class_='data-table-container md')
    table = container.find('table',class_='data-table').find('tbody')
    rows = table.find_all('tr')
    for row in rows:
        data = row.find_all('td')
        county = data[0].text
        numInfections = data[2].text
        year = yr
        counties.append(county)
        infections.append(numInfections)
        years.append(year)

DF = pd.DataFrame({'county':counties,'year':years,'infections':infections})
DF = DF.sort_values(['county','year'])

DF = DF.replace('', '0', regex=True)
DF['infections'] = DF['infections'].astype(int)


DF = DF.groupby(['year','county']).sum().unstack(level=0)

DF.to_csv('Resources/Data/WestNile-Case-Counts-by-County-01-20.csv')

