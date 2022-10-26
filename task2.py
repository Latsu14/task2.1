
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time 

def test_steam_login():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

    driver.get("https://store.steampowered.com/")

    assert driver

    driver.implicitly_wait(5)

    login_button = driver.find_element(by=By.CLASS_NAME, value="global_action_link").click()
    
    
    driver.implicitly_wait(5)


    user_box = driver.find_element(by=By.CLASS_NAME, value="newlogindialog_TextInput_2eKVn").send_keys("alex")


    pass_box = driver.find_element(by=By.XPATH, value='//*[@id="responsive_page_template_content"]/div/div[1]/div/div/div/div[2]/div/form/div[2]/input').send_keys('latsu')


    driver.implicitly_wait(5)

    submit_button = driver.find_element(by=By.CLASS_NAME, value="newlogindialog_SubmitButton_2QgFE").click()


    error_text = driver.find_element(by=By.CLASS_NAME, value="newlogindialog_FormError_1Mcy9")

    value = error_text.text

    assert type(value) == str

    driver.quit()





    

