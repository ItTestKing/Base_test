from seleniumbase.fixtures.base_case import BaseCase


def elements_find( dr, selectory, number):
    """获取元素方法，返回值是一个ElementsID，此返回值不将能用BasedCase终端方法。
    #elements=dr.find_visible_elements(".ivu-btn.ivu-btn-primary.ivu-btn-large")#确定
"""
    elements = dr.find_visible_elements(selectory)  # 确定
    element = elements[number]
    return element

class ComoonPagee(object):
    "公共需要使用的元素"

    # 检测防护标签
    jianceyufanghu_tab = "//div[contains(text(),'检测与防护')]"  # 威胁与防护标签 30使用

    # jianceyufanghu_tab = "//*[@id='app']/div/div/div[1]/div[1]/div/ul/li[4]/div"  # 威胁与防护标签
    weixiefanghu_tab = "//li[contains(text(),'威胁防护策略')]"  # 威胁防护策略
    weigeli = "//li[contains(text(),'微隔离')]"  # 微隔离标签

    # 资产管理标签
    zichanguanl_tab = "//div[contains(text(),'资产管理')]"  # 30版本专用
    # zichanguanl_tab = "//*[@id='app']/div/div/div[1]/div[1]/div/ul/li[2]"
    suoyouzhuji_tab = "//li[contains(text(),'所有主机')]"

    # 风险管理标签
    fengxiangguanl_tab = "//div[contains(text(),'风险管理')]"  # 风险管理  30版本使用
    # fengxiangguanl_tab = '//*[@id="app"]/div/div/div[1]/div[1]/div/ul/li[3]/div' #风险管理
    ruomim_jiance_tab = "//li[contains(text(),'弱密码检测')]"  # 弱密码检测

    anquan_jixian_tab = "//li[contains(text(),'安全基线')]"  # 安全基线
    wangzhanhoumen_jixian_tab = "//li[contains(text(),'网站后门')]"  ##网站后门检测

    # 选择分组按钮
    xuanzeweifenzu_zhongduan = "//div[contains(text(),'选择目标')]/../..//div[2]/div/div[2]/div[2]/div[1]/div[2]/div/ul/li/ul[1]/li/span[2]"  # 选择未分组
    xuanzelinuxfenzu = "//div[contains(text(),'选择目标')]/../..//div[2]/div/div[2]/div[2]/div[1]/div[2]/div/ul/li/ul[2]/li/span[2]"  # 选择linxu分组
    xuanzelinuxzifenzu = "//div[contains(text(),'选择目标')]/../..//div[2]/div/div[2]/div[2]/div[1]/div[2]/div/ul/li/ul[2]/li/ul/li/span[2]"  # 选择linux子分组
    xuanzewindowfenzu = "//div[contains(text(),'选择目标')]/../..//div[2]/div/div[2]/div[2]/div[1]/div[2]/div/ul/li/ul[3]/li/span[2]"  # 选择windows分组
    xuanzewindowzifenzu = "//div[contains(text(),'选择目标')]/../..//div[2]/div/div[2]/div[2]/div[1]/div[2]/div/ul/li/ul[3]/li/ul/li/span[2]"  # 选择windos子分组
    xuanzzhongduan_tab = "//div[contains(text(),'选择目标')]/../..//div[2]/div/div[2]/div[1]/div/div/div/div/div[3]"  # 选择终端标签
    zhongduan_mingcheng_bnt = "//*[@id='selectTargetPopupClientTable']/tr/td[1]/div/label/span"  # 终端名称
    zhongudan_xuanze_span = "//*[@id='selectTargetPopupClientTable']/tr/td[3]/div/span"  # 终端详细信息

    quxiaoxuanze_bnt = "//div[contains(text(),'选择目标')]/../..//div[3]/div/button[1]/span"  # 确定选择目标
    quedingxuanze_bnt = "//div[contains(text(),'选择目标')]/../..//div[3]/div/button[2]/span"  # 确定选择目标

    # 日志报表
    rizhibaobia_tab = "//div[contains(text(),'日志报表')]"  # 日志报表
    weigeli_data_tab = "//li[contains(text(),'微隔离日志')]"  # 微隔离日志


