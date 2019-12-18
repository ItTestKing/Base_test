from seleniumbase.fixtures.base_case import BaseCase
from common.login_page import MyTest
from common.elements_base import MyElements
from common.Element_API import WeiGeLi, ComoonPagee, SuoYouZhuJi, XiTongPeiZhi, HeiBaiMingDan
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
import re


class HeiBaiMingdanPage(BaseCase):
    def black_file(self,dr):
        #MyTest().admin_loggin(dr)
        #dr.maximize_window()
        dr.click(XiTongPeiZhi.xitongpeizhi_tab)  # 点击系统配置标签
        dr.click(XiTongPeiZhi.heibaimingdan_tab)  # 点击黑白名单管理
        MyElements().elements_click(dr, HeiBaiMingDan.add_bnt)  # 点击黑白名单添加
        MyElements().elements_text_update(dr, HeiBaiMingDan.hash_input, 'BAACA87FE5AC99E0F144eB54E030562f')  # 输入哈希值
        MyElements().elements_text_update(dr, HeiBaiMingDan.note_input, "这个是瞎填的")  # 输入备注
        MyElements().elements_click(dr, HeiBaiMingDan.primary_btn)  # 点击确定按钮
        MyElements().elements_click(dr, HeiBaiMingDan.reprimary_btn)  # 再次确认
        time.sleep(1)

    def white_file(self,sb):

        #MyTest().admin_loggin(self)
        #self.maximize_window()
        sb.click(XiTongPeiZhi.xitongpeizhi_tab)  # 点击系统配置标签
        sb.click(XiTongPeiZhi.heibaimingdan_tab)  # 点击黑白名单管理
        sb.click(HeiBaiMingDan.file_white_tab) #文件白名单标签
        MyElements().elements_click(sb, HeiBaiMingDan.add_bnt)  # 点击黑白名单添加
        MyElements().elements_text_update(sb, HeiBaiMingDan.hash_input,
                                          'BAACA87FE5AC99E0F1442B5ff03056Ff')  # 输入哈希值
        MyElements().elements_text_update(sb, HeiBaiMingDan.note_input, "这个是瞎填的")  # 输入备注
        MyElements().elements_click(sb, HeiBaiMingDan.primary_btn)  # 点击确定按钮
        MyElements().elements_click(sb, HeiBaiMingDan.reprimary_btn)  # 再次确认
        time.sleep(1)





    def test_black_certificate(self,):
        MyTest().admin_loggin(self)
        self.maximize_window()
        self.click(XiTongPeiZhi.xitongpeizhi_tab)  # 点击系统配置标签
        self.click(XiTongPeiZhi.heibaimingdan_tab)  # 点击黑白名单管理
        self.click(HeiBaiMingDan.file_certificate_tab) #文件白名单标签
        MyElements().elements_click(self, HeiBaiMingDan.certificate_add)  # 点击黑白名单添加
        MyElements().elements_text_update(self, HeiBaiMingDan.certificate_hash_input,
                                          'ba 28 b5 f1 21 f6 78 ae f6 ac ac 96 be 91 8c d0 a8 b1 86 ff')  # 输入哈希值
        MyElements().elements_text_update(self, HeiBaiMingDan.certificate_note_input, "这个是瞎填的")  # 输入备注
        #MyElements().elements_click(self,HeiBaiMingDan.certificate_trust) #信任文件
        MyElements().elements_click(self, HeiBaiMingDan.certificate_primary_btn)  # 点击确定按钮
        MyElements().elements_click(self, HeiBaiMingDan.reprimary_btn)  # 再次确认
        time.sleep(1)