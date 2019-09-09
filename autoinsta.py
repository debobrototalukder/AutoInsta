from selenium import webdriver
from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


browser = webdriver.Chrome('/Users/debobroto/Documents/WebDriver/chromedriver')
browser.get('https://www.instagram.com/')


login_elem = browser.find_element_by_xpath('//article/div/div/p/a[text()="Log in"]')
login_elem.click()

sleep(3)

browser.find_element_by_name('username').send_keys('yourusername')
browser.find_element_by_name('password').send_keys('yourpassword')
sleep(2)
browser.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0].click()
sleep(4)

browser.find_elements_by_xpath("//button[contains(text(), 'Not Now')]")[0].click()

browser.fullscreen_window()

sleep(2)

searchbox = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Search']")
    )
)

searchbox.send_keys('usernametosearch')
sleep(2)
searchbox.send_keys(Keys.ENTER)
sleep(1)
searchbox.send_keys(Keys.ENTER)

sleep(2)

first_picture = browser.find_elements_by_xpath("(//div[@class=\"eLAPa\"]//parent::a)[1]")
first_picture[0].click()

like_xpath = "//span[contains(@class,\"glyphsSpriteHeart\") and @aria-label = \"Like\"]//parent::button"

sleep(5)

for i in range(40):
    browser.find_elements_by_xpath(like_xpath)[0].click()
    sleep(2)
    browser.find_elements_by_xpath("//a[contains(text(), 'Next')]")[0].click()
    sleep(2)


sleep(2)


