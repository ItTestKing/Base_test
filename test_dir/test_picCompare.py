import json
import time

import pytest
from data import conf
from common.login_page import MyTest
import datetime
import os
from common.scree_you_self import ScreenPng
from common.compare_image import Compare


def get_data(path):
    data = []
    with open(path, 'r', encoding='utf8') as f:
        dict_data = json.load(f)
        for i in dict_data:
            data.append(tuple(i.values()))
    return data


@pytest.mark.usefixtures("sb")
class Test_PicCp(object):
    nowtime = datetime.datetime.now()
    times = nowtime.strftime("%Y_%m_%d %H:%M:%S")

    start = (0, 0)
    stop = (100, 100)

    # ScreenPng().screen_image(start, url,name, 1600, 850, stop)

    def file_compare(self, sb, base_png, run_png, png_name):

        if not os.path.exists(base_png):
            sb.sleep(2)
            sb.save_screenshot(base_png[14:-4], base_png[0:13])  # 前面是名字后面是路径
            # ScreenPng().screen_image(self.start,Compare_png[0:13],Compare_png[14:-4],1600,850,self.stop ) #前面是名字后面是路径

        else:
            sb.sleep(2)
            sb.save_screenshot(run_png[7:-4], run_png[0:7])
            # ScreenPng().screen_image(self.start, png[0:7], png[7:-4], 1600, 850, self.stop)
            sb.assert_equal(Compare().compare_image(base_png, run_png,png_name), True, png_name)
            # sb.assert_equal(Compare().compare_image(self.path_pic+png_name+".png", self.path_compic+png_name+".png"), True, png_name)

    def is_login(self, sb, tab):
        if sb.get_current_url() == conf.every_tab[tab]:
            pass
        if sb.get_current_url() != conf.every_tab[tab]:
            MyTest().admin_loggin(sb)
            sb.open(conf.every_tab[tab])

    # def test_a(self, sb):
    #     MyTest().admin_loggin(sb)

    @pytest.mark.parametrize('tab,png_name', get_data("../data/pic.json"))
    def test_compare(self, sb, tab, png_name, version=32):
        list = ["文件执行主机分析", "网络访问主机分析", "已知未注册主机", "Linux漏洞", "检查项安全评估", "安全基线策略", "安全基线模板", "弱密码字典管理", "弱密码检测日志",
                "弱密码执行日志", "规则库", "网站后门检测日志", "网站后门执行日志", "系统服务", "系统账户", "Linux资源使用检查", "异常信息", "关键文件", "系统配置检查",
                "系统配置变化轨迹", "通信对象管理", "端口对象管理", "账号登录日志", "网络威胁日志", "操作日志", "重要通知日志", "文件白名单", "证书黑白名单", "信任行为", "信任文件",
                "发起攻击"]
        sb.open(conf.every_tab[tab])
        self.is_login(sb, tab)  # 判断有没有登录
        if version == 30:

            if tab == "网络威胁日志" or tab == "系统威胁日志":
                print("32版本标签")

            else:
                if png_name in list:
                    sb.click("//div[contains(text(),'{}')]".format(png_name))
                Compare_png = "../comparePic/{}_default.png".format(png_name)
                png = "../pic/{}.png".format(png_name)
                self.file_compare(sb, Compare_png, png)

        if version == 32:
            if tab == "威胁事件日志":
                print("30版本标签")
            else:
                if png_name in list:
                    if png_name == "网络威胁日志":
                        pass
                    else:
                        sb.click("//div[contains(text(),'{}')]".format(png_name))
                base_png = r"../pic/base_png/{}_default.png".format(png_name)
                run_png = r"../pic/run_png/{}.png".format(png_name)
                self.file_compare(sb, base_png, run_png, png_name)
