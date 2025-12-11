from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import yaml

class DriverFactory:

    @staticmethod
    def get_driver():
        with open("config/config.yaml", "r") as f:
            config = yaml.safe_load(f)

        browser = config["browser"]

        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        driver.implicitly_wait(config["implicit_wait"])

        return driver
