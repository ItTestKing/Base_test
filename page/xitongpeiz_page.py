from seleniumbase.fixtures.base_case import BaseCase
from common.login_page import MyTest
from common.elements_base import MyElements
from common.Element_API import WeiGeLi, ComoonPagee, SuoYouZhuJi, XiTongPeiZhi
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
import time
import re
import datetime


class XiTongpge(BaseCase):
    #################################################################################################
    #  旧的实验类
    # def elements_click(self, selectory):
    #     """探针卸载获得的class都是第一个
    #     #elements=dr.find_visible_elements(".ivu-btn.ivu-btn-primary.ivu-btn-large")#确定
    # """
    #
    #     try:
    #         elements = self.find_visible_elements(selectory[0])  # 确定
    #         if len(elements) == 1:  # 如果可见元素list的长度等于1
    #             elements[0].click()
    #         # if len(elements) >= selectory[1]: #如果可见元素list的长度大于预期值
    #         #     element = elements[selectory[1]]
    #         #     element.click()
    #         if 1 < len(elements) < selectory[1]:  # 如果可见元素大于1，小于预期值。
    #             elements = self.find_elements(selectory[0])
    #             element = elements[selectory[1]]
    #             element.click()
    #     except ElementNotVisibleException:
    #         print('没有这个元素！')
    #         self.assert_equal('', "页面上没有这个元素{}".format(selectory[0]))
    #
    # def elements_text_update(self, selectory, msg):
    #     """探针卸载获得的class都是第一个
    #     #elements=dr.find_visible_elements(".ivu-btn.ivu-btn-primary.ivu-btn-large")#确定
    # """
    #     # print(selectory)
    #     elements = self.find_visible_elements(selectory[0])  # 确定
    #     element = elements[selectory[1]]
    #     element.clear()
    #     element.send_keys(msg)
    #
    # def test_case(self):
    #     MyTest().admin_loggin(self)
    #     self.maximize_window()
    #     self.click(XiTongPeiZhi.xitongpeizhi_tab)  # 点击系统配置标签
    #     self.click(XiTongPeiZhi.canshushezhi_tab)  # 点击参数设置标签
    #     self.elements_text_update(XiTongPeiZhi.fenxiwenjian_input, '30')
    #     self.elements_text_update(XiTongPeiZhi.uninstall_passwrold, 'Mjs#201555')
    #     self.elements_click(XiTongPeiZhi.save_bant)
    #     self.elements_click(XiTongPeiZhi.primary_bant)  # 确定按钮

    def modify_config(self,dr,file_size,password):
       # MyTest().admin_loggin(dr)
       # dr.maximize_window()
       dr.click(XiTongPeiZhi.xitongpeizhi_tab)  # 点击系统配置标签
       dr.click(XiTongPeiZhi.canshushezhi_tab)  # 点击参数设置标签

       MyElements().elements_text_update(dr,XiTongPeiZhi.fenxiwenjian_input, file_size)
       MyElements().elements_text_update(dr,XiTongPeiZhi.uninstall_passwrold, password)
       MyElements().elements_click(dr,XiTongPeiZhi.save_bant)
       MyElements().elements_click(dr,XiTongPeiZhi.primary_bant)
       time.sleep(0.1)
