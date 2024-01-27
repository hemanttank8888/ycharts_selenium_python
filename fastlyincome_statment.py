import json
import time
from selenium import webdriver
from selenium.webdriver import Keys
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
load_dotenv()

symbols=["AAPL","PAG","FSLY"]
main_json={}
for symbol in symbols:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    URL = f"https://ycharts.com/companies/{symbol}/financials/income_statement/1"
    driver
    driver.get(URL)
    sing_up = driver.find_element(By.XPATH, "//a[contains(text(),'Sign In')]").click()

    input_email = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='id_username']"))
    )
    input_email.send_keys(os.getenv("email"))

    input_password = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='id_password']"))
    )
    input_password.send_keys(os.getenv("password"), Keys.ENTER)
    time.sleep(1)
    click_to_selection = driver.find_element(By.XPATH, "//label[contains(text(),'Format')]//following::a[@class='btn btn-block btn-secondary dropdown-toggle']").click()
    # time.sleep(1)
    # Quarterly = driver.find_element(By.XPATH, "//div[@class='dropdown-menu show']//label[1]//span[contains(text(), 'Quarterly')]").click()
    next_page=True
    number=0
    symbol_list=[]
    while next_page: 
        number+=1
        symbol_dict={}
        current_year_months = driver.find_elements(By.XPATH, '//div[@class="tab-pane active"]/div[3]//thead[1]/tr/td[@class="text-right colTxtShort"]')
        revenues = driver.find_elements(By.XPATH,'//div[@class="tab-pane active"]/div[3]//tbody/tr[2]/td[@class="text-right"]')
        try:
            symbol_dict["current_year_months"]=current_year_months[0].text
            symbol_dict["revenues"]=revenues[0].text
        except:
            symbol_dict["current_year_months"]=None
            symbol_dict["revenues"]=None
        symbol_list.append(symbol_dict)
        symbol_dict={}
        
        try:
            symbol_dict["current_year_months"]=current_year_months[1].text
            symbol_dict["revenues"]=revenues[1].text
        except:
            symbol_dict["current_year_months"]=None
            symbol_dict["revenues"]=None
        symbol_list.append(symbol_dict)
        symbol_dict={}
        
        try:
            symbol_dict["current_year_months"]=current_year_months[2].text
            symbol_dict["revenues"]=revenues[2].text
        except:
            symbol_dict["current_year_months"]=None
            symbol_dict["revenues"]=None
        symbol_list.append(symbol_dict)
        symbol_dict={}
        
        try:
            symbol_dict["current_year_months"]=current_year_months[3].text
            symbol_dict["revenues"]=revenues[3].text
        except:
            symbol_dict["current_year_months"]=None
            symbol_dict["revenues"]=None
        symbol_list.append(symbol_dict)
        symbol_dict={}
        
        try:
            symbol_dict["current_year_months"]=current_year_months[4].text
            symbol_dict["revenues"]=revenues[4].text
        except:
            symbol_dict["current_year_months"]=None
            symbol_dict["revenues"]=None
        symbol_list.append(symbol_dict)
        symbol_dict={}
        
        try:
            symbol_dict["current_year_months"]=current_year_months[5].text
            symbol_dict["revenues"]=revenues[5].text
        except:
            symbol_dict["current_year_months"]=None
            symbol_dict["revenues"]=None
        symbol_list.append(symbol_dict)
        symbol_dict={}
        
        try:
            symbol_dict["current_year_months"]=current_year_months[6].text
            symbol_dict["revenues"]=revenues[6].text
        except:
            symbol_dict["current_year_months"]=None
            symbol_dict["revenues"]=None
        symbol_list.append(symbol_dict)
        symbol_dict={}
        
        try:
            symbol_dict["current_year_months"]=current_year_months[7].text
            symbol_dict["revenues"]=revenues[7].text
        except:
            symbol_dict["current_year_months"]=None
            symbol_dict["revenues"]=None
        symbol_list.append(symbol_dict)
        symbol_dict={}
        

        revenues = driver.find_element(By.XPATH,"//div[@class='container']//div[@class='panel-pagination-content']//div[@class='btn btn-secondary'][2]/span/a[1]")
        prev = driver.find_element(By.XPATH,"//div[@class='container']//div[@class='panel-pagination-content']//div[@class='btn btn-secondary'][2]/span/a[1]")
        
        if "PREV" in prev.text:
            revenues.click()
        else:
            break
        if number==4:
            break
    main_json[symbol]=symbol_list
json_data = json.dumps(main_json, indent=4)
with open("final_output.json", 'w') as file:
    file.write(json_data)
