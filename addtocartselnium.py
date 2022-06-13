import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\ChromeDriver\\chromedriver.exe")
driver.get("https://www.flipkart.com/search?q=vivomobiles&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_4_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_4_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=vivomobiles&requestId=daf21a4b-abc8-45c9-afa0-435043973dfb&as-backfill=on")
time.sleep(3)
driver.maximize_window()
driver.find_element_by_xpath("//input[@class='_3704LK']").click()
driver.find_element_by_xpath("//button[@class='L0Z3Pu']").click()
driver.find_element_by_xpath("//img[@class='_396cs4 _3exPp9']").click()

ChildWindow = driver.window_handles[1]
driver.switch_to.window(ChildWindow)
time.sleep(5)
driver.find_element_by_xpath("//button[@class='_2KpZ6l _2U9uOA _3v1-ww']").click()