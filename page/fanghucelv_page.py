from seleniumbase.fixtures.base_case import BaseCase
from common.login_page import MyTest
from common.Element_API import WeiGeLi, ComoonPagee, WeiXieFanghu, SuoYouZhuJi
from selenium.common.exceptions import NoSuchElementException
import time
import re
import datetime
from common.elements_base import MyElements


class FangHuCelv(BaseCase):
    # 终端tab
    list_fenzu = [ComoonPagee.xuanzeweifenzu_zhongduan, ComoonPagee.xuanzewindowfenzu,
                  ComoonPagee.xuanzewindowzifenzu, ComoonPagee.xuanzelinuxfenzu,
                  ComoonPagee.xuanzelinuxzifenzu]
    xiafacelv_time = None

    def chuangjian(self, dr, celv_name,fenzu_name):

        #MyTest().admin_loggin(dr)
        dr.click(ComoonPagee.jianceyufanghu_tab)  # 检测防护tab
        dr.click(ComoonPagee.weixiefanghu_tab)  # 点击威胁防护tab
        dr.click(WeiXieFanghu.XinZen_bnt)  # 点击新增按钮
        dr.send_keys(WeiXieFanghu.celuve_mingcheng_input, celv_name)  # 策略名称
        dr.click(WeiXieFanghu.wangluoweixie_tab)  # 网络威胁标签
        dr.click(WeiXieFanghu.xinrenip_tianjia_bnt)  # 添加信任ip
        dr.send_keys(WeiXieFanghu.ip_qishi_input, '10.10.67.1')  # 输入ip
        dr.send_keys(WeiXieFanghu.ip_zhongzhi_input, '10.10.67.10')  # 输入ip
        dr.click(WeiXieFanghu.ipduan_queding_bnt)  # 确定添加ip
        dr.click(WeiXieFanghu.yingyongmubiao_tab)  # 应用目标标签
        #dr.click(WeiXieFanghu.tianj_bnt)  # 添加标签
        selectory=(".ivu-btn.ivu-btn-primary",19)
        MyElements().elements_click(dr,selectory) #添加按钮
        dr.click(fenzu_name)  # 添加未分组
        dr.click(WeiXieFanghu.queding_bnt)  # 目标确定
        fanbingdu_tab=(".ivu-tabs-tab",3)#反病毒引擎tab
        MyElements().elements_click(dr,fanbingdu_tab)

        time.sleep(1)
        qiyong_bnt=(".ivu-switch.ivu-switch-large",2)#启用按钮
        MyElements().elements_click(dr,qiyong_bnt)
        dr.click(WeiXieFanghu.quedng_tianjiacelv_bnt)  # 确定添加策略
        dr.click(WeiXieFanghu.quedng_baocuncelv_bnt)  # 确定保存防护策略
        loca_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 获取下发策略的时
        time.sleep(2)
        dr.xiafacelv_time = datetime.datetime.strptime(loca_time, '%Y-%m-%d %H:%M:%S')  # 时间格式化

    def check_celv(self,dr,fenuzu):
        # 此次暂时只是比较所有主机标签下的事件清单，将来要做成，选择分组，然后选择相应的终端。
        # MyTest().admin_loggin(dr)
        dr.click(ComoonPagee.zichanguanl_tab)  # 点击资产管理标签
        dr.click(ComoonPagee.suoyouzhuji_tab)  # 点击所有主机
        dr.refresh()
        qiwang_ip = ['10.10.67.1-10.10.67.10']  # 期望值
        ip_list = []
        dr.click(fenuzu)
        # dr.click("//*[@id='tableContent']/div/div/div[4]/div[2]/table/tbody/tr[{}]/td[2]/div/span/span")  # 此次是根据tr,选择不同的终端。
        dr.click(
            "//*[@id='tableContent']/div/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span/span")  # 此次是根据tr,选择不同的终端。
        dr.open_new_window()  # 打开新的窗口，此处会弹一个空白的窗口，暂不解决。
        dr.click(SuoYouZhuJi.yingyongce_tab)  # 应用策略标签
        dr.click(SuoYouZhuJi.wangluoweixie_tab)  # 点击网络威胁
        result = dr.get_text(SuoYouZhuJi.xinren_ip)
        ip_list.append(result)
        # print(result)
        time.sleep(5)
        dr.switch_to_default_window()
        print(ip_list)
        dr.assert_equal(ip_list, qiwang_ip, msg="测试通过")

    def check(self, dr):
        # MyTest().admin_loggin(dr)
        dr.click(ComoonPagee.zichanguanl_tab)  # 点击资产管理标签
        dr.click(ComoonPagee.suoyouzhuji_tab)  # 点击所有主机
        # dr.refresh()
        dr.click(SuoYouZhuJi.xianshilie)  # 点击显示列
        dr.double_click(SuoYouZhuJi.qingchusuoyou)  # 双击清除所有列
        dr.click(SuoYouZhuJi.xuanzefanghucelv_tab)  # 点击显示威胁防护策略
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
                    res = re.findall(r'\d+', version)  # 处理结果，只取当前版本和最新版本号,此处返回有四个值分别为：[20191025,130102,20191025,130102]
                    if res[1] != res[3]:  # 如果版本不相同跳出循环，进行下一次比较
                        break  # 跳出for循环，进入wile循环。
                    if res[1] == res[3]:
                        if i == version_num[-1]:  # 如果比较的元素时列表中的最后一个元素，那么证明，所有元素的值都相等，这时返回比较结果。
                            print("比较完毕，结果一样")
                            return dr.assert_equal(res[1], res[3], msg="比较完毕")

            if resutlt > 3600:
                return dr.assert_equal(1, 2, msg="超时了，比较失败")  # 如果超时直接判断为失败

        # a= dr.get_attribute(SuoYouZhuJi.ceilv_zhuangtai_text, 'title')  # 获取版本状态
        # print(a[6:20],a[-15:])
        # #dr.click(2)
        # dr.assert_equal(a[5:20],a[-15:],"比较所有基线策略版本是否相同")

