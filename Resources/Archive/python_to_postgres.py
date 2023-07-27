import config_file
from sqlalchemy import create_engine, URL

### This is a template for using config file settings to connect to user's SQL db.

#-----------------------------------------------------------------------------------------------------------------------

### Input pandas dataframe and desired postgreSQL table name and write to local postgreSQL server:
## table_name is string. dataframe is pandas DataFrame object.
## if_exists is a string value: one of {‘fail’, ‘replace’, ‘append’} for writing to SQL database.
def python_df_to_postgres(dataframe, table_name, if_exists):
    # Reads the config file for reference to user SQLdb
    config = config_file.read_config()

    # construct a URL object to utilize config.ini settings:
    url_object = URL.create(
        "postgresql+psycopg2",
        username= config['SQLdb']['username'],
        password= config['SQLdb']['pwd'],
        host= config['SQLdb']['hostname'],
        database= config['SQLdb']['database'],)

    try:
    # Create the engine:
        engine = create_engine(url_object)


    #-----------------------------------------------------------------------------------------------------------------------
    ### Place your code block here that outputs a Pandas DataFrame:



    # dataframe = <pd.DataFrame()>
    # table_name = '<my_table_name>'
    # if_exists = 'replace'  # or {‘fail’, ‘replace’, ‘append’}


    ### End code block here.
    #-----------------------------------------------------------------------------------------------------------------------

    # Send the Pandas DataFrame to a SQL database using psycopg2 and SQLalchemy libraries:
        with engine.begin() as connection:
            dataframe.to_sql(
                name= table_name,
                con= engine,
                if_exists= if_exists, # or {‘fail’, ‘replace’, ‘append’}, default ‘fail’
                index= False)


    # Close the connection if no error in try-except block:
    except Exception as error:
        print(error)

    return
