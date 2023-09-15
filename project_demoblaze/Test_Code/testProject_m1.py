from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from Test_Data import project_m
import pytest
import time 

class Test_Project_4:
    url = "https://www.demoblaze.com/ " 

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Edge()
        yield
        self.driver.close() 
           
    def test_home(self, booting_function):
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(3)
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="login2"]'))
        WebDriverWait(self.driver,timeout= 10).until(element_present)
        print("Page loaded successfully!")
        time.sleep(3)
        s1=self.driver.find_element(By.XPATH,value=project_m.Project_Data_1.logo_xpath)
        if s1.is_displayed():
            print("Websitelogo is presented") 
        s2=self.driver.find_element(By.XPATH,value=project_m.Project_Data_1.navi_xpath)
        if s2.is_displayed():
            print("Navigation menu is presented")
        s3=self.driver.find_element(By.XPATH,value=project_m.Project_Data_1.productany_xpath)
        if s3.is_displayed():
            print("product is presented") 
        time.sleep(2)
        
    def test_registration(self,booting_function):
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(3)        
        self.driver.find_element(By.XPATH,value=project_m.Project_Data_1.signup_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,value=project_m.Project_Data_1.username_xpath).send_keys(project_m.Project_Data_2.username)
        time.sleep(3)
        self.driver.find_element(By.XPATH,value=project_m.Project_Data_1.password_xpath).send_keys(project_m.Project_Data_2.password)
        time.sleep(3)
        self.driver.find_element(By.XPATH,value=project_m.Project_Data_1.reg_signup_xpath).click()
        time.sleep(3)
        alert = self.driver.switch_to.alert
        time.sleep(4)
        alert.accept()
        time.sleep(4)
        print("Registration is successfull")
        
    @pytest.fixture
    def test_login(self,booting_function):
        
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(By.XPATH, value=project_m.Project_Data_1.login_xpath).click()
        time.sleep(2) 
        self.driver.find_element(By.XPATH, value=project_m.Project_Data_1.login_username_xpath).send_keys(project_m.Project_Data_2.username)
        time.sleep(2)        
        self.driver.find_element(By.XPATH, value=project_m.Project_Data_1.login_password_xpath).send_keys(project_m.Project_Data_2.password)
        time.sleep(2)  
        self.driver.find_element(By.XPATH, value=project_m.Project_Data_1.reg_login_xpath).click()
        time.sleep(8)
        s4=self.driver.find_element(By.XPATH,value=project_m.Project_Data_1.welcome_xpath)
        if s4.is_displayed():
            print("User is logged in successfully")
        
    def test_selection(self,booting_function,test_login):
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(By.XPATH, value=project_m.Project_Data_1.phone_xpath).click()
        time.sleep(4) 
        self.driver.find_element(By.XPATH, value=project_m.Project_Data_1.nokia_xpath).click()
        time.sleep(4) 
        self.driver.find_element(By.XPATH, value=project_m.Project_Data_1.addtocart_xpath).click()
        time.sleep(4)
        alert_1 = self.driver.switch_to.alert
        a1 = alert_1.text
        alert_1.accept()
        if a1 == "Product added.":
            print("Product is added to the cart successfully")
        time.sleep(3)
        
    def test_order_logout(self,booting_function,test_login):
        
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(By.XPATH, value=project_m.Project_Data_1.cart_xpath).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, value=project_m.Project_Data_1.place_order_xpath).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, value=project_m.Project_Data_1.name_xpath).send_keys(project_m.Project_Data_2.name)
        time.sleep(4)
        self.driver.find_element(By.XPATH, value=project_m.Project_Data_1.country_xpath).send_keys(project_m.Project_Data_2.country)
        time.sleep(4)
        self.driver.find_element(By.XPATH, value=project_m.Project_Data_1.city_xpath).send_keys(project_m.Project_Data_2.city)
        time.sleep(4)
        self.driver.find_element(By.XPATH, value=project_m.Project_Data_1.creditcard_xpath).send_keys(project_m.Project_Data_2.credit_card)
        time.sleep(4)
        self.driver.find_element(By.XPATH, value=project_m.Project_Data_1.month_xpath).send_keys(project_m.Project_Data_2.month)
        time.sleep(4)
        self.driver.find_element(By.XPATH, value=project_m.Project_Data_1.year_xpath).send_keys(project_m.Project_Data_2.year)
        time.sleep(4) 
        self.driver.find_element(By.XPATH, value=project_m.Project_Data_1.purchase_button_xpath).click() 
        time.sleep(6) 
        textt=self.driver.find_element(By.XPATH, value=project_m.Project_Data_1.purchase_xpath).text 
        self.driver.find_element(By.XPATH, value=project_m.Project_Data_1.ok_xpath).click() 
        time.sleep(5)
        if textt == 'Thank you for your purchase!':
            print("Item is purchased")
        time.sleep(3)
        self.driver.find_element(By.XPATH, value=project_m.Project_Data_1.logout_xpath).click() 
        time.sleep(9)
        s7 = self.driver.find_element(By.XPATH, value=project_m.Project_Data_1.login_xpath).text
        if s7 == 'Log in':
            print("User is logged out")
        
        
        
        
        
        
        
        