from seleniumbase.fixtures.base_case import BaseCase
from common.login_page import MyTest
from common.Element_API import WeiGeLi, ComoonPagee, RuoMimaPage, SuoYouZhuJi, AnquanJiXianElt
from selenium.common.exceptions import NoSuchElementException
import time
import re
import datetime


class Anquanjixian(BaseCase):
    # 终端tab
    # list_fenzu = [ComoonPagee.xuanzeweifenzu_zhongduan, ComoonPagee.xuanzeweifenzu_zhongduan,
    #               ComoonPagee.xuanzewindowfenzu,
    #               ComoonPagee.xuanzewindowzifenzu, ComoonPagee.xuanzelinuxfenzu,
    #               ComoonPagee.xuanzelinuxzifenzu]H
    # 下方策略的时间
    xiafacelv_time = None

    # 策略名称
    # list_celvmingcheng = ['linux_未分组', 'windows_未分组', 'windows_分组', 'windows_子分组', 'linux_分组', 'linux_子分组']

    def chuangjian(self, dr,celvmingcheng,fenzumingcheng,moban):
        #MyTest().admin_loggin(dr)
        dr.click(ComoonPagee.fengxiangguanl_tab)  # 点击风险管理tab
        dr.click(ComoonPagee.anquan_jixian_tab)  # 点击安全基线tab

        dr.click(AnquanJiXianElt.AnQuanjixian_celv_tab)  # 选择安全策略
        dr.click(AnquanJiXianElt.XinZen_bnt)  # 点击新增按钮
        dr.send_keys(AnquanJiXianElt.Celuve_mingcheng_input, fenzumingcheng)  # 策略名称
        dr.click(AnquanJiXianElt.yingyong_moban_select)  # 应用模板下拉框

        #dr.click(AnquanJiXianElt.yingyonnmoban_wintab)  # 选择win模板

        dr.click(moban)  # 选择win模板

        dr.double_click(AnquanJiXianElt.tianjia_bnt)  # 添加执行目标
        dr.click(celvmingcheng)  # 添加分组
        dr.click(ComoonPagee.quedingxuanze_bnt)  # 确定添加执行目标
        dr.click(AnquanJiXianElt.queding_xinzenganquan)  # 确定添加策略
        dr.click(AnquanJiXianElt.quedingbaocun_jixian)  # 确定保存基线策略
        dr.click(AnquanJiXianElt.xiafa_bnt)  # 点击下发按钮
        loca_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 获取下发策略的时间
        time.sleep(2)
        dr.xiafacelv_time = datetime.datetime.strptime(loca_time, '%Y-%m-%d %H:%M:%S')  # 时间格式化

    def check(self,dr):
        #MyTest().admin_loggin(dr) #此处不用重新登陆
        dr.click(ComoonPagee.zichanguanl_tab)  # 点击资产管理标签
        dr.click(ComoonPagee.suoyouzhuji_tab)  # 点击所有主机
        # dr.refresh()
        dr.click(SuoYouZhuJi.xianshilie)  # 点击显示列
        dr.double_click(SuoYouZhuJi.qingchusuoyou)  # 双击清除所有列
        dr.click(SuoYouZhuJi.xuanzejixiancelv_tab)  # 点击显示基线策略
        dr.click(SuoYouZhuJi.queding_xuanxiang, timeout=10)  # 点击确定

        loca_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        time.sleep(2)
        dr.xiafacelv_time = datetime.datetime.strptime(loca_time, '%Y-%m-%d %H:%M:%S')
        # 开始获取版本信息
        while True:
            check_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 获取当前时间
            check_timestr = datetime.datetime.strptime(check_time, '%Y-%m-%d %H:%M:%S')  # 获取的时间格式化
            resutlt = (check_timestr - dr.xiafacelv_time).seconds  # 将时间差转换为秒
            dr.refresh()  # 刷新浏览器
            time.sleep(2)  # 休眠时间
            if resutlt <= 3600:  # 如果时间差小于3600
                version_num = dr.find_elements(SuoYouZhuJi.ceilv_zhuangtai_text)  # 获取一组元素list返回
                for i in version_num:  # 循环每个元素，取出title值
                    version = (i.get_attribute('title'))
                    res = re.findall(r'\d+', version)  # 处理结果，只取当前版本和最新版本号
                    if res[0] != res[1]:  # 如果版本不相同跳出循环，进行下一次比较
                        break  # 跳出for循环，进入wile循环。
                    if res[0] == res[1]:
                        if i == version_num[-1]:  # 如果比较的元素时列表中的最后一个元素，那么证明，所有元素的值都相等，这时返回比较结果。
                            print("比较完毕，结果一样", res[0], res[1])
                            return dr.assert_equal(res[0], res[1], msg="比较完毕")

            if resutlt > 3600:
                return dr.assert_equal(1, 2, msg="超时了，比较失败")  # 如果超时直接判断为失败

    def check_data(self,dr):
        str=[]
        #MyTest().admin_loggin(dr)
        #dr.click(ComoonPagee.fengxiangguanl_tab)  # 点击风险管理tab
        #dr.click(ComoonPagee.anquan_jixian_tab)  # 点击安全基线tab
        dr.click(AnquanJiXianElt.AnQuanjixian_pinggu_tab) #点击安全基线评估
        a=dr.find_elements("//td/div")
        for i in a:
            result=i.text
            if u'\u4e00' <= result <= u'\u9fff': #如果包含中文则存储在列表里
                str.append(result)
        print(str)