##########################################################################################################################
# def test_achuangjians(self,dr):
#     MyTest().admin_loggin(dr)
#     dr.click(ComoonPagee.jianceyufanghu_tab)  # 检测防护tab
#     dr.click(ComoonPagee.weixiefanghu_tab)  # 点击威胁防护tab
#
#     for i in range(5):
#         dr.click(WeiXieFanghu.XinZen_bnt)  # 点击新增按钮
#         dr.send_keys(WeiXieFanghu.celuve_mingcheng_input, "test1111{}".format(i))  # 策略名称
#         dr.click(WeiXieFanghu.wangluoweixie_tab)  # 网络威胁标签
#         dr.click(WeiXieFanghu.xinrenip_tianjia_bnt)  # 添加信任ip
#         dr.send_keys(WeiXieFanghu.ip_qishi_input, '10.10.67.10')  # 输入ip
#         dr.send_keys(WeiXieFanghu.ip_zhongzhi_input, '10.10.67.10')  # 输入ip
#         dr.click(WeiXieFanghu.ipduan_queding_bnt)  # 确定添加ip
#         dr.click(WeiXieFanghu.yingyongmubiao_tab)  # 应用目标标签
#         dr.click(WeiXieFanghu.tianj_bnt)  # 添加标签
#         dr.click(dr.list_fenzu[i])  # 添加分组,分组为时一个list,循环下方策略。
#         dr.click(WeiXieFanghu.queding_bnt)  # 目标确定
#         dr.click(WeiXieFanghu.quedng_tianjiacelv_bnt)  # 确定添加策略
#         dr.click(WeiXieFanghu.quedng_baocuncelv_bnt)  # 确定保存防护策略
#     loca_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 获取下发策略的时间
#     time.sleep(2)
#     dr.xiafacelv_time = datetime.datetime.strptime(loca_time, '%Y-%m-%d %H:%M:%S')  # 时间格式化
