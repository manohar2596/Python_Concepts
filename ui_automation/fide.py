import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.fide.com/")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH, "(//a[@class='nav-link'])[2]").click()

time.sleep(2)
driver.execute_script("window.scrollBy(0, 1000);")

table = driver.find_element(By.ID, "top_rating_div")

rows = table.find_elements(By.TAG_NAME, "tr")[1:]

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    if len(cells) >= 4:
        name_cell = cells[1].text
        fed_cell = cells[2].text
        if fed_cell == "IND":
            print(f"The name associated with '{fed_cell}' in the Fed column is:", name_cell)

driver.quit()
