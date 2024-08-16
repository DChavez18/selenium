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

    print("Successfully searched for Oliver's Italian")

    restaurant_image = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "img[alt=\"A photo of Oliver's Italian restaurant\"]"))
    )

    restaurant_image.click()

    print("Successfully clicked on Oliver's Italian")

    party_size_dropdown = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//select[@aria-label='Party size selector']"))
    )
    select_party_size = Select(party_size_dropdown)
    select_party_size.select_by_value("2")

    print("Successfully selected party size")

    date_picker_label = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='day-picker-overlay']"))
    )
    date_picker_label.click()

    print("Successfully clicked on date picker")

    next_month_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Next month']"))
    )

    for _ in range(3):
        next_month_button.click()
        time.sleep(1)

    print("Successfully navigated to November")

    select_date = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Saturday, November 9']"))
    )
    select_date.click()

    print("Successfully selected the date")

    time_picker = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//select[@aria-label='Time selector']"))
    )
    select_time = Select(time_picker)
    select_time.select_by_visible_text("6:30 PM")

    print("Successfully selected time")

    confirm_time_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'book/validate')]"))
    )
    confirm_time_button.click()

    print("Successfully confirmed the time")

    seating_option_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, '_3y2jpx-O-d4- rh4f9n3b2Kc- CThPxXrzskE-')]"))
    )
    seating_option_button.click()

    print("Successfully selected standard dining room seating")

    phone_number_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "phoneNumber"))
    )
    phone_number_input.send_keys("7205057736")

    print("Successfully entered the phone number")

    checkbox = driver.find_element(By.ID, "tcAccepted")
    driver.execute_script("arguments[0].checked = true;", checkbox)

    print("Successfully agreed to the terms and conditions")

    complete_reservation_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "complete-reservation"))
    )
    complete_reservation_button.click()

    print("Successfully completed the reservation")
finally:
    driver.quit()