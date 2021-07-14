import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Browser:
    def __init__(self, config):
        print("Starting browser")
        self._config = config
        driver_path = os.path.join(".", "src", "drivers", "chromedriver.exe")
        options = webdriver.ChromeOptions()
        userdata = "user-data-dir=" + self._config["EPICRPG_PROFILE_SELENIUM_DIR"]
        options.add_argument(userdata)
        options.add_argument("--profile-directory=Selenium")
        options.add_argument("--log-level=3")
        if config.get("EPICRPG_HEADLESS") == 'True':
            options.add_argument("--headless")

        self._driver = webdriver.Chrome(executable_path= driver_path, options=options)

    
    def login(self):
        print("Login")
        driver = self._driver
        url = self._config["EPICRPG_LOGIN_URL"]
        username = self._config["EPICRPG_USERNAME"]
        password = self._config["EPICRPG_PASSWORD"]

        driver.get(url)
        driver.set_window_size(1400,1000)

        time.sleep(10)
        # Check if you are already logged in
        if "@me" in driver.current_url:
            print("You are already logged in")
            return
        
        print("Inserting credentials")
        email_input = driver.find_element_by_xpath("//input[@name='email']")
        password_input = driver.find_element_by_xpath("//input[@name='password']")
        login_button = driver.find_element_by_xpath("//button[@type='submit']")

        email_input.send_keys(username)
        password_input.send_keys(password)

        login_button.click()
        print("Login finished")


    def go_to_channel(self):
        driver = self._driver

        channel_url = self._config["EPICRPG_CHANNEL_URL"]
        driver.get(channel_url)

        time.sleep(5)

    
    def go_to_vote(self):
        driver = self._driver

        vote_url = self._config["EPICRPG_VOTE_URL"]
        driver.get(vote_url)

        time.sleep(5)


    def send_chat_command(self, command, delay=1):
        driver = self._driver

        print(command)
        chat_input = driver.find_element_by_xpath("//div[@data-slate-object='block']")
        chat_input.send_keys(command)
        chat_input.send_keys(Keys.ENTER)

        time.sleep(delay)


    def vote(self):
        driver = self._driver

        self.go_to_vote()

        login_button = driver.find_elements_by_xpath("//a[contains(text(), 'Login')]")
        if len(login_button) != 0 and login_button[0].is_displayed():
            login_button[0].click()
            time.sleep(5)

            authorize_button = driver.find_element_by_xpath("//div[text()='Authorize']/parent::button")
            authorize_button.click()
            time.sleep(5)

        sponsor_ignore_button = driver.find_elements_by_xpath("//a[text()='No thanks']")
        if len(sponsor_ignore_button) != 0 and sponsor_ignore_button[0].is_displayed():
            sponsor_ignore_button[0].click()
            time.sleep(5)

        time.sleep(20)
        sponsor_ignore_button = driver.find_element_by_xpath("//input[@id='votingvoted']")
        sponsor_ignore_button.click()

        # TODO: It's necessary to bypass recaptcha