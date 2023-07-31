from bs4 import BeautifulSoup
import pandas as pd
import os
from time import sleep
from splinter import Browser

# Send any loop iterations with error to an exceptions list:
exceptions = []

#set up dataframe to contain scraped data
county_precipitation_df = pd.DataFrame()

#set first and final year to scrape data for
init_year = 2001
final_year = 2021

#initialize loop to scrape webpages for desired years
for i in range(init_year, final_year + 1): 
    try:
        print(f'Getting Precipitation data table for the year: {i}.')

        ### OJO: method one was to use BeautifulSoup, but this seemed to fail because the webpage loaded HTML too slowly
        ### however, this might work on a faster connection/computer
        #res = requests.get(url)
        #webpage = res.content
        #html_soup_object = BeautifulSoup(webpage, 'html.parser')

        #use Browser from splinter to automate opening the webpage: 

        
        #set the url using this iteration (i) for the year, data will be scraped for average [or total?] precipitation
        #across a 3 month window ending in September (i.e. July, August, September)
        url = f"https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/county/mapping/110/pcp/{i}09/3/value"
        #https://splinter.readthedocs.io/en/latest/drivers/chrome.html
        #from selenium.webdriver.chrome.service import Service
        #my_service = Service(executable_path ='C:\Windows\chromedriver.exe')
        #open browser and save as an object for python to manipulate, first by directing it to the webpage
        #browser = Browser('chrome', service = my_service)
        browser = Browser('chrome')
        browser.visit(url)
        
        #the page loads slowly, so give it time to load fully before copying the html and closing the browser
        sleep(2)
        html_scraped = browser.html
        browser.quit()
       
        #pd.read_html() parses for tables and returns a list of dataframes.
        dfs = pd.read_html(html_scraped)
        
        #The webpage should only have one table
        df = dfs[0]

        #Add a year column and populate with this iteration
        df['Year'] = i

        #Now concatenate this iteration's dfs[0] with the county temperature dataframe that will contain all years temp
        county_precipitation_df = pd.concat([county_precipitation_df, df], ignore_index=True, axis=0)
        print(f'{i} DataFrame concatenated to the County Precipitation Dataframe.')

    except ValueError:  # the except statement sends value errors to a list that can be exported after the loop is finished.
        exceptions.append(url)
        print('There was at least one error during web scrape loop')

    else:
        pass

#check what urls failed
print(exceptions)

#Clean up data column names and format of data
column_names = {
    "County" : "County_ST",
    "Value" : "Precipitation (in)",
}
county_precipitation_df.rename(columns=column_names, inplace=True)
county_precipitation_df[["County", "State Abbreviation"]] = county_precipitation_df["County_ST"].str.split(", ", 1, expand=True)
county_precipitation_df["Precipitation (in)"] = county_precipitation_df["Precipitation (in)"].str.replace("\"", "")

#We only really need five of the columns
county_precipitation_df = county_precipitation_df[["County", "State", "State Abbreviation", "Precipitation (in)", "Year"]]

#Write dataframe out to a csv file
county_precipitation_df.to_csv("../Data/RawData/county_avg_precipitation.csv", index=False)
#-----------------------------------------------------------------------------------------------------------------------


