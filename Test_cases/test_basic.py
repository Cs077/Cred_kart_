class Test_001 :

    def test_01(self):
        a=29
        b=32
        print(f"sum of a+b{a+b}")
        assert a+b==61

    def test_02(self):
       assert True


    def test_03(self):
        assert True



    def test_04(self):
        import time

        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.select import Select
        from selenium.webdriver.support.wait import WebDriverWait

        driver = webdriver.Chrome()
        driver.get("https://automation.credence.in/shop")
        driver.maximize_window()

        driver.implicitly_wait(10)

        apl_btn = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[3]/div[1]/div[1]/a[2]/h3[1]")
        apl_btn.click()
        # time.sleep(5)

        '''al_btn=driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[4]/div[1]/div[1]/a[2]/h3[1]")
        al_btn.click()
        time.sleep(5)
        '''
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/form[1]/input[5]").click()
        # time.sleep(5)

        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/a[1]").click()
        # time.sleep(4)

        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[3]/div[1]/div[1]/a[2]/h3[1]").click()
        # time.sleep(3)

        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/form[1]/input[5]").click()
        # time.sleep(4)
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/a[2]").click()
        # time.sleep(5)

        driver.find_element(By.ID, "email").send_keys("debbiefoster@example.net")
        driver.find_element(By.ID, "password").send_keys("%z8FcCrZe^")
        driver.find_element(By.XPATH,
                            "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[4]/div[1]/button[1]").click()

        driver.find_element(By.ID, "first_name").send_keys("chetan")
        driver.find_element(By.ID, "last_name").send_keys("wadi")
        driver.find_element(By.ID, "phone").send_keys("9721529854")
        driver.find_element(By.ID, "address").send_keys("wadi niwas solapur maharashtra")
        driver.find_element(By.ID, "zip").send_keys("413006")
        dropdown = Select(driver.find_element(By.ID, "state"))

        # time.sleep(5)
        dropdown.select_by_index(1)

        # time.sleep(4)

        driver.find_element(By.ID, "owner").send_keys("Credence")

        driver.find_element(By.ID, "cvv").send_keys("257")

        card_number = driver.find_element(By.XPATH, "//input[@id='cardNumber']")
        card_number.send_keys("5281")
        card_number.send_keys("0370")
        card_number.send_keys("4891")
        card_number.send_keys("6168")

        Year_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='exp_year']"))
        Year_dropdown.select_by_visible_text("2026")

        # wait=WebDriverWait(driver,5)
        month_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='exp_month']"))
        month_dropdown.select_by_visible_text("May")
        # time.sleep(4)

        # wait=WebDriverWait(driver,5)
        driver.find_element(By.XPATH, "//button[@id='confirm-purchase']").click()
