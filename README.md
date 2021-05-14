# Ice Cream Shop viability study using SQLite

## Project Overview
W. Avy is researching the viability of opening a surf and ice cream shop on Oahu based on the local weather. We have been provided a SQLite file with the following weather information recorded by a set of weather stations positioned throughout the island:
- measurement observation id
- measurement station name
- measurement date
- measurement daily precipitation
- measurement temperature observation
- station id
- station name
- station latitude
- station longitude
- station elevation

### Purpose
The script provides analysis of local historical temperature and precipitation data to evaluate the potential success of opening an surf and ice cream shop on Oahu. Based on client's request, we have analyzed the temperature and precipitation trends for the months of June and December.


### Resources
Data sources: 
- hawaii.sqlite

Software: 
- Python 3.7
- Jupyter Notebook
- numpy, datetime, pandas, sqlalchemy, and matplotlib modules

Documentation: 
- https://stackoverflow.com/questions/51451768/sqlalchemy-querying-with-datetime-columns-to-filter-by-month-day-year
- https://stackoverflow.com/questions/21310549/list-database-tables-with-sqlalchemy


## Analysis

### June Historical Analysis
We extracted 1700 data points for the temperature and precipitation for the month of June. 

The below images show Oahu's weather stations' statistical overview for temperature (Picture 1.1) and precipitation (Picture 1.2) in June, respectively.

**Picture 1.1: Historical temperature overview for June (degrees Farenheit)**

![Historical temperature overview for June (degrees Farenheit)](https://github.com/joshuanallen/surfs_up/blob/efe515cc327223d8e260a60a7ba9c73429862f17/analysis/Oahu_historical_temp_overview_june.png)

**Picture 1.2: Historical precipitation overview for June (inches)**

![Historical precipitation overview for June (inches)](https://github.com/joshuanallen/surfs_up/blob/efe515cc327223d8e260a60a7ba9c73429862f17/analysis/Oahu_historical_prcp_overview_june.png)

### December Historical Analysis
We extracted 1517 data points for the temperature and precipitation for the month of December. 

The below images show Oahu's weather stations' statistical overview for temperature (Picture 2.1) and precipitation (Picture 2.2) in December, respectively.

**Picture 2.1: Historical temperature overview for December (degrees Farenheit)**

![Historical temperature overview for December (degrees Farenheit)](https://github.com/joshuanallen/surfs_up/blob/efe515cc327223d8e260a60a7ba9c73429862f17/analysis/Oahu_historical_temp_overview_Dec.png)

**Picture 2.2: Historical precipitation overview for December (inches)**

![Historical precipitation overview for December (inches)](https://github.com/joshuanallen/surfs_up/blob/efe515cc327223d8e260a60a7ba9c73429862f17/analysis/Oahu_historical_prcp_overview_dec.png)


## Results

Our analysis shows the following **temperature trends** for the months of June and December:

1. June's average temperature is 3.9 degrees farenheit higher than December
    - *On average June is warmer than December*
2. December's lowest temperature is 8 degrees lower than June's lowest
    - *There are days in December potentially cold enough to dissaude customers from consuming ice cream*
3. December's standard deviation of temperature is 0.5 degrees higher than June
    - *Temperatures fluctuate more widely in December therefore making ice cream-consuming weather less predictible.*

Our analysis shows the following **precipitation trends** for the months of June and December:

1. 75% of the days in June receive less than 0.12 inches of rain and 75% of the days in December receive 0.15 inches of rain
    - *Most days on Oahu have little to no rain*
2. The average rainfall in December is 0.08 inches higher than June
    - *while still minimal rainfall day-to-day, December gets 62% more rainfall on average*
3. Both December *and* June have days where a significant amount of rain falls, but they are rare.
    - *2% of observations recorded more than 1 inch of daily rainfall in June*
    - *6% of observations recorded more than 1 inch of daily rainfall in December*
    
For the month of June, 647 (**41%**) out of the 1574 data points (126 of the 1700 data points did not have a value recorded for precipitation) or **recorded less than 0.01 inches of rain for the day**, implying the island of Oahu is typically dry and/or light rain during this timeframe.

For the month of June, 510 (**36%**) out of the 1405 data points (112 of the 1517 data points did not have a value recorded for precipitation) or **recorded less than 0.01 inches of rain for the day**, implying the island of Oahu is typically dry and/or light rain during this timeframe.

## Conclusions

Based on the high average temperatures year round and the general lack of heavy daily rainfall on Oahu (save for a few days of *heavy rainfall*), the analysis shows a **postive outlook** for a business requiring nice weather such as an ice cream and surf shop.

### Limitations of dataset and script
To further evaluate the viability of the ice cream and surf shop idea, it would be best to also include the daily surf reports for each weather station location. Therefore, further analysis on best location for said shop could be aligned with the most consistent surf shops.

Additional helpful queries would be to filter the weather data to align precipitation and temperature to get the number of "poor weather days" for surfing and consuming ice cream. This would allow us to evaluate the number of days one would expect there to be weather conducive to running such a business.
