from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

reservation_date = input("Please enter the desired reservation date (e.g., 'Friday, November 8, 2024'): ")
desired_time = input("Please enter the desired reservation time (e.g., '6:30 PM'): ")

def navigate_to_site(driver, url):
    try:
        driver.get(url)
        print(f"Successfully navigated to {url}")
    except Exception as e:
        print(f"Failed to navigate to {url}: {e}")

def perform_search(driver):
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
    except Exception as e:
        print(f"Failed to perform search: {e}")

def select_restaurant(driver):
    try:
        restaurant_image = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "img[alt=\"A photo of Oliver's Italian restaurant\"]"))
        )
        restaurant_image.click()
        print("Successfully clicked on Oliver's Italian")
    except Exception as e:
        print(f"Failed to select restaurant: {e}")

def select_party_size(driver):
    try:
        party_size_dropdown = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//select[@aria-label='Party size selector']"))
        )
        select_party_size = Select(party_size_dropdown)
        select_party_size.select_by_value("2")
        print("Successfully selected party size")
    except Exception as e:
        print(f"Failed to select party size: {e}")

def select_date(driver, desired_date):
    try:
        date_picker_toggle = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@data-test='icDown']"))
        )
        date_picker_toggle.click()

        date_parts = desired_date.split(", ")
        
        if len(date_parts) != 3:
            print(f"Invalid date format. Please input in format 'Friday, November 8, 2024'.")
            return

        target_day = date_parts[1].split(" ")[1] 
        target_month_year = f"{date_parts[1].split(' ')[0]} {date_parts[2]}"
        target_aria_label = f"{date_parts[0]}, {date_parts[1]}" 

        max_attempts = 12
        attempts = 0

        while attempts < max_attempts:
            displayed_month_year_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "react-day-picker-1"))
            )
            displayed_month_year = displayed_month_year_element.text

            print(f"Displayed Month-Year: {displayed_month_year}")
            print(f"Target Month-Year: {target_month_year}")

            if displayed_month_year == target_month_year:
                print(f"Successfully navigated to {target_month_year}")
                break

            next_month_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@data-test='icRight']"))
            )
            next_month_button.click()
            time.sleep(2) 

            attempts += 1

        if attempts == max_attempts:
            print(f"Failed to navigate to {target_month_year}. Max attempts reached.")
            return

        try:
            time.sleep(2)
            select_day = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//button[@aria-label='{target_aria_label}']"))
            )
            select_day.click()

            print(f"Successfully selected the date: {desired_date}")
        except Exception as day_selection_error:
            print(f"Failed to click on the correct day. Error: {day_selection_error}")
            return

    except Exception as e:
        print(f"Failed to select date: {e}")

def select_time(driver):
    try:
        time_picker = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//select[@aria-label='Time selector']"))
        )
        select_time = Select(time_picker)

        try:
            select_time.select_by_visible_text(desired_time)
            print(f"Successfully selected time: {desired_time}")
        except:
            print(f"Desired time {desired_time} not available. Trying to select the first available time.")
            available_time = time_picker.find_elements(By.TAG_NAME, "option")[1]
            select_time.select_by_visible_text(available_time.text)
            print(f"Selected available time: {available_time.text}")
    except Exception as e:
        print(f"Failed to select time: {e}")

def confirm_time(driver):
    try:
        confirm_time_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'book/validate')]"))
        )
        confirm_time_button.click()
        print("Successfully confirmed the time")
    except Exception as e:
        print(f"Failed to confirm time: {e}")

def select_seating_option(driver):
    try:
        seating_option_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, '_3y2jpx-O-d4- rh4f9n3b2Kc- CThPxXrzskE-')]"))
        )
        seating_option_button.click()
        print("Successfully selected standard dining room seating")
    except Exception as e:
        print(f"Failed to select seating option: {e}")

def enter_phone_number(driver):
    try:
        phone_number_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "phoneNumber"))
        )
        phone_number_input.send_keys("7205057736")
        print("Successfully entered the phone number")
    except Exception as e:
        print(f"Failed to enter phone number: {e}")

def accept_terms(driver):
    try:
        checkbox = driver.find_element(By.ID, "tcAccepted")
        driver.execute_script("arguments[0].checked = true;", checkbox)
        print("Successfully agreed to the terms and conditions")
    except Exception as e:
        print(f"Failed to accept terms and conditions: {e}")

def complete_reservation(driver):
    try:
        complete_reservation_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "complete-reservation"))
        )
        complete_reservation_button.click()
        print("Successfully completed the reservation")
    except Exception as e:
        print(f"Failed to complete the reservation: {e}")

driver = webdriver.Chrome()

try:
    navigate_to_site(driver, "https://www.opentable.com")
    perform_search(driver)
    select_restaurant(driver)
    select_party_size(driver)
    select_date(driver, reservation_date)
    select_time(driver)
    confirm_time(driver)
    select_seating_option(driver)
    enter_phone_number(driver)
    accept_terms(driver)
    complete_reservation(driver)
finally:
    driver.quit()