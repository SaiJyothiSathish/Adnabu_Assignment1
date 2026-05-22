from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
print("Chrome browser opened successfully!")
driver.maximize_window()

mywait=WebDriverWait(driver,10) # explicit wait declaration # basic

driver.get("https://adnabu-store-assignment1.myshopify.com")
driver.maximize_window()
time.sleep(5)

search_item = "The Collection Snowboard: Liquid"

driver.find_element(By.ID, 'password').send_keys("AdNabuQA")
driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
driver.find_element(By.CSS_SELECTOR,"summary[aria-label='Search'] span").click()
driver.find_element(By.CSS_SELECTOR,"#Search-In-Modal").send_keys(search_item)
driver.find_element(By.XPATH,"//form[@class='search search-modal__form']//button[@aria-label='Search']//*[name()='svg']").click()
item = mywait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#CardLink--7801364742234")))
item.click()
addcart = mywait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#ProductSubmitButton-template--19850788667482__main")))
addcart.click()
youcart = mywait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='drawer__header']")))
mywait.until(EC.text_to_be_present_in_element((By.XPATH,"//a[@class='cart-item__name h4 break']"), search_item))
print(f"Success! '{search_item}' successfully added to cart.")
time.sleep(10)



# driver.quit()



