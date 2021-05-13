# import dependencies
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Set up DATABASE

# create database engine w/ sqlite file
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect database into classes
Base = automap_base() # automaps classes
Base.prepare(engine, reflect=True) #reflects db

# save table references as variables
Measurement = Base.classes.measurement
Station = Base.classes.station

# initiate a Python session link to database
session = Session(engine)



# Set up Flask app

# create Flask app named "app"
app = Flask(__name__)

# Create "root"/home route
@app.route("/")
# route delivers welcome() function
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/en
    ''')

# create precipitation route
@app.route("/api/v1.0/precipitation")
# pull in precip numbers with function
def precipitation():
    # add variables and analysis code
    # calculate previous year
    prev_year = dt.date(2017 ,8 , 23) - dt.timedelta(days = 365)
    
    # query for date and precip for previous year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    
    # create results dictionary to jsonify output
    precip = {date: prcp for date, prcp in precipitation}

    # return precip data and structure it in JSON
    return jsonify(precip)

# create a stations route
@app.route("/api/v1.0/stations")
# pull in stations info with function
def stations():
    # add variables and analysis code
    results = session.query(Station.station).all()
    # unravel our results into a one-dimensional array using np.ravel() function
    # then convert unraveled results to a list for export using list() function
    stations = list(np.ravel(results))
    
    # return stations data and structure it in JSON
    # use stations=stations inside argument: https://flask.palletsprojects.com/en/1.1.x/api/#flask.json.jsonify
    return jsonify(stations=stations)


# create observations route
@app.route("/api/v1.0/tobs")

# pull in tobs info with function
def temp_monthly():
    # add variables and analysis code
    # calculate previous year
    prev_year = dt.date(2017 ,8 , 23) - dt.timedelta(days = 365)
    
    # query primary station for observation info
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    # unravel results and convert to list
    temps = list(np.ravel(results))
    # return temps in JSON structure
    return jsonify(temps=temps)


# create route for statistics report
# route is different from the previous ones in that we will have to provide both a starting and ending date.
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# create function to pull in stats for given time frame
# add start and end date parameters to function
def stats(start = None, end = None):
    
    # create a query to select the minimum, average, and maximum temperatures from our SQLite database
    # create list called sel to hold query results
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    # need to determine the starting and ending date, add an if-not statement to our code
    if not end:
        # query our database using the list that we just made
        # asterisk is used to indicate there will be multiple results for our query: minimum, average, and maximum temperatures
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        # unravel the results into a one-dimensional array and convert them to a list
        temps = list(np.ravel(results))
     # jsonify our results and return them 
        return jsonify(temps=temps)

    # calculate the temperature minimum, average, and maximum with the start and end dates
    # use the sel list, which is simply the data points we need to collect
    # create our next query, which will get our statistics data
    # filter sel data between start and end dates
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)