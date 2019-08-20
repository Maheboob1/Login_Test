from selenium import webdriver
import time
driver=webdriver.Chrome("C:\\Users\\Ifra Fatimah\\Desktop\\driver\\Chrome\\chromedriver.exe")
driver.get("https://admin-demo.nopcommerce.com")
driver.find_element_by_id("Email").send_keys("admin@yourstore.com")
driver.find_element_by_id("Password").send_keys("admin")
driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/input").click()
time.sleep(5)
driver.close()