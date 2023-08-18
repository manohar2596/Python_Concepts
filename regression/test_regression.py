import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestNetflixRegression(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Replace with appropriate WebDriver
        self.driver.maximize_window()
        self.base_url = "https://www.netflix.com/"

    def tearDown(self):
        self.driver.quit()

    def test_login_and_verify_movie_duration(self):
        driver = self.driver

        # Open Netflix website
        driver.get(self.base_url)

        # Click on Sign In link
        login_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Sign In")))
        login_link.click()

        # Enter login credentials
        mail = driver.find_element(By.ID, "id_userLoginId")
        mail.send_keys("email")  # Provide your email
        password = driver.find_element(By.XPATH, "//input[@type='password']")
        password.send_keys("password")  # Provide your password

        submit = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        submit.click()

        # Click on the profile icon
        profile = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='profile-icon'])[1]")))
        profile.click()

        # Get movie duration
        movie_duration_element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='duration']")))
        movie_duration = movie_duration_element.text
        print("Actual Movie Duration:", movie_duration)

        # Assertions
        self.assertTrue("Movie Duration:" in movie_duration)


if __name__ == "__main__":
    unittest.main()
