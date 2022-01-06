import configparser
import common.Constants as Constants

config = None  

def init():
    global config
    config = configparser.ConfigParser()
    config.read(Constants.CONFIG_LOCATION)

def getSection(sectionName):
    global config
    return config[sectionName]

def getDataLocationsData(key):
    return getSection(Constants.CONFIG_DATA_LOCATIONS)[key]

def getOperationalData(key):
    return getSection(Constants.CONFIG_OPERATIONAL)[key]