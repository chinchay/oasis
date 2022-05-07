
## https://github.com/meteostat/meteostat-python

# Import Meteostat library and dependencies
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily

def getLastYear():
    lastYear = 2021 #####
    return lastYear

def getTimeFrame(year):
    # Set time period
    start = datetime(year, 1, 1)
    end   = datetime(year, 12, 31)
    return start, end
#

def getLocation():
    # Create Point for Vancouver, BC
    location = Point(49.2497, -123.1193, 70)
    return location
#

def getDailyData(year):
    # Get daily data for `year`
    start, end = getTimeFrame(year)
    location = getLocation()
    data = Daily(location, start, end)
    data = data.fetch()
    return data
#

## Plot line chart including average, minimum and maximum temperature
# data.plot(y=['tavg', 'tmin', 'tmax'])
#plt.show()

def getCoords():
    coords = [ [49.2497, -123.1193, 70] ]  ##??# Create Point for Vancouver, BC
    return coords

def get_dailyT_avg(data):
    daily_t = [0,0,0,0]
    return daily_t

def getDataLastYear():
    year = getLastYear()
    start, end = getTimeFrame(year)
    coords = getCoords()
    daily_t_world = []
    for coord in coords:
        location = Point( coord )
        data = Daily(location, start, end)
        data = data.fetch()
        daily_t = get_dailyT_avg()
        daily_t_world.append(daily_t)
    #
    return daily_t_world
#

# Practical tutorial in Portuguese:
# https://www.youtube.com/watch?v=QkDiBWJ8Row
import requests
import json

def store(): # do it just once per year
    daily_t_world = getDataLastYear()
    link = "https://oasis-cloud-default-rtdb.firebaseio.com/"
    for cityCode in daily_t_world:
        d = {day: temperature}
        resquisicao = request.post( f'{link}/{cityCode}/.json', data=d )
    #
    # temperatures for cities for the last year has been saved in the database
#

#

def requestData():
    data = []
    for cityCode in daily_t_world:
        requisicao = requests.get(f'{link}/{cityCode}/.json')
        data.append([cityCode, requisicao])
    #
    return data
#

def workWithData():
    # data = requestData()
    return bestcity

    

