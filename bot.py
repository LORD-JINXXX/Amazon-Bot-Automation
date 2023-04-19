from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import Bot.constants as const
import os
import time



class Bot(webdriver.Chrome):
    def __int__(self,driver_path = r"your chrome driver path"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Bot,self).__init__()

    def maxwin(self):
        self.maximize_window()

    def lan_Amazon(self):
        self.get(const.base_url)

    def menu_btn(self):
        btn = self.find_element(by=By.ID,value='nav-hamburger-menu')
        btn.click()

    def sign_btn(self):
        hello_btn = self.find_element(by=By.ID, value='hmenu-customer-name')
        hello_btn.click()
        time.sleep(5)

    def username(self):
        username_input = self.find_element(by=By.ID, value='ap_email')
        username_input.send_keys(const.user_id)
        username_input.send_keys(Keys.RETURN)
        time.sleep(5)

    def password(self):
        password_field = self.find_element(by=By.ID, value='ap_password')
        password_field.send_keys(const.password)
        password_field.send_keys(Keys.RETURN)
        time.sleep(5)

    def search(self):
        search_btn = self.find_element(by=By.ID, value='twotabsearchtextbox')
        search_btn.send_keys(const.search)
        search_btn.send_keys(Keys.RETURN)
        time.sleep(5)

    def review(self,rating=None):
        review = self.find_element(by=By.CSS_SELECTOR,value= f'section[aria-label*="{rating} Stars & Up"]')
        review.click()
        time.sleep(5)

    def price_set(self,low:int=None,high:int=None):
        l_price = self.find_element(by=By.ID,value='low-price')
        l_price.send_keys(low)
        h_price = self.find_element(by=By.ID,value='high-price')
        h_price.send_keys(high)
        go = self.find_element(by=By.CLASS_NAME,value="a-button-input")
        go.click()
        time.sleep(5)

    def select_item(self,count=None):
        xPathTitle = '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[' + str(count) + ']/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span'
        item = self.find_element(by=By.XPATH,value=xPathTitle)
        item.click()
        time.sleep(5)

    def add_to_cart(self):
        xPathAdd = '//*[@id="add-to-cart-button"]'
        add = self.find_element(by=By.XPATH,value=xPathAdd)
        add.click()
        time.sleep(5)


    def switch(self):
        self.switch_to.window(self.window_handles[1])


