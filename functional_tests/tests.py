from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
class NewVisitorTest(LiveServerTestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_calculate(self):  
         

        self.browser.get(self.live_server_url)

        self.assertIn('Calculator', self.browser.title)  


        x = self.browser.find_element_by_id('x')
        x.send_keys('70')

        y = self.browser.find_element_by_id('y')  
        y.send_keys('7')    

        add=self.browser.find_element_by_id('add')
        add.send_keys(Keys.ENTER)



        x.send_keys('70') # ทำการใส่ค่าใหม่เนื่องจากหลังกดคำนวณ เลขในช่อง x,yจะหายไป
        y.send_keys('7')
        sub=self.browser.find_element_by_id('sub')
        sub.send_keys(Keys.ENTER) 

        x.send_keys('70') # ทำการใส่ค่าใหม่เนื่องจากหลังกดคำนวณ เลขในช่อง x,yจะหายไป
        y.send_keys('7')
        mul=self.browser.find_element_by_id('mul')
        mul.send_keys(Keys.ENTER)

        x.send_keys('70') # ทำการใส่ค่าใหม่เนื่องจากหลังกดคำนวณ เลขในช่อง x,yจะหายไป
        y.send_keys('7')
        div=self.browser.find_element_by_id('div')
        div.send_keys(Keys.ENTER)
        
        time.sleep(10)
        self.fail('Finish the test!')  

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  