# 登陆页面类
class AdminLogginPage():
    URL = "https://10.10.67.243"
    admin_btn = "#btnAdmin"  # 选择管理系统Button
    master_btn = "//*[@id='masterConfigBtn']"  # 产品配置系统
    # admin登陆页面元素：
    username_input = "#userNmFake"  # 用户名
    password_input = "#pwdFake"  # "密码"
    logging_btn = "//*[@id='btnLogin']"  # 登陆
    # mster 登陆页面元素：
    passworld_input = "//*[@id='contentDiv']/div[2]/div/div[3]/input"  # 登陆按钮


# 所有主机
class SuoYouZhuJi():
    suoyouzhongduan_tab = "//span[contains(text(),'所有终端')]"
    xinjianzu_btn = "//button[contains(@title,'新建组')]"
    zuming_input = "//input[contains(@placeholder,'组名')]"
    IPqishiduan_input = "//input[contains(@placeholder,'IP段起始值')]"
    IPzhongzhi_input = "//input[contains(@placeholder,'IP段终止值')]"
    ceilv_zhuangtai_text = "//span[contains(@title,'当前版本')]"
    # ceilv_zhuangtai_text = "//td"
    gruop_name = ".ivu-tree-title"  # 所有分组的class 名称

    fenzuxinx_queding_bnt = "//div[contains(text(),'分组信息')]/../../div[3]/div/button[2]/span"
    # weigeli_ceilv_zhuangtai_text=".//*[@id='micro_quarantine_status_label_0/ancestor::*']"
    quedingbaocun_fenzuxinx_bnt = "//div[contains(text(),'确定保存分组信息吗？')]/../div[3]/button[2]/span"
    yidongzhongduan_redoi = "//*[@id='tableContent']/div/div/div[4]/div[2]/table/tbody/tr/td[1]/div/label/span"
    yidongdaozu_tab = "//*[@id='appContent']/div/div[2]/div[2]/div/div/div[1]/button[2]/span"
    xuanzefenzu_tab = "//div[contains(text(),'选择分组')]"
    xuanzefenzu_tabss = "//span[contains(text(),'确定')]"

    xianshilie = "//span[contains(text(),'显示列')]"  # 显示列
    qingchusuoyou = "//label[contains(text(),'所有信息')]/span"  # 显示所有信息
    xianshiweigeli = "//label[contains(text(),'微隔离')]/span"  # 选择微隔离 弱密码策略版本状态
    xuanzeruomima_tab = "//label[contains(text(),'弱密码策略版本状态')]/span"  # 弱密码策略版本状态
    xuanzejixiancelv_tab = "//label[contains(text(),'基线策略版本状态')]/span"  # 基线策略版本状态
    xuanzefanghucelv_tab = "//label[contains(text(),' 防护策略版本状态')]/span"  # 防护策略版本状态

    wangzhanhouomencelv_tab = "//label[contains(text(),'网站后门策略版本状态')]/span"  # 网站后门策略版本状态
    queding_xuanxiang = "//div[contains(text(),'显示列')]/../..//div[3]/button[2]/span"  # 确定选择微隔离、弱密码等

    # 事件清单按钮
    yingyongce_tab = "//div[contains(text(),'应用策略')]"
    wangluoweixie_tab = "//div[contains(text(),'网络威胁')]"
    xinrenqingdan_tab = "//div[contains(text(),'信任IP清单')]"
    xinren_ip = "//div[contains(text(),'信任IP清单')]/..//div[2]/div[3]/div/div/div/div[2]/table/tbody/tr/td[2]/div/span"

    # 分组管理
    #xinzen_bnt = "//*[@id='appContent']/div/div[1]/div[1]/div/div[2]/span/div/button[1]/i"  # 点击创建分组
    xinzen_bnt = ".ivu-icon.ivu-icon-md-add"  # 点击创建分组
    fenzumingcheng_input = ".ivu-input.ivu-input-default"  # 分组名称
    #fenzumingcheng_input = "//div[contains(text(),'分组信息')]/../..//div[2]/div/div[3]/div[2]/div/div[1]/div/input"  # 分组名称

    #queding_tianjia_bnt = "//div[contains(text(),'分组信息')]/../..//div[3]/div/button[2]/span"  # 确定添加按钮

    queding_tianjia_bnt = "//div[contains(text(),'分组信息')]/../..//div[3]/div/button[2]/span"  # 确定添加按钮
    queding_baocun_bnt = "//div[contains(text(),'保存分组信息')]/../..//div[3]/button[2]/span"
    # 分组id
    linuxfenzu_tab = "//span[contains(text(),'linux分组')]"  # Linux分组
    linuxzifenzu_tab = "//span[contains(text(),'linux子分组')]"  # Linux分组
    windowsfenzu_tab = "//span[contains(text(),'windows分组')]"  # Linux分组
    windowszifenzu_tab = "//span[contains(text(),'windows子分组')]"  # Linux分组
    weifenzu = "//span[contains(text(),'未分组终端')]"  # Linux分组


