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