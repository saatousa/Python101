import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import threading

url = "https://orteil.dashnet.org/experiments/cookie/"

chrome_driver_path = "/Users/atusa/Development/chromedriver"
driver = webdriver.Chrome()

driver.get(url)


def check_for_upgrades():
    money_str = driver.find_element(By.ID, "money").text.strip()

    if "," in money_str:
        money = int(money_str.replace(",", ""))
    else:
        money = int(money_str)

    store_items = driver.find_elements(By.CSS_SELECTOR, "#store b")
    costs_list = []
    items_list = []

    try:
        for item in store_items:
            item_name = item.text.split("-")[0].strip()
            items_list.append(item_name)

        items_list.reverse()
        items_list.pop(0)

        for item in store_items:
            item_cost = item.text.split("-")[1]
            if "," in item_cost:
                costs_list.append(int(item_cost.replace(",", "").strip()))

            else:
                costs_list.append(int(item_cost.strip()))

    except IndexError:
        print("no more items for now")

    costs_list.reverse()
    for cost in costs_list:
        index_num = costs_list.index(cost)
        if money > cost:
            store_item = driver.find_element(By.ID, f"buy{items_list[index_num]}")
            store_item.click()
        else:
            pass


timeout = time.time() + 60 * 5
while True:
    cookie = driver.find_element(By.ID, "cookie")
    cookie.click()
    t = threading.Timer(5, check_for_upgrades)
    t.start()

    if time.time() > timeout:
        cookie_second = driver.find_element(By.ID, "cps").text
        print(cookie_second)
        break
