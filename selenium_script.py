from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.opentable.com")

try:

    search_bar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label='Please input a Location, Restaurant or Cuisine']"))
    )
    search_bar.send_keys("Oliver's Italian")

    find_table_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label=\"Let’s go\"]"))
    )

    find_table_button.click()

    restaurant_image = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "img[alt=\"A photo of Oliver's Italian restaurant\"]"))
    )

    restaurant_image.click()

    party_size_dropdown = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//select[@aria-label='Party size selector']"))
    )
    select_party_size = Select(party_size_dropdown)
    select_party_size.select_by_value("2")

    print("Successfully selected party size")



finally:
    driver.quit()