# Project_3_Mosquito-borne_Diseases
Project 3: Mapping Mosquito-borne illnesses in Minnesota

Graded __/100


## Project Description:
This project is to analyze trends in vector-borne (tick and mosquito) illnesses in the United States. The rate of illnesses was visually compared to available county temperature and precipitation data.


The data used in this project was generated from the sources listed below and is intended for educational purposes only.


## Tools and Methods Used:

- JavaScript:
	libraries: D3, Leaflet (heatmap, CSS) ...

- Python:
	modules: Flask, SQLAlchemy, pandas, splinter, BeautifulSoup, JSON, configparser, numpy
	methods: ...

- SQL Database: 
	PostgreSQL server

- Git collaboration


## Methods below are reference as of July 25, 2023. In-progress:
### Extract:
	Scrape website table data using splinter and BeautifulSoup.

	Export pandas DataFrames to CSV. 

	Imported CSV output files to local postgreSQL server


### Transform:
	String manipulation and list comprehension cleaning to read data into Pandas DataFrame objects.
	Merge and append operations to manipulate DataFrame objects.


### Load:
	Load postgres database tables to Python Flask API.

	Call Flask API data using JavaScript.


### Visualization:
	Leaflet heat mapping, filter layers, ...

	Pareto bar chart, ...




## SQL Database Setup and Data Import instructions:

1) in pgAdmin, create new Database titled "Project_3"
2) Right-click the Project_3 Database and select "Query Tool"
3) Above the Query tool text input window, click "Open File"
4) Open the Project_3_tables_schema.sql file here. Execute the query here to populate tables.
5) Manually import the CSV files from the Data folder by right-clicking each table in pgAdmin and selecting "Import/Export Data..."
6) Confirm all data imported by running SELECT * statements in pgAdmin query window.


### Flask app for API setup instructions:
1) Modify example_config.ini to reference your postgres database information.
	- database was named 'Project_3'
	- hostname remains as 'localhost', port remains as '5432'
	- Update your specific username (may be defaulted as 'postgres') and password for local postgres server.
2) Run app.py and confirm API data outputs are correct.



## Collaborators:
Ryan C.

Miranda D.

Kevin M.

Timothy S.

Evan S.



## Data sources:
1) USA Counties Temperature and Precipitation:
	https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/county/mapping

2) West Nile case incidence data:
	https://www.cdc.gov/westnile/statsmaps/historic-data.html

3) Lyme Disease case incidence data:
	https://www.cdc.gov/lyme/datasurveillance/lyme-disease-maps.html#print




## Methods sources: in-progress July 25, 2023
[1] Flask API setup, Leaftlet heatmapping, ...
	edX Boot Camps LLC. Multiple lecture activities.

[2] Row objects to tuples for JSON serializing:
	https://stackoverflow.com/questions/71724579/row-is-not-json-serializable-error-when-sending-result-set-to-a-flask-view

[3] Config file setup and reference:
	https://www.c-sharpcorner.com/article/configuration-files-in-python/#:~:text=Config%20files%20are%20used%20to,at%20some%20point%2C%20of%20time