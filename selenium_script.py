from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.opentable.com")

try:

    search_bar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label='Please input a Location, Restaurant or Cuisine']"))
    )
    search_bar.send_keys("Oliver's Italian")

    restaurant_image = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "img[alt=\"A photo of Oliver's Italian restaurant\"]"))
    )

    restaurant_image.click()

    print(driver.current_url)
    print(driver.title)


finally:
    driver.quit()