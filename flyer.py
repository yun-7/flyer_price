import time
import numpy as np
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Flyer():
    def catch_flyer(self):
        # 設定 Webdriver Options
        opt = webdriver.ChromeOptions()
        user_agent = UserAgent()
        opt.add_argument("--user-agent=%s" % user_agent)
        opt.add_argument("--window-size=1920,1080")
        opt.add_argument("--enable-javascript")
        #opt.add_argument("--headless")   # 啟用 headless 模式
        opt.add_argument("--disable-gpu")   # 測試關閉 GPU 避免某些錯誤出現
        

        driver = webdriver.Chrome(options=opt)
        driver.get('https://www.skyscanner.com.tw/')
        #driver.execute_script("alert('Hello, World!')")
        driver.maximize_window()
        print(driver.title)
        # 模擬用戶等待網站載入，每次都用隨機時間
        time.sleep(np.random.uniform(3, 5))

        destination = driver.find_element(By.XPATH, '//*[@id="destinationInput-label"]')
        destination.click()
        destination.send_keys('大阪關西國際 (KIX)')
        time.sleep(2)
        destination.send_keys(Keys.ENTER)

        # 點選直飛航班
        driver.find_element(By.XPATH, '//input[@name="prefer-directs"]').click()
        time.sleep(2)

        from_btn = driver.find_element(By.XPATH, '//button[@data-testid="depart-btn"]')
        from_btn.click()
        time.sleep(2)
        from_month = driver.find_elements(By.XPATH, "//div//h2[@class='BpkText_bpk-text__ZmFmY BpkText_bpk-text--heading-4__MTNhO CustomCalendar_monthName__MmVhY']")
        for month in from_month:
            if '9月' in month:
                from_date = driver.find_element(By.XPATH, "//div//button[@class='CustomCalendar_day__OWJhO']")
                for date in from_date:
                    print(date.text)
                time.sleep(2)
            else:
                driver.find_element(By.CLASS_NAME, 'CustomCalendar_nextBtn__ODA5Y').click()
                time.sleep(2)
                from_month = driver.find_elements(By.XPATH, "//div//h2[@class='BpkText_bpk-text__ZmFmY BpkText_bpk-text--heading-4__MTNhO CustomCalendar_monthName__MmVhY']")

        time.sleep(5)


flyer = Flyer()
flyer.catch_flyer()
