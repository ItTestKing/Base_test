import win32con
import win32gui

from common.Element_API import ComoonPagee, AnquanJiXianElt
from common.login_page import MyTest
from page.ruomim_page import RuoMima
from page.anquanjixian_page import Anquanjixian
from page.wangzhanhoumen_page import WangZhanHouMen
from page.xitongpeiz_page import XiTongpge
from page.heibaimingdan import HeiBaiMingdanPage
from page.weige_page import WeigeliPage
from page.fanghucelv_page import FangHuCelv
from page.suoyouzhuji_page import SuoYou
import pytest
import time
import re
import datetime
from common.compare_image import Compare


@pytest.mark.usefixtures("sb")
class Test_upatas(object):
    nowtime = datetime.datetime.now()
    times = nowtime.strftime("%Y_%m_%d %H:%M:%S")

    # def setup(self):
    #     sb = self.sb
    #     #MyTest().admin_loggin(sb)
    #     print("测试开始")
    def Sendfile(self, picpath):  # 传入图片路径

        dialog = win32gui.FindWindow('#32770', '打开')  # 对话框
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button

        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, picpath)  # 往输入框输入绝对地址
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button

    @pytest.mark.parametrize('value', ["linux"])
    def test_dashboard(self, sb, value):
        x = 0
        MyTest().master_logoin(sb)
        sb.open("https://10.11.64.244/master/mastMain.php?pageID=systemUpgrade")
        time.sleep(2)
        sb.click(".ivu-radio.ivu-radio-checked")
        elements = sb.find_elements(".ivu-btn.ivu-btn-primary")
        elements[1].click()
        sb.click(".ivu-btn.ivu-btn-default")
        sb.sleep(2)  # 此处需要休息两秒等待窗口打开。
        # win32gui
        self.Sendfile("D:\\upload\\installer-5.0.32.2105.bin")
        sb.sleep(2)
        sb.click(".ivu-btn.ivu-btn-default")
        for i in range(2):
            while (True):
                if not sb.is_element_visible(".ivu-btn.ivu-btn-default"):
                    sb.sleep(2)
                    x += 1
                if sb.is_element_visible(".ivu-btn.ivu-btn-default"):
                    sb.click(".ivu-btn.ivu-btn-default")
                    break
                if x == 10:
                    break
        print(sb.get_current_url())
        sb.sleep(5000)
