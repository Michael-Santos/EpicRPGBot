import os
from selenium import webdriver

class Browser:
    def __init__(self, config):
        self._config = config
        driver_path = os.path.join(".", "src", "drivers", "chromedriver.exe")
        self.driver = webdriver.Chrome(executable_path=driver_path)

    
    def login(self):
        url = self._config["EPICRPG_LOGIN_URL"]
        username = self._config["EPICRPG_USERNAME"]
        password = self._config["EPICRPG_PASSWORD"]
        
        self.driver.get(url)
        
        pass

    def execute_command(self, command):
        pass