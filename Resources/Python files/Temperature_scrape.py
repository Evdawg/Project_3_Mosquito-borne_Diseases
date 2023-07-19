from bs4 import BeautifulSoup
import requests
import pandas as pd
from python_to_postgres import python_df_to_postgres
import os
import sqlalchemy
from sqlalchemy import create_engine, URL, text
from sqlalchemy.orm import sessionmaker
import config_file
import psycopg2

### TODO: Rewrite this code for Temperature and Precipitation web scrape of https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/county/mapping/110/...

# Send any loop iterations with error to an exceptions list:
exceptions = []

### I dunno if this stackoverflow post helps but I referenced it at one point. I think it's using dictionaries in the loop somehow...
### See https://stackoverflow.com/questions/68607106/creating-multiple-dataframes-using-for-loop-with-pandas for example of storing the dataframes in a dictionary.
# Need to be able to concat scraped table data to the correct DataFrame within the webpage loop.
# dynamic variables is bad practice, so for now just type out each dataframe variable for each position:

### Webpage schema is:
    ### https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/county/mapping/110/tavg/200109/3/value
    #TODO: break this out into base URL and then loop through the changing "200109" values for just year, because
    # the date will always be 3 month centered around August, so 09 for September as the last month.
    ### example)
            # root = https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/county/mapping/110/tavg/'
            # url_end_piece = '09/3/value'
            # year = 2001 # then add 1 to this value within the loop
            # url = root + year + url_end_piece
            # print(f'Getting Temperature data table for the year: {year}.)

# probably delete this dictionary structure, but we'll cross that bridge. -Evan
big_df = {}
#TODO: This needs to be a while loop (while year <2022) or something like that -Evan
for i in range(year, 2021): # the years are not in a list because we'll be adding +1
    SOME_YEAR_DF_HERE[FIXTHIS_TIMOTHY] = pd.DataFrame() # Here is where the individual year dataframe is created.
#print(big_df)

    # Loop through links_df to scrape all players data:

    ### Continue here with the webpage parsing code.
    ### Need to create a beautifulsoup object to parse the whole page:
        res = requests.get(url)
        webpage = res.content # TODO: Explore the following soup object to get that specific table for all temp data of that year!
        soup = BeautifulSoup(webpage, 'html.parser')

    ### pd.read_html() parses for tables and returns a list of dataframes.
    # TODO: figure out which element has the table we need to send to a DataFrame below:
        dfs = pd.read_html(webpage)
        # See if this df at index 0 gives us the whole table for that year:
        df = dfs[0]


    ### The yearly tables don't include a year column so adding that within the loop here:
        df['Year'] = year

        ### Now concatenate that year's dfs[0] with the global df that will contain all years temp data 2000 - 2020:
        print(f'{year} DataFrame concatenated to the (single dataframe to be outputted as CSV).')
        # The concat line below needs to be adapted for our Temperature table data scrape:
        big_df[player_pos] = pd.concat([big_df[player_pos], df], ignore_index=True, axis=0)
        #print(big_df[player_pos])

    except AttributeError:  # the except statement sends Attribute errors to a list that can be exported after the loop is finished.
        exceptions.append(url)
        print('There was at least one error during web scrape loop')

    else:
        pass

# This is where you write the output DataFrame to a CSV:
# TODO: Make this write to a dynamic path in the project folder. Use Pandas .to_csv to write the csv. Not this method:
    with open(
            r'C:\Users\EvanS\Programming\PyCharm\Projects\Mosquito_project_3_location_here\County_temperature.csv', 'w') as fp:
        fp.write('\n'.join(exceptions))

### End code block here.
#-----------------------------------------------------------------------------------------------------------------------

### Send the completed positional DataFrames to SQL database using the defined function python_to_postgres
python_df_to_postgres(big_df, 'county_temperatures_df', 'replace')