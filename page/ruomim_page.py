from selenium.webdriver.common.keys import Keys
from seleniumbase.fixtures.base_case import BaseCase
from common.login_page import MyTest
from common.Element_API import WeiGeLi, ComoonPagee, RuoMimaPage, SuoYouZhuJi
from selenium.common.exceptions import NoSuchElementException
import time
import datetime
import re


class RuoMima(BaseCase):
    # 终端tab
    xiafacelv_time = None
    # 分组tab
    list_fenzu = [ComoonPagee.xuanzeweifenzu_zhongduan, ComoonPagee.xuanzewindowfenzu,
                  ComoonPagee.xuanzewindowzifenzu, ComoonPagee.xuanzelinuxfenzu,
                  ComoonPagee.xuanzelinuxzifenzu]
    # 终端tab
    zhonguan_tab = ['终端tab', ComoonPagee.zhongduan_mingcheng_bnt, ComoonPagee.zhongudan_xuanze_span,
                    ComoonPagee.xuanzzhongduan_tab]

    def chuangjian_fenzu_celv(self, dr, fenzu, fenzumingcheng):
        # 选择分组下发策略
        #MyTest().admin_loggin(dr)
        dr.click(ComoonPagee.fengxiangguanl_tab)  # 风险管理tab
        dr.click(ComoonPagee.ruomim_jiance_tab)  # 弱密码检测tab
        dr.click(RuoMimaPage.xinzen_bnt)  # 点击新增按钮
        dr.send_keys(RuoMimaPage.jihuamingchen_input, fenzumingcheng)  # 输入弱密码计划名称
        dr.click(RuoMimaPage.mimazidian_select)
        dr.click(RuoMimaPage.xitongquanliang_tab)  # 选择系统全量
        nowtime = datetime.datetime.now() + datetime.timedelta(hours=1,
                                                               minutes=3)  # 获取当前时间，加一个小时，加三分钟，因为下拉框是从00开始的所以时间需要加1个小时。
        times = nowtime.strftime("%H:%M")  # 格式化时间，只取时分

        dr.click(RuoMimaPage.zhixingshijian_input)  # 点击时间输入控件
        dr.find_element(RuoMimaPage.zhixingshijian_input).send_keys(Keys.CONTROL, "a")  # 删除默认时间
        dr.find_element(RuoMimaPage.zhixingshijian_input).send_keys(Keys.DELETE)  # 删除默认时间
        dr.click(RuoMimaPage.zhixingshijian_input)  # 点击时间输入控件
        # dr.send_keys(RuoMimaPage.zhixingshijian_input,times) 此处无法输入只能点击下拉选择框所以采用别的方式。
        dr.click(
            "//div[contains(text(),'弱密码策略')]/../..//div[2]/div[5]/div[15]/div[2]/div/div[2]/div/div/div/div/div/div[1]")  # 点击下拉选择框
        dr.scroll_click(
            "//div[contains(text(),'弱密码策略')]/../..//div[2]/div[5]/div[15]/div[2]/div/div[2]/div/div/div/div/div/div[1]/ul/li[{}]".format(
                times[0:2]))  # 输入时
        dr.click(
            "//div[contains(text(),'弱密码策略')]/../..//div[2]/div[5]/div[15]/div[2]/div/div[2]/div/div/div/div/div/div[2]")  # 点击下拉选择框
        dr.scroll_click(
            "//div[contains(text(),'弱密码策略')]/../..//div[2]/div[5]/div[15]/div[2]/div/div[2]/div/div/div/div/div/div[2]/ul/li[{}]".format(
                times[3:5]))  # 输入分

        dr.double_click(RuoMimaPage.tianj_zhixiangmubiao_bnt)  # 添加执行目标
        dr.click(fenzu)  # 选择终端分组
        dr.click(ComoonPagee.quedingxuanze_bnt)  # 确定选择终端分组
        dr.click(RuoMimaPage.quedingtianjia_mimacelv_bnt)  # 确定添加策略
        loca_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        dr.xiafacelv_time = datetime.datetime.strptime(loca_time, '%Y-%m-%d %H:%M:%S')

    def check(self, dr):
        #######################
        #     检查主机页面的版本
        #
        #
        # MyTest().admin_loggin(dr)
        dr.click(ComoonPagee.zichanguanl_tab)  # 点击资产管理标签
        dr.click(ComoonPagee.suoyouzhuji_tab)  # 点击所有主机
        dr.click(SuoYouZhuJi.xianshilie)  # 点击显示列
        dr.double_click(SuoYouZhuJi.qingchusuoyou)  # 双击清除所有列
        dr.click(SuoYouZhuJi.xuanzeruomima_tab)  # 点击显示弱密码策略
        dr.click(SuoYouZhuJi.queding_xuanxiang, timeout=10)  # 点击确定
        # 测试时使用
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
                            print("比较完毕，结果一样")
                            return dr.assert_equal(res[0], res[1], msg="比较完毕")

            if resutlt > 3600:
                return dr.assert_equal(1, 2, msg="超时了，比较失败")  # 如果超时直接判断为失败

    def check_data(self, dr):
        str = []
        # MyTest().admin_loggin(selfdr) #登陆方法
        #dr.click(ComoonPagee.fengxiangguanl_tab)  # 检测防护tab
        dr.click(ComoonPagee.ruomim_jiance_tab)  # 点击威胁防护tab
        dr.click(RuoMimaPage.ruomima_rizhi_tab)  # 弱密码检测日志
        a = dr.find_elements("//td/div")
        for i in a:
            result = i.text

            str.append(result)
            # if u'\u4e00' <= result <= u'\u9fff': #如果包含中文则存储在列表里
            #     str.append(result)
        print(str)
        return str
