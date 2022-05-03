import cloud as cloud

cities = []
Tmin = 20
Tmax = 24
scoreTheshold = 90

bestRange = [Tmin, Tmax]


def belongs(x, xmin, xmax):
    return (xmin <= x) & (x <= xmax)
#

def getScore(temperatures):
    score = sum(temperatures) / len(temperatures) # to be improved
    return score
#

def getBestCities():
    bestCities = []
    for city in cities:
        temperatures = cloud.getCityTemperatures(city)
        score = getScore(temperatures)
        if score > scoreTheshold:
            bestCities.append(city)
        #
    #
    return bestCities
#

def displayBestCities(bestCities):
    return
#



