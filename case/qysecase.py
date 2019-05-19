from selenium import webdriver
from page.page import Page,url
from common.ReadE import ReadE
import time
import unittest
import ddt
d=ReadE()
data=d.Read_excel(r"H:\github\selenium-gwth\mc.xlsx")
print(data)
@ddt.ddt
class Qysz(unittest.TestCase):
    driver = webdriver.Firefox()
    ele = Page(driver)
    # driver.switch_to_frame()
    # driver.switch_to.frame()
    list1 = ["test01","test02","test03"]
    def setUp(self):
        self.ele.open(url)
        self.ele.inputuname("admin")
        self.ele.inputpwd("admin")
        time.sleep(2)
        self.ele.clickbtn()
    @unittest.skip("模块跳过")
    def testqy_01(self):
        self.ele.clickxtsz()#点击系统设置
        self.ele.clickqygl()#点击区域管理
        self.ele.swifrom()
        for i in self.list1:
            self.ele.clickqytj()
            self.ele.inputqymc(i)             #
            self.ele.clicksave()
            time.sleep(3)
    @ddt.data(*data)
    def testqy_xlrd(self,data):
        self.ele.clickxtsz()  # 点击系统设置
        self.ele.clickqygl()  # 点击区域管理
        self.ele.swifrom()
        self.ele.clickqytj()
        self.ele.inputqymc(data["name"])  #
        self.ele.clicksave()
        time.sleep(3)

    # def tearDown(self):
    #     self.driver.quit()

    @unittest.skip("不执行")  #跳过这个模块
    def testlogin_01(self):
        self.ele.inputuname("admin")
        self.ele.inputpwd("admin")
        self.ele.clickbtn()
        print(self.ele.get_msg("2"))
        self.assertEqual("yonghu",self.ele.get_msg("2"))
        # self.assertEqual("国网通航",self.driver.title)

if __name__ == '__main__':
    unittest.main()