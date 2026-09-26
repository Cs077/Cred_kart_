class Test_03:
    import time
    def test_login_hrm(self):
        from faker import Faker
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.select import Select

        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()

        driver.implicitly_wait(10)

        # time.sleep(5)
        """user_data=Faker().user_name()
        print(f"username-->{user_data}")

        pass_data=Faker().password()
        print(f"password-->{pass_data}")"""

        user_btn = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]/input[1]")
        user_btn.send_keys("Admin")

        # time.sleep(4)

        pas_btn = driver.find_element(By.NAME, "password")
        pas_btn.send_keys("admin123")

        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[3]/button[1]").click()
        # time.sleep(4)

        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/button[1]/*[name()='svg'][1]/*[name()='g'][1]/*[name()='path'][1]").click()
        # time.sleep(5)

        driver.back()

        # time.sleep(5)
        leav_btn = driver.find_element(By.XPATH,"//button[@title='Leave List']//*[name()='svg']//*[name()='g' and contains(@fill,'currentCol')]//*[name()='g'][1]")
        leav_btn.click()
        # time.sleep(5)
        """driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys("chetan wadi")
        time.sleep(5)

        #driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]").send_keys("CAN - Vacation")
        dropdow=Select(driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]"))
        dropdow.select_by_visible_text("CAN - Vacation")
        time.sleep(5)"""




