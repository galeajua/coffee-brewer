import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd
from io import StringIO

# create class to load/save csv data

class DataLoader:
    def __init__(self, source_url):
        self.source_url = source_url

    def set_driver_options(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        return chrome_options

    def load_resource(self, by_strategy, identifier, attribute_name):
        chrome_options = self.set_driver_options()
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(self.source_url)

        content = None
        try:
            content_initial = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((by_strategy, identifier))
            )
            content = content_initial.get_attribute(attribute_name)
            content_df = pd.read_csv(StringIO(content))
        except TimeoutException:
            print("element did not load in time")
            content_df = None
        except pd.errors.ParserError:
            print("content is not in a valid csv format")
            content_df = None
        finally:
            driver.quit()
        return content_df




