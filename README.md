# Anniversary Reservation Automation

This Python script automates the process of booking a dinner reservation for your anniversary. The script uses Selenium to interact with the OpenTable website, ensuring that you don't forget to book your special night.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Notes](#notes)

## Overview
This script is designed to automate the booking of a reservation at Oliver's Italian restaurant for November 9th, 2024, at 6:30 PM. The script will:
- Search for the restaurant on OpenTable.
- Select a party size of 2.
- Navigate to the desired date (November 9th, 2024).
- Select the appropriate time (6:30 PM).
- Choose standard dining room seating.
- Enter the phone number for confirmation.
- Agree to the restaurant's terms and conditions.
- Complete the reservation.

## Prerequisites
- Python 3.x
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)
- Selenium (`pip install selenium`)

## Installation

1. **Install Python 3.x**: Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Selenium**:
   ```bash
   pip install selenium

3. **Download ChromeDriver**: Download the version of ChromeDriver that matches your installed Chrome browser

## Usage

1. **Run The Script**: To execute the script, simply run the following command in your terminal:
```bash
python3 selenium_script.py
```

2. The script will automatically navigate through the steps to book the reservation on OpenTable.

## How It Works

### Searching for the Restaurant:
The script begins by searching for "Oliver's Italian" using OpenTable's search bar.

### Selecting Party Size:
After clicking on the restaurant, the script selects a party size of 2 using the dropdown menu.

### Choosing the Date:
The script clicks on the date picker and navigates to November 2024, selecting November 9th.

### Selecting the Time:
The script selects a reservation time of 6:30 PM.

### Confirming the Reservation:
After confirming the time, the script chooses standard dining room seating and enters a phone number for reservation confirmation.

### Agreeing to Terms:
The script agrees to the restaurant's terms and conditions by checking the checkbox.

### Completing the Reservation:
Finally, the script completes the reservation by clicking the "Complete reservation" button.

## Notes

### Customization
You can customize the script for different dates, times, or restaurants by modifying the relevant parts of the code.

### Error Handling
The script includes basic error handling. If any step fails, the script will print an error message and exit gracefully.

### Automation
You can set up this script to run automatically using cron jobs (Linux/macOS) or Task Scheduler (Windows) to ensure you never miss a reservation.

## Future Iterations

### Security Enhancements
- **Secure Storage of Sensitive Data:** Implement secure methods for storing sensitive data, such as phone numbers, to avoid exposing personal information within the script.
- **Two-Factor Authentication:** If the website supports it, consider adding support for two-factor authentication to enhance security.

### Improved Error Handling
- **Detailed Error Logs:** Implement detailed logging to capture specific errors encountered during the automation process.
- **Retry Mechanism:** Add a retry mechanism to handle transient errors, such as network issues, to ensure the reservation process completes successfully.

### Customization Options
- **User Interface:** Develop a simple user interface that allows users to input the desired reservation details without modifying the script directly.
- **Configuration File:** Introduce a configuration file to store reservation details, making it easier to update parameters like date, time, or restaurant.