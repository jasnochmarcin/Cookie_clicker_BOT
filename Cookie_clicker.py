from selenium import webdriver
import time

window = webdriver.Chrome("C:\Program Files (x86)\Chromedriver\chromedriver.exe")
window.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(2)

cookie = window.find_element_by_xpath("/html/body/div/div[2]/div[15]/div[8]/div[1]")
shop_products = window.find_elements_by_xpath("/html/body/div/div[2]/div[19]/div[3]/div[6]/*")
shop_products.reverse()

click_counter = 0

def buy_items():
    buy_best = False
    for item in shop_products:
        if item.get_attribute("class") == "product unlocked enabled":
            item.click()
            buy_best = True
            break
    if buy_best is True:
        buy_items()


while True:
    cookie.click()
    click_counter += 1
    if click_counter == 500:
        buy_items()
        click_counter = 0