# 安全基线
class AnquanJiXianElt():
    """安全基线的一些标签，按钮"""
    AnQuanjixian_celv_tab = "//div[contains(text(),'安全基线策略')]"  # 安全基线策略标签
    AnQuanjixian_pinggu_tab = "//div[contains(text(),'检查项安全评估')]"  # 检查项安全评估
    XinZen_bnt = "//span[contains(text(),'新增...')]"  # 新增按钮
    Celuve_mingcheng_input = "//input[contains(@placeholder,'策略名称')]"  # 策略名称输入框
    yingyong_moban_select = "//span[contains(text(),'请选择基线模板')]"  # 选择框
    yingyonnmoban_wintab = "//span[contains(text(),'请选择基线模板')]/../../..//div[2]/ul[2]/li[1]"  # windows应用模板选项
    yingyonnmoban_linuxtab = "//span[contains(text(),'请选择基线模板')]/../../..//div[2]/ul[2]/li[2]"  # linux应用模板选项
    tianjia_bnt = "//span[contains(text(),'添加...')]"  # 添加按钮执行目标

    queding_xinzenganquan = "//div[contains(text(),'新增安全基线策略')]/../..//div[3]/div/button[2]/span"  # 确定新增安全基线策略
    quedingbaocun_jixian = "//div[contains(text(),'保存安全基线策略')]/../..//div[3]/button[2]/span"
    xiafa_bnt = "//*[@id='appContent']/div/div[1]/div[1]/div[1]/div/a/i"


# 弱密码
class RuoMimaPage():
    """公用的一些标签，弱密码检测页面"""
    xinzen_bnt = "//span[contains(text(),'新增')]"  # 新增
    ruomima_rizhi_tab = "//div[contains(text(),'弱密码检测日志')]"  # 弱密码检测日志
    jihuamingchen_input = "//div[contains(text(),'弱密码策略')]/../..//div[2]/div[4]/div[2]/div/div[1]/input"  # 计划名称
    mimazidian_select = "//span[contains(text(),'请选择密码字典')]"  # 选择密码字典
    xitongquanliang_tab = "//li[contains(text(),'系统全量密码本')]"  # 系统全量密码本
    xitonggengxinmim_tab = "//li[contains(text(),'系统变量密码本')]"  # 系统变量密码本
    zhixingshijian_input = "//input[contains(@placeholder,'请选择时间')]"  # 输入时间

    tianj_zhixiangmubiao_bnt = "//span[contains(text(),'添加...')]"  # 添加执行目标
    quedingtianjia_mimacelv_bnt = "//div[contains(text(),'密码策略')]/../..//div[3]/div/button[2]/span"  # 确定添加密码策略
    quxiaotianjia_mimacelv_bnt = "//div[contains(text(),'密码策略')]/../..//div[3]/div/button[1]/span"  # 确定添加密码策略


