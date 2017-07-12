import configparser


class BasePageObject():

    def __init__(self, driver):
        self._driver = driver
        config = configparser.ConfigParser()
        config.read('./util/settings.ini')
        self._baseUrl = config.get('Base', 'BaseUrl')
