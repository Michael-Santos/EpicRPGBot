import os
import time
from selenium import webdriver

class Browser:
    def __init__(self, config):
        self._config = config
        driver_path = os.path.join(".", "src", "drivers", "chromedriver.exe")
        options = webdriver.ChromeOptions()
        userdata = "user-data-dir=" + self._config["EPICRPG_PROFILE_SELENIUM_DIR"]
        options.add_argument(userdata)
        options.add_argument("--profile-directory=Selenium")
        
        try:
            self.driver = webdriver.Chrome(executable_path=driver_path, options=options)
        except:
            self.driver = webdriver.Chrome(executable_path= driver_path, options=options)

    
    def login(self):
        driver = self.driver
        url = self._config["EPICRPG_LOGIN_URL"]
        username = self._config["EPICRPG_USERNAME"]
        password = self._config["EPICRPG_PASSWORD"]

        driver.get(url)

        time.sleep(10)

        # Check if you are already logged in
        if "@me" in driver.current_url:
            return
        
        email_input = driver.find_element_by_xpath("//input[@name='email']")
        password_input = driver.find_element_by_xpath("//input[@name='password']")
        login_button = driver.find_element_by_xpath("//button[@type='submit']")

        email_input.send_keys(username)
        password_input.send_keys(password)

        login_button.click()
        pass


    def go_to_channel(self):
        driver = self.driver

        channel_url = self._config["EPICRPG_CHANNEL_URL"]
        driver.get(channel_url)

        time.sleep(10)


    def send_chat_command(self, command):
        pass