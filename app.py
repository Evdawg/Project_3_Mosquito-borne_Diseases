# ### schema to connect to postgres is: "postgresql+psycopg2://username:password@host:port/database"

from flask import Flask, jsonify
from sqlalchemy import URL, inspect, create_engine, MetaData
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import json, sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
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

# Assign postgres table objects to variables
temp_table = metadata.tables['county_avg_temperature']
precip_table = metadata.tables['county_avg_precipitation']
westnile_table = metadata.tables['WestNile-Case-Counts-by-County']
lymes_table = metadata.tables['LD-Case_Counts-by-County']


# Create our session (link) from Python to the DB
session = Session(engine)

app = Flask(__name__)
# print(app)


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
# API routes:

@app.route("/api/county_avg_temperature")
def temps():
    # Create session (link) from Python to the DB
    session = Session(engine)

    # Query the session for full temperature table data:
    results = session.query(temp_table).all()
    # print(type(results))

    temps_list = []
    for row in results:
        temps_list.append(row._asdict())
        #print(row._asdict())
    # print(temps_list)
    session.close()

    dictionary = {i: d for i, d in enumerate(temps_list)}
    return dictionary  



@app.route("/api/county_avg_precipitation")
def precips():
    # Create session (link) from Python to the DB
    session = Session(engine)

    # Query the session for full temperature table data:
    results = session.query(precip_table).all()

    precip_list = []
    for row in results:
        precip_list.append(row._asdict())

    session.close()
    dictionary = {i: d for i, d in enumerate(precip_list)}
    return dictionary



@app.route("/api/WestNile-Case-Counts-by-County")
def westnile():
    # Create session (link) from Python to the DB
    session = Session(engine)

    # Query the session for full temperature table data:
    results = session.query(westnile_table).all()

    westnile_list = []
    for row in results:
        westnile_list.append(row._asdict())

    session.close()
    dictionary = {i: d for i, d in enumerate(westnile_list)}
    return dictionary



@app.route("/api/LD-Case_Counts-by-County")
def lymes():
    # Create session (link) from Python to the DB
    session = Session(engine)

    # Query the session for full temperature table data:
    results = session.query(lymes_table).all()

    lymes_list = []
    for row in results:
        lymes_list.append(row._asdict())
    session.close()

    dictionary = {i: d for i, d in enumerate(lymes_list)}
    return dictionary

# --------------------------------------------------------------------------

### make sure session is closed:
session.close()

# Run the app on local machine:
if __name__ == "__main__":
    app.run(host='localhost', debug=True)