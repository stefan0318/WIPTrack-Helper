from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from config import CREDENTIALS_FILE_PATH


# Username = admin
# Password = admin
# Operator Number = 0000

# Open the file and read the contents
with open(CREDENTIALS_FILE_PATH, "r") as f:
    credentials = {}
    for line in f:
        # Split each line at the '=' sign
        if "=" in line:
            key, value = line.strip().split("=", 1)  # Split into key and value
            credentials[key.strip()] = value.strip()  # Strip whitespace

username: str = credentials.get("Username")  # type: ignore
password: str = credentials.get("Password")  # type: ignore
operator_number: str = credentials.get("Operator Number")  # type: ignore


def wiptrack_login(driver: webdriver.Edge):
    driver.get(
        "http://10.10.100.112/WIPtrac/index.cfm?ScreenAvailHeight=1040&ScreenAvailWidth=1920&isMobile=1"
    )

    driver.find_element(By.ID, "UserName").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)

    driver.find_element(By.XPATH, "//input[@value='LOGIN']").click()


def click_process_work(driver: webdriver.Edge):
    driver.find_element(By.XPATH, "//img[@title='PROCESS WORK']").click()


def find_and_click_lot(driver: webdriver.Edge, lot_number: str):
    driver.find_element(By.ID, "LotID").send_keys(lot_number)
    driver.find_element(By.XPATH, "//input[@type='Submit']").click()
    # elements = driver.find_elements(By.XPATH, "//a[contains(@onclick, 'popUp')]")

    # for element in elements:
    #     on_click_attribute = element.get_attribute("onclick")
    #     if f"LotID={lot_number}" in on_click_attribute:
    #         element.click()
    #         break
    time.sleep(1)
    # driver.close()
    # driver.switch_to.window(driver.window_handles[0])


def log_in_and_find_wiptrack_lot(lot_number: str) -> webdriver.Edge:
    driver = webdriver.Edge()
    wiptrack_login(driver)
    click_process_work(driver)
    find_and_click_lot(driver, lot_number)
    return driver
