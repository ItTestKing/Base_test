from seleniumbase.fixtures.base_case import BaseCase
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


@pytest.mark.usefixtures("sb")
class Test_State(object):
    nowtime = datetime.datetime.now()
    times = nowtime.strftime("%Y_%m_%d %H:%M:%S")
    fenzu_linux = ComoonPagee.xuanzelinuxfenzu
    fenzu_win = ComoonPagee.xuanzewindowfenzu
    fenzu_name_linux = "linux分组_{}".format(times)
    fenzu_name_win = "windows分组_{}".format(times)

    def setup(self):
        sb = self.sb
        MyTest().admin_loggin(sb)

    @pytest.mark.parametrize('value', ['window', "linux"])
    def test_addgruop(self, sb, value):
        SuoYou().add_gruop(sb, value)

    # 策略下发

    @pytest.mark.parametrize('value', [(ComoonPagee.xuanzelinuxfenzu, "linux_{}"),
                                       (ComoonPagee.xuanzewindowfenzu, "windows_{}")])
    def test_ruomfim(self, sb, value):
        # 弱密码策略下发
        RuoMima().chuangjian_fenzu_celv(sb, value[0], value[1].format(self.times))  # 下发策略

    @pytest.mark.parametrize('value',
                             [(ComoonPagee.xuanzelinuxfenzu, "linux_{}", AnquanJiXianElt.yingyonnmoban_linuxtab),
                              (ComoonPagee.xuanzewindowfenzu, "windows_{}", AnquanJiXianElt.yingyonnmoban_wintab)])
    def test_anquanjiaixna(self, sb, value):
        # 安全基线策略下发
        Anquanjixian().chuangjian(sb, value[0], value[1].format(self.times), value[2])

    @pytest.mark.parametrize('value', [(ComoonPagee.xuanzelinuxfenzu, "linux_{}", '/var/log'),
                                       (ComoonPagee.xuanzewindowfenzu, "windows_{}", 'C:\\222')])
    def test_wangzhanghoumen(self, sb, value):
        # 网站后门策略下发
        WangZhanHouMen().chuangjian(sb, value[1].format(self.times), value[0], value[2])

    @pytest.mark.parametrize('value', [(ComoonPagee.xuanzelinuxfenzu, "linux_{}"),
                                       (ComoonPagee.xuanzewindowfenzu, "windows_{}")])
    def test_weigeli(self, sb, value):
        # 创建安全域
        WeigeliPage().chuangjian_anquanyu(sb, value[1].format(self.times), value[0])
        # 创建对象
        WeigeliPage().chuangjian_duixiang(sb)
        # 创建入站规则
        WeigeliPage().cweigeli_ruzhan(sb)
        # 下发策略
        WeigeliPage().xiafacelv(sb)

    @pytest.mark.parametrize('value', [(ComoonPagee.xuanzelinuxfenzu, "linux_{}"),
                                       (ComoonPagee.xuanzewindowfenzu, "windows_{}")])
    def test_fanghucelv(self, sb, value):
        # 防护策略下发
        FangHuCelv().chuangjian(sb, value[1].format(self.times), value[0])

    @pytest.mark.parametrize('value', [('10', "Mjs#0aasdf"), ('20', "Mjs#2015333")])
    def test_set_config(self, sb, value):
        XiTongpge().modify_config(sb, value[0], value[1])
        sb.assert_element("//div[contains(text(),'系统参数配置保存成功')]")

    def test_BF_management(self, sb):
        HeiBaiMingdanPage().black_file(sb)

    def test_WF_management(self,sb):
        HeiBaiMingdanPage().white_file(sb)
        sb.find_visible_elements()
        sb.find_elements()