# 网站后门检测
class WangZhanHoumenpage():
    web_data_tab = "//div[contains(text(),'网站后门检测日志')]"
    XinZen_bnt = "//span[contains(text(),'新增...')]"  # 新增按钮
    Jihua_mingcheng_input = "//input[contains(@placeholder,'计划名称')]"  # 输入计划名称

    caozuoxitong = "//div[contains(text(),'网站后门策略')]/../..//div[2]/div[5]/div[1]/div[2]/div/label[2]/span"  # linux操作系统

    guizeku_select = "//span[contains(text(),'请选择规则库')]"  # 选择规则库下拉框
    zhixingriq_span = "//div[contains(text(),'网站后门策略')]/../..//div[2]/div[5]/div[9]/div[2]/div/div[1]/label/span/span"  # 选择webshell
    zhixingshijian_input = "//input[contains(@placeholder,'请选择时间')]"  # 执行时间输入框

    webshell_select = "//div[contains(text(),'网站后门策略')]/../..//div[2]/div[5]/div[5]/div[2]/div/div[2]/ul[2]/li"  # 选择webshell
    wangzhanlujing_input = "//div[contains(text(),'网站后门策略')]/../..//div[2]/div[5]/div[15]/div[2]/div/input"  # 网站后门路径输入框

    tianjlujing_bnt = "//div[contains(text(),'网站后门策略')]/../..//div[2]/div[5]/div[15]/div[3]/div/button[1]"  # 添加路径按钮
    tianjiazhixingmubiao_bnt = "//div[contains(text(),'网站后门策略')]/../..//div[2]/div[5]/div[19]/div[2]/div/button[1]"  # 添加执行目标
    xuanzeweifenzu_zhongduan = "//div[contains(text(),'选择目标')]/../..//div[2]/div/div[2]/div[2]/div[1]/div[2]/div/ul/li/ul[1]/li/span[2]"  # 选择未分组
    xuanzelinuxfenzu = "//div[contains(text(),'选择目标')]/../..//div[2]/div/div[2]/div[2]/div[1]/div[2]/div/ul/li/ul[2]/li/span[2]"  # 选择linxu分组
    xuanzelinuxzifenzu = "//div[contains(text(),'选择目标')]/../..//div[2]/div/div[2]/div[2]/div[1]/div[2]/div/ul/li/ul[2]/li/ul/li/span[2]"  # 选择linux子分组
    xuanzewindowfenzu = "//div[contains(text(),'选择目标')]/../..//div[2]/div/div[2]/div[2]/div[1]/div[2]/div/ul/li/ul[3]/li/span[2]"  # 选择windows分组
    xuanzewindowzifenzu = "//div[contains(text(),'选择目标')]/../..//div[2]/div/div[2]/div[2]/div[1]/div[2]/div/ul/li/ul[3]/li/ul/li/span[2]"  # 选择windos子分组

    quedingtianj_wangzhanhoumen = "//div[contains(text(),'网站后门策略')]/../../div[3]/div/button[2]/span"  # 确定添加网站后门策略
    qued_tianjiacelv_bant = "//div[contains(text(),'策略详情')]/../..//div[3]/button[2]/span"


# 威胁防护策略
class WeiXieFanghu():
    XinZen_bnt = "//span[contains(text(),'新增...')]"  # 新增按钮
    celuve_mingcheng_input = "//input[contains(@placeholder,'策略名称')]"  # 策略名称输入框
    wangluoweixie_tab = "//div[contains(text(),'防护策略')]/../..//div[2]/span/div/div[1]/div/div/div/div/div[4]"  # 网络威胁标签
    xinrenip_tianjia_bnt = "//div[contains(text(),'防护策略')]/../..//div[2]/span/div/div[2]/div[3]/div/div/div[10]/div[2]/div[1]/div/button/span"  # 添加信任ip
    ip_qishi_input = "//div[contains(text(),'添加远端IP地址')]/../..//div[2]/div[5]/div[2]/div/div[1]/div/input"  # ip起始
    ip_zhongzhi_input = "//div[contains(text(),'添加远端IP地址')]/../..//div[2]/div[5]/div[2]/div/div[3]/div/input"  # ip终止
    ipduan_queding_bnt = "//div[contains(text(),'添加远端IP地址')]/../../div[3]/div/button[2]"

    yingyongmubiao_tab = "//div[contains(text(),'应用目标')]"  # 应用目标标签
    tianj_bnt = "//div[contains(text(),'防护策略')]/../..//div[2]/span/div/div[2]/div[6]/div/div[1]/div/button/span"  # 添加按钮 ,有时候5有时候6
    # tianj_bnt="//div[contains(text(),'防护策略')]/../..//div[2]/span/div/div[2]/div[6]/div/div[1]/div/button/span" #添加按钮
    tianjiaweifenzu_tab = "//div[contains(text(),'选择目标')]/../..//div[2]/div/div[2]/div[2]/div[1]/div[2]/div/ul/li/ul[1]/li/span[2]"  # 未分组终端
    tianjia_linux_fenzu_tab = "//div[contains(text(),'选择目标')]/../..//div[2]/div/div[2]/div[2]/div[1]/div[2]/div/ul/li/ul[2]/li/span[2]"  # linux分组
    tianjia_linuxzi_fenzu_tab = "//div[contains(text(),'选择目标')]/../..//div[2]/div/div[2]/div[2]/div[1]/div[2]/div/ul/li/ul[2]/li/ul/li/span[2]"  # linux子分组
    tianjia_win_fenzu_tab = "//div[contains(text(),'选择目标')]/../..//div[2]/div/div[2]/div[2]/div[1]/div[2]/div/ul/li/ul[3]/li/span[2]"  # window分组
    tianjia_win_zi_fenzu_tab = "//div[contains(text(),'选择目标')]/../..//div[2]/div/div[2]/div[2]/div[1]/div[2]/div/ul/li/ul[3]/li/ul/li/span[2]"  # windows子分组

    queding_bnt = "//div[contains(text(),'选择目标')]/../../div[3]/div/button[2]"  # 确定目标
    quedng_tianjiacelv_bnt = "//div[contains(text(),'防护策略')]/../../div[3]/div/button[2]"  # 确定添加策略
    quedng_baocuncelv_bnt = "//div[contains(text(),'确定保存防护策略吗')]/../div[3]/button[2]"  # 确定保存策略


