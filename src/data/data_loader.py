import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

class DataLoader:
    def __init__(self, source_url):
        self.source_url = source_url

    def load_resource(self, by_strategy, identifier, attribute_name):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--no-sandbox")  # Optional: Helps with certain environments
        chrome_options.add_argument("--disable-dev-shm-usage")  # Optional: Reduces resource usage
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(self.source_url)

        content = None
        try:
            content_initial = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((by_strategy, identifier))
            )
            content = content_initial.get_attribute(attribute_name)
            lines = content.splitlines()
            for line in lines[:5]:  # Print the first 5 lines to check if csv structure
                print(line)
        except:
            print("Element did not load in time.")
        finally:
            driver.quit()
        return content
    
    def save_raw_data_locally(self, content, path):
        with open(path, "w") as f:
            f.write(content)

        return pd.read_csv(path)

    # def load_resource_click(self):



