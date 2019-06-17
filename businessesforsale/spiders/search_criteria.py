from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os


options = Options()
options.add_argument('--headless')
options.add_argument('disable-gpu')
options.add_argument('window-size=1200,1100')
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")



class SelectingSearchParametrs():


    def __init__(self):
        self.browser = webdriver.Chrome(executable_path=os.getcwd() + '/chromedriver', options=options)
        self.browser.get('https://www.businessesforsale.com/search/businesses-for-sale')


    def login(self, login, password):
        self.browser.get('https://www.businessesforsale.com/login.aspx')
        self.browser.find_element_by_xpath('//input[@id="username"]').send_keys(login)
        self.browser.find_element_by_xpath('//input[@name="password"]').send_keys(password)
        self.browser.find_element_by_xpath('//input[@value="Login"]').click()
        self.browser.get('https://www.businessesforsale.com/search/businesses-for-sale')


    def select_business_category(self, category):
        try:
            Elem = WebDriverWait(self.browser, 15).until(EC.presence_of_element_located((By.XPATH, '//a[@id="category-trigger-1"]/i')))
        except TimeoutException:
            print("Element does't loaded")
        buisness_category = self.browser.find_element_by_xpath('//a[@id="category-trigger-1"]/i').click()
        time.sleep(5)
        try:
            Elem = WebDriverWait(self.browser, 15).until(EC.presence_of_element_located((By.XPATH, '//select[@id="category-select-1"]')))
        except TimeoutException:
            print("Element does't loaded")
        select = Select(self.browser.find_element_by_xpath('//select[@id="category-select-1"]'))
        all_selected_options = select.options
        for i in all_selected_options:
            text = i.text
            if category.lower() in text.lower():
                val = i.get_attribute('value')
                try:
                    ActionChains(self.browser).move_to_element(self.browser.find_element_by_xpath('//select[@id="category-select-1"]//option[@value="' + val + '"]')).click().perform()
                except StaleElementReferenceException:
                    pass
                ActionChains(self.browser).move_to_element(self.browser.find_element_by_xpath('//input[@value="Update Results"]')).click().perform()
                time.sleep(3)
                return None
        print('No such category')


    def select_business_sub_category(self, sub_category):
        try:
            Elem = WebDriverWait(self.browser, 15).until(EC.presence_of_element_located((By.XPATH, '//a[@id="category-trigger-1"]/i')))
        except TimeoutException:
            print("Element does't loaded")
        buisness_category = self.browser.find_element_by_xpath('//a[@id="category-trigger-1"]/i').click()
        time.sleep(5)
        select = Select(self.browser.find_element_by_xpath('//select[@id="category-select-2"]'))
        all_selected_options = select.options
        for i in all_selected_options:
            text = i.text
            if sub_category.lower() in text.lower():
                val = i.get_attribute('value')
                try:
                    ActionChains(self.browser).move_to_element(self.browser.find_element_by_xpath('//select[@id="category-select-2"]//option[@value="' + val + '"]')).click().perform()
                except StaleElementReferenceException:
                    pass
                ActionChains(self.browser).move_to_element(self.browser.find_element_by_xpath('//input[@value="Update Results"]')).click().perform()
                time.sleep(3)
                return None
        print('No such subcategory')



    def select_countries(self, countrie):
         countries = self.browser.find_element_by_xpath('//a[@id="region-trigger-1"]/i').click()
         time.sleep(3)
         try:
             ActionChains(self.browser).move_to_element(self.browser.find_element_by_xpath('//span[@class="suggestion" and contains(., "' + countrie.capitalize() + '")]')).click().perform()
         except NoSuchElementException:
             print('There is no country for this category')
         time.sleep(3)


    def select_asking_price(self, min_price, max_price):
        self.browser.find_element_by_xpath('//input[@name="Price.From"]').send_keys(min_price)
        time.sleep(1)
        self.browser.find_element_by_xpath('//input[@name="Price.To"]').send_keys(max_price)
        time.sleep(3)
        ActionChains(self.browser).move_to_element(self.browser.find_element_by_xpath('(//div[@class="financial-form"]//input[@value="Update Results"])[1]')).click().perform()


    def select_fash_flow(self, min_price, max_price):
        self.browser.find_element_by_xpath('//input[@name="Profit.From"]').send_keys(min_price)
        time.sleep(1)
        self.browser.find_element_by_xpath('//input[@name="Profit.To"]').send_keys(max_price)
        time.sleep(3)
        ActionChains(self.browser).move_to_element(self.browser.find_element_by_xpath('(//div[@class="financial-form"]//input[@value="Update Results"])[2]')).click().perform()


    def select_sales_revenue(self, min_price, max_price):
        self.browser.find_element_by_xpath('//input[@id="turnoverFrom"]').send_keys(min_price)
        time.sleep(1)
        self.browser.find_element_by_xpath('//input[@id="turnoverTo"]').send_keys(max_price)
        time.sleep(3)
        ActionChains(self.browser).move_to_element(self.browser.find_element_by_xpath('(//div[@class="financial-form"]//input[@value="Update Results"])[3]')).click().perform()




if __name__ == "__main__":
    selecter = SelectingSearchParametrs()
    selecter.login('random1k11@yandex.ru', 'dima1994')
    # selecter.select_business_category('Tech & Media')
    # selecter.select_business_sub_category('Information Technology')
    # selecter.select_countries('italy')
    # selecter.select_asking_price('1000', '5000')
    # selecter.select_fash_flow('2000', '7000')
    # selecter.select_sales_revenue('100', '300')