# 微隔离页面类：
class WeiGeLi():
    URL = None
    # 公用标签
    xiafa_btn = ".ivu-icon"".ivu-icon-ios-megaphone"  # 下发策略小喇叭")
    xiafa_queding_btn = "/html/body/div[22]/div[2]/div/div/div[3]/button[2]/span"  # 下发确定按钮
    celvxiafa_panduan_text = "//*[@id='mqTargetBody']/tr[1]/td/div[3]/span/span"  # 探针总数

    # 创建安全域
    xinzeng_button = ".ivu-icon"".ivu-icon-md-add"  # 新增安全域
    shanchu_button = ".ivu-icon"".ivu-icon-md-trash"  # 删除安全域
    anquanyumingcheng_input = "//input[@placeholder='安全域名称']"  # 输入安全域名称
    shanchuanquanyu_queding_btn = "/html/body/div[22]/div[2]/div/div/div[3]/button[2]"  # 删除安全域

    tianjia_btn = "//button[@title='添加目标']"  # 点击添加按钮"
    querentianj_anquanyu_btn = "//div[contains(text(),'安全域')]/../..//div[3]/div/button[2]/span"  # 确认添加安全域按钮")

    # 通信对象管理tab
    tongxduixiang_tab = "//div[contains(text(),'通信对象管理')]"
    tongxunxinzen_btn = "//*[@id='appContent']/div/div/div[2]/div[2]/div/div[1]/div/div[1]/button[1]/span"  # 入站规则新增
    tongxinduix_tabl = "//div[contains(text(),'通信对象名称')]"
    tongxduixiangmingcheng_input = "//div[contains(text(),'通信对象名称')]/../..//div[2]/div/div[1]/input"  # 通信对象名称框
    tongxingduixneir_input = "//div[contains(text(),'通信对象名称')]/../../..//div[10]/div[2]/div/div[1]/div/input"  # 通信对象输入内容框

    tongxuntianjtiaoimu_bnt = "//div[contains(text(),'通信对象名称')]/../../..//div[10]/div[2]/div/div[3]/button/span"  # 添加按钮
    tongxun_queding_bnt = "//div[contains(text(),'通信对象名称')]/../../../../..//div[3]/div/button[2]/span"  # 确定添加通信对象
    tongxun_zaiciqueding_bng = "//div[contains(text(),'确定新增该通信对象吗？')]/../div[3]/button[2]/span"  # 确定添加策略码

    # 入站规则tab

    ruzhanguizexinzen_btn = "//span[contains(text(),'新增')]"  # 入站规则新增
    # 选择TCP和UDP
    tcp_udp = "//div[contains(text(),'入站策略')]/../..//div[2]/div/div[5]/div[2]/div/label[4]/span[1]"  # tcp_udp按钮
    tcp = "//span[contains(text(),'TCP')]"  # tcp按钮
    # 通信对象选择按钮
    tongxunduixiang_xuanze = "//div[contains(text(),'入站策略')]/../..//div[2]/div/div[7]/div[2]/button[1]/span"

    # 选择通信对象名称
    tongxunduixiang_mingcheng = "//div[contains(text(),'通信对象列表')]/../..//div[2]/div/div[3]/div/div/div/div[1]/table/thead/tr/th[1]/div/label/span"  # 全选按钮
    tongxunduixiang_mingchegn_1 = "//div[contains(text(),'通信对象列表')]/../..//div[2]/div/div[3]/div/div/div/div[2]/table/tbody/tr[1]/td[1]/div/label"  # 通信对象第一个
    tongxunduixiang_mingchegn_2 = "//div[contains(text(),'通信对象列表')]/../..//div[2]/div/div[3]/div/div/div/div[2]/table/tbody/tr[2]/td[1]/div/label/span"  # 通信对象第二个

    tongxun_libie_duankou_queding = "//*[@id='getMQAddressPopup_OK']/span"  # 通信对象确定按钮
    duankouduixiang = "//div[contains(text(),'入站策略')]/../..//div[2]/div/div[9]/div[2]/button[1]/span"  # 端口对象选择按钮
    # 端口对象名称
    ruzhancelv_queding_bnt = "//div[contains(text(),'入站策略')]/../..//div[3]/div/button[2]"  # 入站策略确定按钮

    # 阻止
    zuzhi_redio_btn = "//div[contains(text(),'入站策略')]/../..//div[2]/div/div[11]/div[2]/div/label[2]/span[1]"  # 阻止按钮
    # 记录日志
    jilurizhi_input_chekbox = "//div[contains(text(),'入站策略')]/../..//div[2]/div/div[11]/div[2]/label/span"  # 记录日志

    # 确定添加入站规则
    quedingtianjia_guize_btn = "//div[contains(text(),'确定新增该入站策略吗？')]/..//div[3]/button[2]"

    tongbudzhongduan_text = "//*[@id='mqTargetBody']/tr/td/div[3]/span/span"  # 第一个分组
    tongbudzhongduan_two_text = "//*[@id='mqTargetBody']/tr[2]/td/div[3]/span/span"  # 第二个分组
    tongbudzhongduan_three_text = "//*[@id='mqTargetBody']/tr[3]/td/div[3]/span/span"  # 第三个分组
    tongbudzhongduan_for_text = "//*[@id='mqTargetBody']/tr[4]/td/div[3]/span/span"  # 第四个分组


