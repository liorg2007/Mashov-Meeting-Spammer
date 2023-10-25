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

    #enter login
    driver.find_element('xpath','/html/body/mshv-root/mshv-login/mat-card/mat-tab-group/mat-tab-header/div/div/div/div[2]/span[2]/span').click()
    time.sleep(1)
    driver.find_element('xpath','/html/body/mshv-root/mshv-login/mat-card/mat-tab-group/div/mat-tab-body[2]/div/div/button/span[2]').click()
    time.sleep(1)

    #login details:
    driver.find_element('xpath','/html/body/section/div[1]/div[3]/div[1]').click()
    #user name
    driver.find_element('xpath', '/html/body/section/div[1]/div[3]/form/fieldset/input[2]').send_keys(user_name)
    #password
    driver.find_element('xpath', '/html/body/section/div[1]/div[3]/form/fieldset/span/input[4]').send_keys(password)
    #send details
    driver.find_element('xpath','/html/body/section/div[1]/div[3]/form/fieldset/button').click()
    time.sleep(2)
    driver.find_element('xpath', '/html/body/mshv-root/mshv-login/mat-card/mat-tab-group/div/mat-tab-body[2]/div/div/button').click()
    time.sleep(2)

    #enter the lessons menu
    driver.find_element('xpath', '/html/body/mshv-root/mshv-main/mat-sidenav-container/mat-sidenav/div/mshv-main-menu/ul/li[26]/button/span[2]/div').click()
    p = driver.current_window_handle

    for i in range(NUM_OF_ENTRIES):
        time.sleep(0.2)
        #swith to main tab
        driver.switch_to.window(p)
        #enter the selected lesson
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
