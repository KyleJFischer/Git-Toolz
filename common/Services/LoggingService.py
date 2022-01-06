import logging
import common.Services.ConfigService as ConfigService


def init():
    logLevelString = ConfigService.getOperationalData("LogLevel")
    logLevel = logging.getLevelName(logLevelString)

    logFileLocation = ConfigService.getDataLocationsData("LogFileLocation")

    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=level, filename=logFileLocation)
    logging.debug("Logging System Initialized")

def logInfo(message):
    logging.info(message)

def logDebug(message):
    logging.debug(message)

def logWarning(message):
    logging.warning(message)

def logError(message):
    logging.error(message)