# 系统配置
class XiTongPeiZhi(BaseCase):

    xitongpeizhi_tab = "//div[contains(text(),'系统配置')]"  # 系统配置标签
    renwuguanli_tab = "//li[contains(text(),'任务管理')]"  # 任务管理标签
    canshushezhi_tab = "//li[contains(text(),'参数设置')]"  # 参数设置
    biaoqianguanli_tab = "//li[contains(text(),'任务管理')]"  # 标签管理
    zhanghupeizhi_tab = "//li[contains(text(),'账户配置')]"  # 账户配置
    heibaimingdan_tab = "//li[contains(text(),'黑白名单管理')]"  # 黑白名单管理
    geliwenjian_tab = "//li[contains(text(),'隔离文件管理')]"  # 隔离文件管理
    zhongyaotongzhi_tab = "//li[contains(text(),'重要通知配置')]"  # 重要通知配置
    tanzhenbushu_tab = "//li[contains(text(),'任务管理')]"  # 探针部署
    fenxiwenjian_input=('.ivu-input.ivu-input-small',0) #设置分析文件大小

    uninstall_passwrold=('.ivu-input.ivu-input-small',1) #设置卸载密码
    save_bant=('.fa.fa-save',1)#保存按钮
    primary_bant=(".ivu-btn.ivu-btn-primary.ivu-btn-large",9)#确定按钮
    Enable_expert_mode=(".ivu-checkbox-inner",4)#启用专家模式



class HeiBaiMingDan():
    #文件黑白名单,此处应用字典。
    add_bnt=(".ivu-btn.ivu-btn-primary",2)#文件黑名单新增按钮
    hash_input=(".ivu-input.ivu-input-default",16)#哈希输入框
    note_input=(".ivu-input.ivu-input-default",17)#备注输入框
    primary_btn=(".ivu-btn.ivu-btn-primary.ivu-btn-large",11) #确定按钮
    reprimary_btn=(".ivu-btn.ivu-btn-primary.ivu-btn-large",9) #再次确定按钮

    #file_white_tab=(".ivu-tabs-tab",1) #白名单tab
    file_white_tab=("//*[@id='appContent']/div/div/div[1]/div/div/div/div/div[3]") #白名单tab

    file_certificate_tab=("//*[@id='appContent']/div/div/div[1]/div/div/div/div/div[4]") #证书黑名单tab
    certificate_add=(".ivu-btn.ivu-btn-primary",28) #证书添加按钮
    certificate_hash_input=(".ivu-input.ivu-input-default",14)#证书哈希值
    certificate_note_input=(".ivu-input.ivu-input-default",15)#证书备注
    certificate_trust=("span.ivu-radio-inner",5) #信任
    certificate_no_trust=("span.ivu-radio-inner",6) #不信任
    certificate_primary_btn=(".ivu-btn.ivu-btn-primary.ivu-btn-large",5) #确定按钮


