from data import conf
class MyTest(object):
    # 打开后台管理界面，输入账号密码，点击登陆。
    path =conf.WEB_SERVER_URL
    def admin_loggin(self,dr):
        #dr.open(self.path+"https://10.11.64.242/admin/majorSec.php?pageID=runtimeRisk")
        dr.open(self.path+"admin/majorSec.php?pageID=runtimeRisk")
        dr.maximize_window()
        dr.click("#btnAdmin")

        dr.send_keys("#userNmFake", "admin")
        dr.send_keys("#pwdFake", "Mjs#2015")
        dr.click("#btnLogin")

    # 打开master页面输入账号密码，点击登陆。
    def master_logoin(self,dr):
        dr.open(self.path+"master/login/login.php")
        dr.maximize_window()
        # self.click("#btnAdmin")
        dr.send_keys("input[autofocus='autofocus']", "Mjs#2015")
        # self.send_keys("#pwdFake","Mjs#2015")
        # dr.click(".btnExecClass.ivu-btn.ivu-btn-primary.ivu-btn-long")
        dr.click("button[type='button']")


