import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

TWITTER_EMAIL = "..."
TWITTER_PASSWORD = "...."
TWITTER_USERNAME = "..."

speed_test_url = "https://www.speedtest.net/"
twitter_url = "https://twitter.com/?lang=en"

promised_down = 20
promised_up = 20

chrome_driver_path = "/Users/atusa/Development/chromedriver"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(speed_test_url)

        # time.sleep(3)
        go_btn = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        go_btn.click()

        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"down: {self.down}")
        print(f"up: {self.up}")

    def tweet_at_provider(self):
        self.driver.get(twitter_url)
        signin = self.driver.find_element(By.XPATH,
                                          '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a')
        signin.click()

        time.sleep(30)
        email_input = self.driver.find_element(By.XPATH,
                                               '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email_input.send_keys(TWITTER_EMAIL)

        next_btn = self.driver.find_element(By.XPATH,
                                            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
        next_btn.click()

        time.sleep(30)
        password_input = self.driver.find_element(By.XPATH,
                                                  '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.send_keys(Keys.ENTER)

        # login_btn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        # login_btn.click()

        time.sleep(5)
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {promised_down}down/{promised_up}up?"
        tweet_compose = self.driver.find_element(By.XPATH,
                                                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet_compose.send_keys(tweet)
        time.sleep(5)
        post_btn = self.driver.find_element(By.XPATH,
                                            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span')
        post_btn.click()
        time.sleep(5)


internet_speed_bot = InternetSpeedTwitterBot()
if internet_speed_bot.up < promised_up or internet_speed_bot.down < promised_down:
    internet_speed_bot.get_internet_speed()
    internet_speed_bot.tweet_at_provider()
