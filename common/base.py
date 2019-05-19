from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xlrd


class Base():
    def __init__(self,driver):
        self.driver = driver

    def open(self,url):
        self.driver.get(url)

    def findelement(self,loc):#定位单个元素
        '''
        :param loc: 是一个数组类型的参数，主要是元素的一个定位例，通过ID定位（“id“，kw””）
        :return: 返回定位到的元素
        '''
        element =WebDriverWait(self.driver,20).until(EC.presence_of_element_located(loc))
        return element

    def findelements(self,loc):
        elements = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(loc))
        return elements

    def sendKeys(self,loc,text,is_clear=True):
        if is_clear == True:
            self.findelement(loc).clear()
        self.findelement(loc).send_keys(text)

    def switchiframe(self,loc):
        fr = self.findelement(loc)
        # self.driver.switch_to_frame(fr)
        self.driver.switch_to.frame(fr)
    def click(self,loc):
        self.findelement(loc).click()





# if __name__ == '__main__':
#     driver = webdriver.Firefox()
#     b=Base(driver)
#     b.open(r"http://114.115.217.74:8080/gwth/")
#     u = ("id","username")
#     p = ("id","password")
#     b.sendKeys(u,"admin")
#     b.sendKeys(p,"admin")
