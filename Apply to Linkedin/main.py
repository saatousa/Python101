import time
from selenium import webdriver
from selenium.webdriver.common.by import By

ACCOUNT_EMAIL = "..."
ACCOUNT_PASSWORD = "..."

url = "https://www.linkedin.com/jobs/search/?currentJobId=3915053224&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom"

chrome_driver_path = "/Users/atusa/Development/chromedriver"
driver = webdriver.Chrome()

driver.get(url)

first_signin_btn = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
first_signin_btn.click()

time.sleep(5)

username = driver.find_element(By.ID, "username")
username.send_keys(ACCOUNT_EMAIL)

password = driver.find_element(By.ID, "password")
password.send_keys(ACCOUNT_PASSWORD)

second_signin_btn = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container button")
second_signin_btn.click()

time.sleep(5)


job_title = driver.find_elements(By.CSS_SELECTOR, "ul li div div div a strong")
for job in job_title:
    time.sleep(5)
    job.click()
    save_btn = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    save_btn.click()
    follow_btn = driver.find_element(By.CLASS_NAME, "follow")


