import common.Services.LoggingService as LoggingService
import common.Services.ConfigService as ConfigService


def init():
    startup()

def startup():
    ConfigService.init()
    LoggingService.init()