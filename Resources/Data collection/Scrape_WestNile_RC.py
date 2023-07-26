# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 20:35:03 2023

@author: Ryan Cornelius
"""
#importing dependencies
from bs4 import BeautifulSoup
from splinter import Browser
from time import sleep 
from numpy import arange
import pandas as pd

#%%                            WestNyle Data Importing
#setting up the desired years using numpy
yearlist = arange(2001,2021,1)

#base website to grab data from, couldn't directly grab the table.
baseurl = 'https://www.cdc.gov/westnile/statsmaps/historic-data.html#tabs-2-2'
browser = Browser('chrome')
browser.visit(baseurl)
sleep(1)

#initializing empty vectors to store the data in. [county, year, infections]
counties = []
infections = []
years = []


for yr in yearlist:
    #setting up the desired xpath for the year selector [in the data by county section]
    #using a f-string to select the specific year, and then allowing for load time
    xpath = f'//div[@id="accordionTabs_2"]//section[@class="dashboard-filters-section"]//option[@value="{yr}"]'
    element = browser.find_by_xpath(xpath).first.click()
    sleep(1.5)

    #collecting and parsing the html for the data table, then collecting the data rows
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    container = soup.find("div",id="accordionTabs_2").find('section',class_='cdc-map-inner-container md').find('section',class_='data-table-container md')
    table = container.find('table',class_='data-table').find('tbody')
    rows = table.find_all('tr')
    
    #for each row, collected and append the desired data.
    for row in rows:
        data = row.find_all('td')
        county = data[0].text
        numInfections = data[2].text
        year = yr
        counties.append(county)
        infections.append(numInfections)
        years.append(year)

#format a Dataframe from the 3 data vectors and save out a RAW dataframe of the scrape.
DF = pd.DataFrame({'county':counties,'year':years,'infections':infections})
DF = DF.sort_values(['county','year'])
#DF.to_csv('Resources/Data/RawData/RAW_WestNile-Case-Counts-by-County-01-20.csv')


#Replace empty strings with 0. This does not account for non-reporting counties.
DF = DF.replace('', '0', regex=True)
DF['infections'] = DF['infections'].astype(int)

#groupby in order to get a dual-index dataframe, which can then by unstacked to produce columns for each year.
DF = DF.groupby(['year','county']).sum().unstack(level=0)

#save out the formatted dataframe. NaNs will be in place for non-reporting counties.
#DF.to_csv('Resources/Data/WestNile-Case-Counts-by-County-01-20.csv')


#%%             Geocoding county data

# Dependencies
import requests
import json
import pandas as pd
from numpy import arange


# importing DF csv
csvPath = 'Resources/Data/WestNile-Case-Counts-by-County-01-20.csv'

DF = pd.read_csv(csvPath, header='infer')





censusURL = 'https://api.census.gov/data/2010/dec/sf1?get=NAME&for=county:*&in=state:*'
geoapifyBaseURL = 'https://api.geoapify.com/v1/geocode/search?text='
geoapifyApiKey = '5f3e3b9c92f0408cae7e05687fdf496c'

text = 'https://api.geoapify.com/v1/geocode/search?text=MN,Renville&bias=countrycode:us&format=json&apiKey=5f3e3b9c92f0408cae7e05687fdf496c'

countyCodes = requests.get(censusURL).json()
countyCodesDF = pd.DataFrame(countyCodes)
countyCodesDF = countyCodesDF.rename(columns=countyCodesDF.iloc[0]).loc[1:]


latVector = []
lonVector = []
comboCodeVector = []

for i in arange(0,len(DF.index),1):
    countySearch = DF['county'].iloc[i]
    county = countySearch[4:]
    geoapifyQuery = f'{geoapifyBaseURL}{countySearch}%20county&filter=countrycode:us&format=json&apiKey={geoapifyApiKey}'
    countyData = requests.get(geoapifyQuery).json()
    lat = countyData['results'][0]['lat']
    lon = countyData['results'][0]['lon']
    countyResult = countyData['results'][0]['county']
    stateResult = countyData['results'][0]['state']
    #regString = f'{countyResult}, {stateResult}'
    if county in countyResult:
        countyDFResult = countyCodesDF.loc[countyCodesDF['NAME'].str.contains(countyResult) 
                                           & countyCodesDF['NAME'].str.contains(stateResult)]
        try:
            stateCode = countyDFResult['state'].iloc[0]
            countyCode = countyDFResult['county'].iloc[0]
            comboCode = stateCode + countyCode
            
            print(f'search {county} county, \nresult: {countyResult}, {stateResult}, FIPS: {comboCode}')
            print(f'lat: {lat}, lon: {lon}')
        except: 
            print(f'error encountered for county {county}')
            print('please enter data manually')
            lat = input('enter lat')
            lon = input('enter lon')
            comboCode = input('enter FIPS comboCode')
            print(f'{county} entered manually. continuing.')
    else:
        print(f'{countyResult} does not match {county}')
        print('please enter data manually')
        lat = input('enter lat')
        lon = input('enter lon')
        comboCode = input('enter FIPS comboCode')
        print(f'{county} entered manually. continuing.')

    latVector.append(lat)
    lonVector.append(lon)
    comboCodeVector.append(comboCode)
    

#%%  Data cleaning and merging


from bs4 import BeautifulSoup
from splinter import Browser
from time import sleep 
from numpy import arange
import pandas as pd
import re


# import/export DataFrame csv
csvPath = 'Resources/Data/RawData/WestNile-Case-Counts-by-County-01-20.csv'
savePath = 'Resources/Data/Clean_WestNile-Case-Counts-by-County-01-20.csv'

#URL of the counties list with FIPs codes and coordinates
url = 'https://en.wikipedia.org/wiki/User:Michael_J/County_table'

#Using a splinter instance to grab the FIPs table above
browser = Browser('chrome')
browser.visit(url)

#giving page time to load and then scraping the html
sleep(2)
html_scraped = browser.html
browser.quit()

#pd.read_html() parses for tables and returns a list of dataframes.
WebDFs = pd.read_html(html_scraped)
        
#The webpage should only have one table, grabbing the first table. 
WebDFs = WebDFs[0]


#grab the data to be cleaned 
dataDF = pd.read_csv(csvPath, header='infer')

#reduce the dataset to continental US
dataDF = dataDF.loc[dataDF['county'].str[0:2] != 'PR' ]
dataDF = dataDF.loc[dataDF['county'].str[0:2] != 'AK' ]
dataDF = dataDF.loc[dataDF['county'].str[0:2] != 'HI' ]
dataDF = dataDF.loc[dataDF['county'].str[0:2] != 'Pr' ]
dataDF = dataDF.loc[dataDF['county'].str[0:2] != 'Ak' ]
dataDF = dataDF.loc[dataDF['county'].str[0:2] != 'Hi' ]

#set up empty vectors for the information I want. 
latVector = []
lonVector = []
FIPScodeVector = []
#tracking errors/replacements by creating a list of dictionaries. 
ErrorList = []
ErrorDict = {}

#loop over all dataframe rows
for i in arange(0,len(dataDF.index),1):
    #grab the county/state and seperate out the county and state
    countySearch = dataDF['county'].iloc[i]
    county = countySearch[4:]
    state = countySearch[:2]
    
    #account for some common discrepencies between the source data and the FIPS data
    county = county.replace(' Parish','')
    county = county.replace(' County','')
    county = county.replace('St ','St. ')
    county = county.replace(' City','')
    county = county.replace(' Borough','')

    
    #account for some specific discrepencies
    if state == 'DC':
        county = 'District of Columbia'
    if county == 'Baltimore City':
        county = 'Baltimore'
    if county == 'St. Louis City':
        county = 'St. Louis'            
    if county == 'O Brien':
        county = 'Brien' 
    if county == 'Colonial Heights Cit':
        county = 'Colonial Heights'   

    #check for a match between the county name in the data and in the FIPS data
    countyDFResult = WebDFs.loc[WebDFs['County [2]'].str.contains(county, case=False) 
                                       & WebDFs['State'].str.contains(state, case=False)]
    
    #use try to catch if no match was found
    try:
        #grab the values from the FIPS data
        FIPScode = str(countyDFResult['FIPS'].iloc[0])
        if len(FIPScode) == 4:
            FIPScode = '0' + FIPScode
        lat = countyDFResult['Latitude'].iloc[0]
        lon = countyDFResult['Longitude'].iloc[0]
    #if the match dataframe is empty, do the same, but matching only a partial match 
    except: 
        print(f'no matching county for {countySearch}... trying based on last 4 characters...\n')
        
        try:

            countyDFResult = WebDFs.loc[WebDFs['County [2]'].astype(str).str
                                        .contains(county[len(county)-4:len(county)-1], case=False) 
                                        & WebDFs['State'].str.contains(state, case=False)] 
            FIPScode = str(countyDFResult['FIPS'].iloc[0])
            if len(FIPScode) == 4:
                FIPScode = '0' + FIPScode
            countyMatch = countyDFResult['County [2]'].iloc[0]
            lat = countyDFResult['Latitude'].iloc[0]
            lon = countyDFResult['Longitude'].iloc[0]
            print(f'{countySearch} result: county {countyMatch}, FIPS {FIPScode}, Lat {lat}, Lon {lon}')
            
        except:
            print(f'no matching county for {countySearch}\n')
            print(f'using {url}')
            dataindex = input('enter the index of the data manually:   ')
        
            countyDFResult = WebDFs.loc[WebDFs['Sort [1]'].astype(str).str.fullmatch(dataindex) ]
        
            FIPScode = str(countyDFResult['FIPS'].iloc[0])
            if len(FIPScode) == 4:
                FIPScode = '0' + FIPScode
                
            countyMatch = countyDFResult['County [2]'].iloc[0]
            lat = countyDFResult['Latitude'].iloc[0]
            lon = countyDFResult['Longitude'].iloc[0]
            print(f'{countySearch} result: county {countyMatch}, FIPS {FIPScode}, Lat {lat}, Lon {lon}')
        ErrorDict = {countySearch : countyMatch}
        ErrorList.append(ErrorDict)
    lat = float(re.search('\d+.\d+',lat)[0])
    lon = -float(re.search('\d+.\d+',lon)[0])
    
    latVector.append(lat)
    lonVector.append(lon)
    FIPScodeVector.append(FIPScode)

dataDF['lat'] = latVector
dataDF['lon'] = lonVector
dataDF['FIPS'] = FIPScodeVector

dataDF.to_csv(savePath)



#%%           Lymes Disease Cleaning and Merging


from bs4 import BeautifulSoup
from splinter import Browser
from time import sleep 
from numpy import arange
import pandas as pd
import re


# import/export DataFrame csv
csvPath = 'Resources/Data/RawData/RAW_Ld-Case-Counts-by-County-01-20.csv'
savePath = 'Resources/Data/Clean_Ld-Case-Counts-by-County-01-20.csv'

#URL of the counties list with FIPs codes and coordinates
url = 'https://en.wikipedia.org/wiki/User:Michael_J/County_table'

#Using a splinter instance to grab the FIPs table above
browser = Browser('chrome')
browser.visit(url)

#giving page time to load and then scraping the html
sleep(2)
html_scraped = browser.html
browser.quit()

#pd.read_html() parses for tables and returns a list of dataframes.
WebDFs = pd.read_html(html_scraped)
        
#The webpage should only have one table, grabbing the first table. 
WebDFs = WebDFs[0]


WebDFs['FIPS'] = WebDFs['FIPS'].astype(str).str.zfill(5)


#grab the data to be cleaned 
dataDF = pd.read_csv(csvPath, header='infer')



#reduce the dataset to continental US
dataDF = dataDF.loc[dataDF['state'] != 'Alaska' ]
dataDF = dataDF.loc[dataDF['state'] != 'Hawaii' ]

#set up empty vectors for the information I want. 
latVector = []
lonVector = []
FIPScodeVector = []
#tracking errors/replacements by creating a list of dictionaries. 
ErrorList = []
ErrorDict = {}

#loop over all dataframe rows
for i in arange(0,len(dataDF.index),1):
    countySearch = dataDF['county'].iloc[i]
    stateCode = str(dataDF['stcode'].iloc[i])
    
    if len(stateCode) == 1:
        stateCode = '0'+stateCode
        
    countyCode = str(dataDF['ctycode'].iloc[i])
    while len(countyCode) !=3:
        countyCode = '0'+countyCode

    FIPScode = stateCode+countyCode
    
    #check for a match between the county name in the data and in the FIPS data
    countyDFResult = WebDFs.loc[WebDFs['FIPS'].str.contains(FIPScode, case=False)]
    
    #use try to catch if no match was found
    try:
        #grab the values from the FIPS data
        lat = countyDFResult['Latitude'].iloc[0]
        lon = countyDFResult['Longitude'].iloc[0]
    #if the match dataframe is empty, do the same, but matching only a partial match 
    except: 
        print(f'no matching county for {countySearch}, FIPS code {FIPScode}\n')
        ErrorDict = {countySearch : FIPScode}
        ErrorList.append(ErrorDict)
    lat = float(re.search('\d+.\d+',lat)[0])
    lon = -float(re.search('\d+.\d+',lon)[0])
    
    latVector.append(lat)
    lonVector.append(lon)
    FIPScodeVector.append(FIPScode)

dataDF['lat'] = latVector
dataDF['lon'] = lonVector
dataDF['FIPS'] = FIPScodeVector

dataDF.to_csv(savePath)
