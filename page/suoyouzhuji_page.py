from seleniumbase.fixtures.base_case import BaseCase
from common.login_page import MyTest
from common.Element_API import ComoonPagee, RuoMimaPage, SuoYouZhuJi
from selenium.common.exceptions import NoSuchElementException
import time
import datetime
import re


class SuoYou(BaseCase):
    # 终端tab
    xiafacelv_time = None
    list_fenzu = [ComoonPagee.xuanzeweifenzu_zhongduan, ComoonPagee.xuanzewindowfenzu,
                  ComoonPagee.xuanzewindowzifenzu, ComoonPagee.xuanzelinuxfenzu,
                  ComoonPagee.xuanzelinuxzifenzu]

    def add_gruop(self,driver,value):
        fenzu_list = ['windows分组', 'linux分组']
        #MyTest().admin_loggin(driver)

        driver.click(ComoonPagee.zichanguanl_tab)  # 点击资产管理标签
        driver.click(ComoonPagee.suoyouzhuji_tab)  # 点击所有主机
        group=driver.find_elements(SuoYouZhuJi.gruop_name) #获取分组元素
        #此处判断分组是否存在
        for i in group:
            if value in i.text:
                return print("分组已存在")

        driver.click(SuoYouZhuJi.xinzen_bnt)  # 点击新增按钮
        driver.send_keys(SuoYouZhuJi.fenzumingcheng_input, value)# 输入分组名称
        driver.click(SuoYouZhuJi.queding_tianjia_bnt)  # 确定添加分组
        driver.click(SuoYouZhuJi.queding_baocun_bnt)  # 确定保存分组

        loca_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        time.sleep(2)
        self.xiafacelv_time = datetime.datetime.strptime(loca_time, '%Y-%m-%d %H:%M:%S')

    def check(self, dr, celvname):
        # flag = None
        list_vsion = []
        dr.click(SuoYouZhuJi.xianshilie)  # 点击显示列
        dr.double_click(SuoYouZhuJi.qingchusuoyou)  # 双击清除所有列
        dr.click(celvname)  # 点击显示策略标签
        dr.click(SuoYouZhuJi.queding_xuanxiang, timeout=10)  # 点击确定
        # 开始获取版本信息
        x = 0
        # while True:
        dr.refresh()  # 刷新
        version_num = dr.find_elements(SuoYouZhuJi.ceilv_zhuangtai_text)  # 获取一组元素list返回

        for i in range(int(len(version_num) / 3)):  # 除以3是为了去重
            version = (version_num[i].get_attribute('title'))
            # version = (i.text)
            res = re.findall(r'\d+', version)  # 处理结果，只取当前版本和最新版本号
            list_vsion.append(res)
            i += 1
            # if i == version_num[-1]:  # 如果比较的元素时列表中的最后一个元素，那么证明，所有元素的值都相等，这时返回比较结果。
        return list_vsion
