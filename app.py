# ### schema to connect to postgres is: "postgresql+psycopg2://username:password@host:port/database"

from flask import Flask, jsonify
from sqlalchemy import URL, inspect, create_engine, MetaData, Table
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import json

import config_file

# Reference config file for your postgres database settings.
# modify the 'example_config.ini' file and rename as 'config.ini'
config = config_file.read_config()

url_object = URL.create(
    "postgresql+psycopg2",
    username= config['SQLdb']['username'],
    password= config['SQLdb']['pwd'],
    host= config['SQLdb']['hostname'],
    database= config['SQLdb']['database'],
)


engine = create_engine(url_object)

insp = inspect(engine)
print(insp.get_table_names())

metadata = MetaData()
metadata.reflect(engine, only=['county_avg_temperature', 'county_avg_precipitation', 'WestNile-Case-Counts-by-County', 'LD-Case_Counts-by-County'])
# print(metadata)

# reflect the existing database into a new model
Base = automap_base(metadata=metadata)

# reflect the tables
Base.prepare(autoload_with=engine, reflect=True)

# temperature_data = Table("county_avg_temperature", metadata, autoload_with=engine)
# print(temperature_data.columns)

temp_table = metadata.tables['county_avg_temperature']
precip_table = metadata.tables['county_avg_precipitation']
westnile_table = metadata.tables['WestNile-Case-Counts-by-County']
lymes_table = metadata.tables['LD-Case_Counts-by-County']

# Create our session (link) from Python to the DB
session = Session(engine)


app = Flask(__name__)
# print(app)


# Assign postgres tables to variables:




@app.route('/')
def homepage():
    """List all available api routes."""
    return (
        f"Available tables API routes:<br/>"
        f"/api/county_avg_temperature<br/>"
        f"/api/county_avg_precipitation<br/>"
        f"/api/WestNile-Case-Counts-by-County<br/>"
        f"/api/LD-Case_Counts-by-County<br/>"
    )


# --------------------------------------------------------------------------
### Do table stuff here

@app.route("/api/county_avg_temperature")
def temps():
    # Create session (link) from Python to the DB
    session = Session(engine)

    # Query the session for full temperature table data:
    results = session.query(temp_table).all()
    print(type(results))
    for u in session.query(temp_table).all():
        print(__dict__)
    result_tups = [tuple(row) for row in results]
    json_string = json.dumps(result_tups)
    session.close()

    print(type(result_tups))
    return json_string



@app.route("/api/county_avg_precipitation")
def precips():
    # Create session (link) from Python to the DB
    session = Session(engine)

    # Query the session for full temperature table data:
    results = session.query(precip_table).all()
    result_tups = [tuple(row) for row in results]
    json_string = json.dumps(result_tups)
    session.close()

    print(type(result_tups))
    return json_string

@app.route("/api/WestNile-Case-Counts-by-County")
def westnile():
    # Create session (link) from Python to the DB
    session = Session(engine)

    # Query the session for full temperature table data:
    results = session.query(westnile_table).all()
    result_tups = [tuple(row) for row in results]
    json_string = json.dumps(result_tups)
    session.close()

    print(type(result_tups))
    return json_string


@app.route("/api/LD-Case_Counts-by-County")
def lymes():
    # Create session (link) from Python to the DB
    session = Session(engine)

    # Query the session for full temperature table data:
    results = session.query(lymes_table).all()
    result_tups = [tuple(row) for row in results]
    json_string = json.dumps(result_tups)
    session.close()

    print(type(result_tups))
    return json_string

# --------------------------------------------------------------------------

### make sure session is closed:
session.close()

# Run the app on local machine:
if __name__ == "__main__":
    app.run(host='localhost', debug=True)