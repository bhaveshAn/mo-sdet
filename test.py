import unittest
import time
import io
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_create_campaign(self):
        self.driver.get('https://app.moengage.com')
        wait = WebDriverWait(self.driver, 10)

        # get elements
        self.driver.find_element_by_xpath('//*[@id="signin-email"]').send_keys("moeautouser@gmail.com")
        self.driver.find_element_by_xpath('//*[@id="signin-password"]').send_keys('dosalike1!')
        screen = self.driver.get_screenshot_as_png()
        image = Image.open(io.BytesIO(screen))
        image.save('screenshots/1.png')
        self.driver.find_element_by_xpath('//*[@id="signin-container"]/div[2]/form[1]/div[3]/div/button').click()
        time.sleep(50)
        self.driver.find_element_by_xpath('//*[@id="nav"]/li[5]/a/span').click()
        time.sleep(10)
        self.driver.find_element_by_xpath('//*[@id="nav"]/li[5]/ul/li[2]/a/span').click()
        time.sleep(20)
        self.driver.find_element_by_xpath('//*[@id="tab-content-0"]/div/md-content/div[1]/div[1]/a/span').click()
        time.sleep(20)
        self.driver.find_element_by_xpath('//*[@id="ANDROID"]/div[1]').click()
        time.sleep(10)
        self.driver.find_element_by_xpath('//*[@id="radio_12"]').click()
        time.sleep(10)
        self.driver.find_element_by_xpath('//*[@id="steps-uid-0-p-0"]/md-content/div[3]/div[1]/segmentation-filter/form[1]/section/div/filter-generator/div[1]/div/div[2]/div/label[2]').click()
        time.sleep(5)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="steps-uid-0-p-0"]/md-content/div[3]/div[1]/segmentation-filter/form[1]/section/div/filter-generator/div[1]/div/div[3]/segmentation-event-generator/div/div[2]/div/a/span')))
        self.driver.find_element_by_xpath('//*[@id="steps-uid-0-p-0"]/md-content/div[3]/div[1]/segmentation-filter/form[1]/section/div/filter-generator/div[1]/div/div[3]/segmentation-event-generator/div/div[2]/div/a/span').click()
        select1 = Select(self.driver.find_element_by_xpath('//*[@id="steps-uid-0-p-0"]/md-content/div[3]/div[1]/segmentation-filter/form[1]/section/div/filter-generator/div[1]/div/div[3]/segmentation-event-generator/div/div[2]/select'))
        select1.select_by_value('5')
        select2 = Select(self.driver.find_element_by_css_selector('.my-box ng-valid ng-dirty ng-valid-parse ng-touched'))
        select2.select_by_visible_text('at most')
        self.driver.find_element_by_xpath('/md-content/div[3]/div[1]/segmentation-filter/form[1]/section/div/filter-generator/div[1]/div/div[3]/segmentation-event-generator/div[1]/div[4]/input').send_keys("2")
        select3 = Select(self.driver.find_element_by_xpath('//*[@id="steps-uid-0-p-0"]/md-content/div[3]/div[1]/segmentation-filter/form[1]/section/div/filter-generator/div[1]/div/div[3]/segmentation-event-generator/div[2]/div[1]/div/select'))
        select3.select_by_visible_text('after')
        self.driver.find_element_by_xpath('//*[@id="steps-uid-0-p-0"]/md-content/div[3]/div[1]/segmentation-filter/form[1]/section/div/filter-generator/div[1]/div/div[3]/segmentation-event-generator/div[2]/div[1]/div[2]/span/input').send_keys("14-March-2019")
        self.driver.find_element_by_xpath('//*[@id="steps-uid-0-p-0"]/md-content/div[3]/div[1]/segmentation-filter/form[1]/section/div/filter-generator/div[1]/div/div[3]/segmentation-event-generator/div[2]/div[2]/div[2]/button').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="steps-uid-0-p-0"]/md-content/div[3]/div[1]/segmentation-filter/form[1]/section/div/filter-generator/div[1]/div/div[3]/segmentation-event-generator/div[2]/div[2]/segmentation-event-attribute-generator/div/div[2]/div/div/div/input').send_keys('Platform')
        select4 = Select(self.driver.find_element_by_xpath('//*[@id="steps-uid-0-p-0"]/md-content/div[3]/div[1]/segmentation-filter/form[1]/section/div/filter-generator/div[1]/div/div[3]/segmentation-event-generator/div[2]/div[2]/segmentation-event-attribute-generator/div/div[3]/select'))
        select4.select_by_visible_text('starts with')
        self.driver.find_element_by_xpath('//*[@id="steps-uid-0-p-0"]/md-content/div[3]/div[1]/segmentation-filter/form[1]/section/div/filter-generator/div[1]/div/div[3]/segmentation-event-generator/div[2]/div[2]/segmentation-event-attribute-generator/div/div[4]/input').send_keys("and")
        screen = self.driver.get_screenshot_as_png()
        image = Image.open(io.BytesIO(screen))
        image.save('screenshots/2.png')
        self.driver.find_element_by_xpath('//*[@id="steps-uid-0"]/div[3]/ul/li[2]/a').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="tab-content-21"]/div/div[1]/div[2]/textarea').send_keys('@')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/mentio-menu[1]/ul/li[6]/a').click()
        self.driver.find_element_by_xpath('//*[@id="tab-content-18"]/div/md-content/div/div/md-content[2]/div/md-switch/div[1]/div[2]/div').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="tab-content-25"]/div/div[1]/div[2]/textarea').send_keys('anything')
        self.driver.find_element_by_xpath('//*[@id="tab-content-25"]/div/div[2]/div[2]/textarea').send_keys('anything')
        self.driver.find_element_by_xpath('//*[@id="tab-content-18"]/div/md-content/div/div/md-content[2]/md-tabs/md-tabs-wrapper/md-tabs-canvas/md-pagination-wrapper/md-tab-item[2]/i').click()
        select5 = Select(self.driver.find_element_by_xpath('//*[@id="tab-content-26"]/div/md-card/md-card-content/div[2]/div[2]/select'))
        select5.select_by_visible_text('Coupon')
        self.driver.find_element_by_xpath('//*[@id="coupon"]/div[2]/input').send_keys('anything')
        self.driver.find_element_by_xpath('//*[@id="tab-content-26"]/div/div/button/span').click()
        time.sleep(2)
        select6 = Select(self.driver.find_element_by_xpath('//*[@id="tab-content-26"]/div/md-card[2]/md-card-content/div[2]/div[2]/select'))
        select6.select_by_visible_text('Image')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="image"]/input').send_keys('https://app.moengage.com')
        screen = self.driver.get_screenshot_as_png()
        image = Image.open(io.BytesIO(screen))
        image.save('screenshots/3.png')
        self.driver.find_element_by_xpath('//*[@id="tab-content-18"]/div/md-content/div/div/md-content[1]/md-tabs/md-tabs-wrapper/md-tabs-canvas/md-pagination-wrapper/md-tab-item[3]/i').click()
        select7 = Select(self.driver.find_element_by_xpath('//*[@id="tab-content-20"]/div/md-card/md-card-content/div/div[2]/select'))
        select7.select_by_visible_text('Navigate to a screen')
        time.sleep(2)
        select8 = Select(self.driver.find_element_by_xpath('//*[@id="tab-content-20"]/div/md-card/md-card-content/div/div[2]/select'))
        select8.select_by_visible_text('Navigate to a screen')
        time.sleep(2)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="androidnavigation"]/div[1]/div[2]/div/a/span')))
        self.driver.find_element_by_xpath('//*[@id="androidnavigation"]/div[1]/div[2]/div/a/span').click()
        select9 = Select(self.driver.find_element_by_xpath('//*[@id="androidnavigation"]/div[1]/div[2]/select'))
        select9.select_by_value('com.moengage.demoapp.DemoScreen')
        self.driver.find_element_by_xpath('//*[@id="androidnavigation"]/div[2]/div[2]/div[1]/input').send_keys('name1')
        self.driver.find_element_by_xpath('//*[@id="androidnavigation"]/div[2]/div[2]/div[2]/input').send_keys('val1')
        self.driver.find_element_by_xpath('//*[@id="androidnavigation"]/div[2]/div[2]/div[4]/button').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="androidnavigation"]/div[2]/div[3]/div[1]/input').send_keys('name2')
        self.driver.find_element_by_xpath('//*[@id="androidnavigation"]/div[2]/div[2]/div[2]/input').send_keys('val2')
        self.driver.find_element_by_xpath('//*[@id="androidnavigation"]/div[2]/div[3]/div[4]/button/i').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="androidnavigation"]/div[2]/div[4]/div[1]/input').send_keys('name3')
        self.driver.find_element_by_xpath('//*[@id="androidnavigation"]/div[2]/div[4]/div[2]/input').send_keys('val3')
        screen = self.driver.get_screenshot_as_png()
        image = Image.open(io.BytesIO(screen))
        image.save('screenshots/4.png')
        self.driver.find_element_by_xpath('//*[@id="steps-uid-0"]/div[3]/ul/li[2]/a').click()
        mins = 0
        while mins <= 20:
            self.driver.find_element_by_xpath('//*[@id="steps-uid-0-p-2"]/md-content/div[1]/div/div[2]/table/tbody/tr[1]/td[3]/a/span').click()
            mins += 1
        screen = self.driver.get_screenshot_as_png()
        image = Image.open(io.BytesIO(screen))
        image.save('screenshots/5.png')
        self.driver.find_element_by_xpath('//*[@id="steps-uid-0"]/div[3]/ul/li[3]/a').click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
