from common.base import Base
from common.ReadE import ReadE
url = r"http://114.115.217.74:8080/gwth/"
class Page(Base):
    u = ("id","username")#用户名
    p = ("id","password")#密码
    # button = ('css selector','input[type=submit]')#登录
    button = ("xpath","//form[@id='loginForm']/input[3]")  # 登录
    yanz = ("xpath","//div[@id='messageBox']/lable[2]")#验证码
    xtsz = ("link text","系统设置")#系统设置
    qygl = ("link text", "区域管理") # 区域管理
    frme = ("id","mainFrame")
    qytj = ("link text", "区域添加") # 区域添加
    qymc = ("id", "name") # 区域名称
    save = ("id", "btnSubmit") # 保存
    loginerr = ("id","loginError")

    def inputuname(self,text):#用户名
        self.sendKeys(self.u,text)

    def inputpwd(self,text):
        self.sendKeys(self.p,text)

    def clickbtn(self):
        self.click(self.button)
    def get_msg(self,n):
         yanzs = ("xpath","//div[@id='messageBox']/label[%s]"%n)#验证文本
         a = self.findelement(yanzs).text
         return a

    def clickxtsz(self):
        self.click(self.xtsz)

    def clickqygl(self):
        self.click(self.qygl)

    def swifrom(self):
        self.switchiframe(self.frme)

    def clickqytj(self):
        self.click(self.qytj)
    def clickqygl(self):
        self.click(self.qygl)

    def inputqymc(self,text):
        self.sendKeys(self.qymc,text)

    def clicksave(self):
        self.click(self.save)
