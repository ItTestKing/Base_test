from seleniumbase.fixtures.base_case import BaseCase
from common.login_page import MyTest
from common.Element_API import WeiGeLi, ComoonPagee, SuoYouZhuJi
from selenium.common.exceptions import NoSuchElementException
import time
import re
import datetime


class WeigeliPage(BaseCase):
    xiafacelv_time = None
    text_celv = None
    """
    测试微隔离，策略下发和验证。
    """

    # 终端tab
    list_fenzu = [ComoonPagee.xuanzeweifenzu_zhongduan, ComoonPagee.xuanzewindowfenzu,
                  ComoonPagee.xuanzewindowzifenzu, ComoonPagee.xuanzelinuxfenzu,
                  ComoonPagee.xuanzelinuxzifenzu]

    # 创建安全域分组名称
    list_anquanyu = ['未分组', 'windows分组', 'windows子分组', 'linux分组', 'linux子分组']

    # 创建入站规则选择通信对象

    def chuangjian_anquanyu(self, dr, fenzumingcheng, fenzu):
        # 创建安全域
        #MyTest().admin_loggin(dr)
        dr.click(ComoonPagee.jianceyufanghu_tab)  # 选择检测与防护模块
        dr.click(ComoonPagee.weigeli)  # 选择微隔离标签
        dr.click(WeiGeLi.xinzeng_button)  # 选择新增标签
        dr.send_keys(WeiGeLi.anquanyumingcheng_input, fenzumingcheng)  # 输入安全域名称
        dr.click(WeiGeLi.tianjia_btn)  # 添加按钮
        # dr.click(WeiGeLi.zhongduan_biaoqian)  # 点击终端标签 以后s加上
        dr.click(fenzu)  # 选取执行标签
        dr.click(ComoonPagee.quedingxuanze_bnt)  # 确定添加终端
        dr.click(WeiGeLi.querentianj_anquanyu_btn)  # 确认添加安全域

    def chuangjian_duixiang(self, dr):
        # 创建终端对象

        # MyTest().admin_loggin(dr)
        # dr.click(ComoonPagee.jianceyufanghu_tab)  # 选择检测与防护模块
        # dr.click(ComoonPagee.weigeli)  # 选择微隔离标签
        dr.refresh()
        for i in range(10):
            nowtime = datetime.datetime.now()
            times = nowtime.strftime("%Y_%m_%d %H:%M:%S")
            dr.click(WeiGeLi.tongxduixiang_tab)  # 选择通信对象tab
            dr.click(WeiGeLi.tongxunxinzen_btn)  # 新增通信对象
            print(dr.get_text(WeiGeLi.tongxinduix_tabl))  #
            dr.send_keys(WeiGeLi.tongxduixiangmingcheng_input, 'test_{}'.format(times))  # 通信对象名称
            dr.send_keys(WeiGeLi.tongxingduixneir_input, '10.10.67.3')
            dr.click(WeiGeLi.tongxuntianjtiaoimu_bnt)
            dr.click(WeiGeLi.tongxun_queding_bnt)
            dr.click(WeiGeLi.tongxun_zaiciqueding_bng)

    def cweigeli_ruzhan(self, dr):
        # 创建入站规则
        # MyTest().admin_loggin(dr)
        # dr.click(ComoonPagee.jianceyufanghu_tab)  # 选择防护模块
        # dr.click(ComoonPagee.weigeli)  # 选择微隔离标签
        dr.refresh()
        # for 循环添加安全域
        for i in range(1):
            i += 1
            dr.js_click("//*[@id='mqTargetBody']/tr[{}]/td/div[1]/span".format(i))
            dr.click(WeiGeLi.ruzhanguizexinzen_btn)  # 点击新增按钮
            dr.click(WeiGeLi.tongxunduixiang_xuanze)  # 点击通信对象选择按钮
            dr.click(WeiGeLi.tongxunduixiang_mingcheng)  # 通信对象名称选择 ，此出提前寻找好了几个元素。
            dr.click(WeiGeLi.tongxun_libie_duankou_queding)  # 通信对象确定
            dr.click(WeiGeLi.zuzhi_redio_btn)  # 阻止
            dr.click(WeiGeLi.jilurizhi_input_chekbox)  # 记录日志
            dr.js_click(WeiGeLi.tongxun_libie_duankou_queding)  # 通信对象确定
            dr.click(WeiGeLi.ruzhancelv_queding_bnt)  # 点击入站策略确定按钮
            dr.click(WeiGeLi.quedingtianjia_guize_btn)  # 确定添加入站规则

    def xiafacelv(self, dr):
        """
        测试步骤：
        1.点击下发按钮
        2.查看微隔离，同步终端是否正确。
        3.查看所有主机，当前版本，和历史版本是否一致。
        """
        # MyTest().admin_loggin(dr)
        # dr.click(ComoonPagee.jianceyufanghu_tab)  # 选择防护模块
        # dr.click(ComoonPagee.weigeli)  # 选择微隔离标签
        dr.refresh()
        dr.click(WeiGeLi.xiafa_btn)  # 点击下发按钮
        dr.click(WeiGeLi.xiafa_queding_btn)  # 确定下发
        loca_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 获取下发策略的时间
        time.sleep(2)
        dr.xiafacelv_time = datetime.datetime.strptime(loca_time, '%Y-%m-%d %H:%M:%S')  # 时间格式化

    def weigel_check(self, dr):
        # 微隔离安全域里比较
        # MyTest().admin_loggin(dr)
        # dr.click(ComoonPagee.jianceyufanghu_tab)  # 选择防护模块
        # dr.click(ComoonPagee.weigeli)  # 选择微隔离标签

        # 此出为测试，在此次获取下发时间，真正测试应该注释
        loca_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 获取下发策略的时间
        time.sleep(2)
        dr.xiafacelv_time = datetime.datetime.strptime(loca_time, '%Y-%m-%d %H:%M:%S')  # 时间格式化

        while True:
            check_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 获取当前时间
            check_timestr = datetime.datetime.strptime(check_time, '%Y-%m-%d %H:%M:%S')  # 获取的时间格式化
            resutlt = (check_timestr - dr.xiafacelv_time).seconds  # 将时间差转换为秒
            dr.refresh()  # 刷新浏览器
            time.sleep(10)  # 休眠时间
            if resutlt < 3600:  # 如果时间差小于3600
                text = dr.get_text(WeiGeLi.tongbudzhongduan_text)  # 获取分组元素的值
                res = re.findall(r'\d+', text)  # 取出值里的数字
                print(res[0], res[1])
                if res[0] != res[1]:  # 如果不相等，跳出for循环
                    break
                if res[0] == res[1]:
                    return dr.assert_equal(res[0], res[1], msg="比较最后一个")
            if resutlt > 3600:
                return dr.assert_equal(0, 1, msg="比较失败")

    # 检测版本情况
    def suoyouzhuji_check(self, dr):
        # MyTest().admin_loggin(dr)
        dr.click(ComoonPagee.zichanguanl_tab)  # 点击资产管理标签
        dr.click(ComoonPagee.suoyouzhuji_tab)  # 点击所有主机
        dr.refresh()  # 此处不能点击
        dr.click(SuoYouZhuJi.xianshilie)  # 点击显示列
        dr.double_click(SuoYouZhuJi.qingchusuoyou)  # 双击清除所有列
        dr.click(SuoYouZhuJi.xianshiweigeli)  # 点击显示微隔离
        dr.click(SuoYouZhuJi.queding_xuanxiang, timeout=10)  # 点击确定

        loca_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        time.sleep(2)
        dr.xiafacelv_time = datetime.datetime.strptime(loca_time, '%Y-%m-%d %H:%M:%S')  # 此出时间真正测试的时候，应该去掉
        # 开始获取版本信息
        while True:
            check_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 获取当前时间
            check_timestr = datetime.datetime.strptime(check_time, '%Y-%m-%d %H:%M:%S')  # 获取的时间格式化
            resutlt = (check_timestr - dr.xiafacelv_time).seconds  # 将时间差转换为秒
            dr.refresh()  # 刷新浏览器
            time.sleep(10)  # 休眠时间
            print(1111)
            if resutlt <= 3600:  # 如果时间差小于3600
                version_num = dr.find_elements(SuoYouZhuJi.ceilv_zhuangtai_text)  # 获取一组元素list返回
                for i in version_num:  # 循环每个元素，取出title值
                    version = (i.get_attribute('title'))
                    res = re.findall(r'\d+', version)  # 处理结果，只取当前版本和最新版本号
                    print(res[0], res[1])
                    if res[0] != res[1]:  # 如果版本不相同跳出循环，进行下一次比较
                        # print(res[0] == res[1])
                        break  # 跳出for循环，进入wile循环。
                    if res[0] == res[1]:
                        if i == version_num[-1]:  # 如果比较的元素时列表中的最后一个元素，那么证明，所有元素的值都相等，这时返回比较结果。
                            print("比较完毕，结果一样")
                            return dr.assert_equal(res[0], res[1], msg="比较完毕")
            if resutlt > 3600:
                return dr.assert_equal(1, 2, msg="超时了，比较失败")  # 如果超时直接判断为失败

    def data_check(self, dr):
        # MyTest().admin_loggin(self) #登陆
        str = []
        dr.click(ComoonPagee.rizhibaobia_tab)  # 点击日志报表tab
        dr.click(ComoonPagee.weigeli_data_tab)  # 点击微隔离日志
        a = dr.find_elements("//td/div")
        for i in a:
            result = i.text

            str.append(result)
            # if u'\u4e00' <= result <= u'\u9fff': #如果包含中文则存储在列表里
            #     str.append(result)
        print(str)
        return str

    def stest_deleta_anquanyu(self, dr):
        # 删除分组
        i = 0
        flag = True
        # MyTest().admin_loggin(dr)
        dr.click(ComoonPagee.jianceyufanghu_tab)  # 选择威胁防护模块
        dr.click(ComoonPagee.weigeli)  # 选择微隔离标签
        while flag:
            i += 1
            if i > 8:
                i = 1
                dr.refresh()
            dr.js_click("//*[@id='mqTargetBody']/tr[{}]/td/div[1]/span".format(i))  # 这个标签时选择微隔离安全分组
            dr.click(WeiGeLi.shanchu_button)
            try:
                dr.click(WeiGeLi.shanchuanquanyu_queding_btn)
            except NoSuchElementException:
                flag = False
        self.update_text()
        self.find_elements()