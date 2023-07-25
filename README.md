# Project_3_Mosquito-borne_Diseases
Project 3: Mapping Mosquito-borne illnesses in Minnesota

Group 4

Graded __/100


## Project Description:
This project is to analyze trends in mosquito-borne illnesses in the state of Minnesota. The rate of illnesses was compared to available state watershed and climate data.
	The data used in this project was generated from the sources listed below and is intended for educational purposes only.


## Tools and Methods Used:

- JavaScript:
	libraries: D3, Leaflet, ...

- Python:
	modules: Flask, Pandas, JSON
	methods: ...

- SQL Database: 
	PostgreSQL

- Git collaboration


## Methods below are reference as of July 18, 2023. In-progress:
### Extract:
	Import raw data from CSV and .xlsx formats. 

### Transform:
	String manipulation and list comprehension cleaning to read data into Pandas DataFrame objects.
	Merge and append operations to manipulate DataFrame objects.

### Load:
	Final output writes DataFrames to CSV format for further end-user application.


### PostgreSQL Database:
	Imported CSV output files to local postgreSQL server.
	Assigned primary and foreign keys, defined relationships between tables.

### Visualization:
	Leaflet heat mapping, filter layers, ...
	Pareto bar chart, ...


## Collaborators:
Ryan C.

Miranda D.

Kevin M.

Timothy S.

Evan S.


## Sources: in-progress July 18, 2023
[1] edX Boot Camps LLC. Module 14 ...

[2] Row objects to tuples for JSON serializing:
	https://stackoverflow.com/questions/71724579/row-is-not-json-serializable-error-when-sending-result-set-to-a-flask-view

[3] Config file setup and reference:
	https://www.c-sharpcorner.com/article/configuration-files-in-python/#:~:text=Config%20files%20are%20used%20to,at%20some%20point%2C%20of%20time