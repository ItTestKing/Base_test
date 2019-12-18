from seleniumbase import BaseCase
from data import conf
from common.login_page import MyTest
import datetime
import os
from common.compare_image import Compare
import logging


class Test_pic(BaseCase):
    nowtime = datetime.datetime.now()
    times = nowtime.strftime("%Y_%m_%d %H:%M:%S")

    def file_compare(self, Compare_png, png):
        if not os.path.exists(Compare_png):
            self.sleep(2)
            self.save_screenshot(Compare_png[14:-4], Compare_png[0:13])
        else:
            self.save_screenshot(png[7:-4], png[0:7])
            self.assert_equal(Compare().compare_image(png, Compare_png), True, "对比图片")
            self.save_screenshot("execFileSituation_default", "../pic")


    # 安全总览adashboard
    def test_aa(self):
        MyTest().admin_loggin(self)
        Compare_png = "../comparePic/dashboard_default.png"
        png = "../pic/dashboard.png"
        self.file_compare(Compare_png, png)

    # 风险终端概览
    def test_riskClient(self):
        self.open(conf.every_tab["风险终端概览"])
        Compare_png = "../comparePic/riskClient_default.png"
        png = "../pic/riskClient.png"
        self.file_compare(Compare_png, png)

    # 风险事件概览
    def test_riskEvent(self):
        self.open(conf.every_tab["风险事件概览"])

        Compare_png = "../comparePic/riskEvent_default.png"
        png = "../pic/riskEvent.png"
        self.file_compare(Compare_png, png)

    # 文件执行分析
    def test_execFile(self):
        self.open(conf.every_tab["文件执行分析"])
        # 文件态势
        # execFileSituation_default_png = "../comparePic/execFileSituation_default.png"
        Compare_png = "../comparePic/execFileSituation_default.png"
        png = "../pic/execFileSituation.png"
        self.file_compare(Compare_png, png)

        # 文件主机
        self.click("//div[contains(text(),'文件执行主机分析')]")
        Compare_png1 = "../comparePic/execFileHost_default.png"
        png1 = "../pic/execFileHost.png"
        self.file_compare(Compare_png1, png1)
        # self.save_screenshot("execFileHost_default", "../pic")

    # 网络访问分析
    def test_netAccess(self):
        #MyTest().admin_loggin(self)
        self.open(conf.every_tab["网络访问分析"])

        Compare_png = "../comparePic/netAccessSituation_default.png"
        png = "../pic/netAccessSituation.png"
        self.file_compare(Compare_png, png)

        # 网络访问主机分析
        self.click("//div[contains(text(),'网络访问主机分析')]")
        Compare_png1 = "../comparePic/netAccessHost_default.png"
        png1 = "../pic/netAccessHost.png"
        self.file_compare(Compare_png1, png1)

    # 所有主机
    def test_device(self):
        self.open(conf.every_tab["所有主机"])
        # self.save_screenshot("device_default", "../pic")
        Compare_png = "../comparePic/device_default.png"
        png = "../pic/device.png"
        self.file_compare(Compare_png, png)

    # 未注册主机
    def test_unRegDevices(self):
        self.open(conf.every_tab["未注册主机"])
        # self.save_screenshot("KnowUnRegDevices_default", "../pic")
        Compare_png = "../comparePic/KnowUnRegDevices_default.png"
        png = "../pic/KnowUnRegDevices.png"
        self.file_compare(Compare_png, png)

        # 已知未注册主机
        self.click("//div[contains(text(),'已知未注册主机')]")

        # self.save_screenshot("DKnowUnRegDevices_default", "../pic")
        Compare_png1 = "../comparePic/DKnowUnRegDevices_default.png"
        png1 = "../pic/DKnowUnRegDevices.png"
        self.file_compare(Compare_png1, png1)

    # 无线路由
    def test_wirlessHub(self):
        self.open(conf.every_tab["无线路由"])
        # self.save_screenshot("wirlessHub_default", "../pic")

        Compare_png = "../comparePic/wirlessHub_default.png"
        png = "../pic/wirlessHub.png"
        self.file_compare(Compare_png, png)

    #  安装软件
    def test_software(self):
        self.open(conf.every_tab["安装软件"])
        # self.save_screenshot("software_default", "../pic")
        Compare_png = "../comparePic/software_default.png"
        png = "../pic/software.png"
        self.file_compare(Compare_png, png)

    #  资产变化轨迹
    def test_deviceTrace(self):
        self.open(conf.every_tab["资产变化轨迹"])
        # self.save_screenshot("deviceTrace_default", "../pic")
        Compare_png = "../comparePic/deviceTrace_default.png"
        png = "../pic/deviceTrace.png"
        self.file_compare(Compare_png, png)

    #  漏洞管理
    def test_patches(self):
        self.open(conf.every_tab["漏洞管理"])
        # self.save_screenshot("windowsPatches_default", "../pic")
        Compare_png = "../comparePic/windowsPatches_default.png"
        png = "../pic/windowsPatches.png"
        self.file_compare(Compare_png, png)

        # linux漏洞
        self.click("//div[contains(text(),'Linux漏洞')]")
        # self.save_screenshot("LinuxPatches_default", "../pic")
        Compare_png1 = "../comparePic/LinuxPatches_default.png"
        png1 = "../pic/LinuxPatches.png"
        self.file_compare(Compare_png1, png1)

    #  安全基线
    def test_safeBaseline(self):
        self.open(conf.every_tab["安全基线"])
        # self.save_screenshot("agentSafeBaseline_default", "../pic")
        Compare_png = "../comparePic/agentSafeBaseline_default.png"
        png = "../pic/agentSafeBaseline.png"
        self.file_compare(Compare_png, png)

        # 检查项安全评估
        self.click("//div[contains(text(),'检查项安全评估')]")
        # self.save_screenshot("checkSafeBaseline_default", "../pic")
        Compare_png1 = "../comparePic/checkSafeBaseline_default.png"
        png1 = "../pic/checkSafeBaseline.png"
        self.file_compare(Compare_png1, png1)
        # 安全基线策略
        self.click("//div[contains(text(),'安全基线策略')]")
        # self.save_screenshot("StrategySafeBaseline_default", "../pic")
        Compare_png2 = "../comparePic/StrategySafeBaseline_default.png"
        png2 = "../pic/StrategySafeBaseline.png"
        self.file_compare(Compare_png2, png2)
        # 安全基线模板

        self.click("//div[contains(text(),'安全基线模板')]")
        # self.save_screenshot("MoBanStrategySafeBaseline_default", "../pic")
        Compare_png3 = "../comparePic/MoBanStrategySafeBaseline_default.png"
        png3 = "../pic/MoBanStrategySafeBaseline.png"
        self.file_compare(Compare_png3, png3)

    #  弱密码检测
    def test_weakPassword(self):
        self.open(conf.every_tab["弱密码检测"])
        # self.save_screenshot("StrategyWeakPassword_default", "../pic")
        Compare_png = "../comparePic/StrategyWeakPassword_default.png"
        png = "../pic/StrategyWeakPassword.png"
        self.file_compare(Compare_png, png)

        self.click("//div[contains(text(),'弱密码字典管理')]")
        # self.save_screenshot("DictWeakPassword_default", "../pic")
        Compare_png1 = "../comparePic/DictWeakPassword_default.png"
        png1 = "../pic/DictWeakPassword.png"
        self.file_compare(Compare_png1, png1)

        self.click("//div[contains(text(),'弱密码检测日志')]")
        # self.save_screenshot("DataWeakPassword_default", "../pic")
        Compare_png2 = "../comparePic/DataWeakPassword_default.png"
        png2 = "../pic/DataWeakPassword.png"
        self.file_compare(Compare_png2, png2)

        self.click("//div[contains(text(),'弱密码执行日志')]")
        # self.save_screenshot("runWeakPassword_default", "../pic")
        Compare_png3 = "../comparePic/runWeakPassword_default.png"
        png3 = "../pic/runWeakPassword.png"
        self.file_compare(Compare_png3, png3)

    #   网站后门检测
    def test_webshell(self):
        self.open(conf.every_tab["网站后门检测"])
        # self.save_screenshot("StrategyWebShell_default", "../pic")
        Compare_png = "../comparePic/StrategyWebShell_default.png"
        png = "../pic/StrategyWebShell.png"
        self.file_compare(Compare_png, png)

        self.click("//div[contains(text(),'规则库')]")
        # self.save_screenshot("RuleWeakWebShell_default", "../pic")
        Compare_png1 = "../comparePic/RuleWeakWebShell_default.png"
        png1 = "../pic/RuleWeakWebShell.png"
        self.file_compare(Compare_png1, png1)

        self.click("//div[contains(text(),'网站后门检测日志')]")
        # self.save_screenshot("dataWeakWebShell_default", "../pic")
        Compare_png2 = "../comparePic/dataWeakWebShell_default.png"
        png2 = "../pic/dataWeakWebShell.png"
        self.file_compare(Compare_png2, png2)

        self.click("//div[contains(text(),'网站后门执行日志')]")
        # self.save_screenshot("runWeakWebShell_default", "../pic")
        Compare_png3 = "../comparePic/runWeakWebShell_default.png"
        png3 = "../pic/runWeakWebShell.png"
        self.file_compare(Compare_png3, png3)

    #   运行风险
    def test_runtimeRisk(self):
        self.open(conf.every_tab["运行风险"])
        # self.save_screenshot("netPort_default", "../pic")
        Compare_png = "../comparePic/netPort_default.png"
        png = "../pic/netPort.png"
        self.file_compare(Compare_png, png)

        self.click("//div[contains(text(),'系统服务')]")
        # self.save_screenshot("SysService_default", "../pic")
        Compare_png1 = "../comparePic/SysService_default.png"
        png1 = "../pic/SysService.png"
        self.file_compare(Compare_png1, png1)

        self.click("//div[contains(text(),'系统账户')]")
        # self.save_screenshot("SysAccount_default", "../pic")
        Compare_png2 = "../comparePic/SysAccount_default.png"
        png2 = "../pic/SysAccount.png"
        self.file_compare(Compare_png2, png2)

        self.click("//div[contains(text(),'Linux资源使用检查')]")
        self.save_screenshot("LinuxCheckUse_default", "../pic")
        Compare_png3 = "../comparePic/LinuxCheckUse_default.png"
        png3 = "../pic/LinuxCheckUse.png"
        self.file_compare(Compare_png3, png3)

        self.click("//div[contains(text(),'异常信息')]")
        # self.save_screenshot("ExceptionInformation_default", "../pic")
        Compare_png4 = "../comparePic/ExceptionInformation_default.png"
        png4 = "../pic/ExceptionInformation.png"
        self.file_compare(Compare_png4, png4)

    #   多维威胁检查
    def test_multiThreat(self):
        MyTest().admin_loggin(self)
        self.open(conf.every_tab["多维威胁检查"])
        # self.save_screenshot("CompleteFile_default", "../pic")
        Compare_png = "../comparePic/CompleteFile_default.png"
        png = "../pic/CompleteFile.png"
        self.file_compare(Compare_png, png)

        self.click("//div[contains(text(),'关键文件')]")
        # self.save_screenshot("KeyDocument_default", "../pic")
        Compare_png1 = "../comparePic/KeyDocument_default.png"
        png1 = "../pic/KeyDocument.png"
        self.file_compare(Compare_png1, png1)

        self.click("//div[contains(text(),'系统配置检查')]")
        # self.save_screenshot("sysconfigCheck_default", "../pic")
        Compare_png2 = "../comparePic/sysconfigCheck_default.png"
        png2 = "../pic/sysconfigCheck.png"
        self.file_compare(Compare_png2, png2)

        self.click("//div[contains(text(),'系统配置变化轨迹')]")
        # self.save_screenshot("sysconfig_default", "../pic")
        Compare_png3 = "../comparePic/sysconfig_default.png"
        png3 = "../pic/sysconfig.png"
        self.file_compare(Compare_png3, png3)

    # 威胁防护策略
    def test_safePolicy(self):
        self.open(conf.every_tab["威胁防护策略"])
        # self.save_screenshot("safePolicy_default", "../pic")
        Compare_png = "../comparePic/safePolicy_default.png"
        png = "../pic/safePolicy.png"
        self.file_compare(Compare_png, png)

    # 微隔离
    def test_microQuarantine(self):
        # MyTest().admin_loggin(self)
        self.open(conf.every_tab["微隔离"])
        # self.save_screenshot("StrategyMicroQuarantine_default", "../pic")
        Compare_png = "../comparePic/StrategyMicroQuarantine_default.png"
        png = "../pic/StrategyMicroQuarantine.png"
        self.file_compare(Compare_png, png)

        self.click("//div[contains(text(),'通信对象管理')]")
        # self.save_screenshot("ObjectMicroQuarantine_default", "../pic")
        Compare_png1 = "../comparePic/ObjectMicroQuarantine_default.png"
        png1 = "../pic/ObjectMicroQuarantine.png"
        self.file_compare(Compare_png1, png1)

        self.click("//div[contains(text(),'端口对象管理')]")
        # self.save_screenshot("portMicroQuarantine_default", "../pic")
        Compare_png2 = "../comparePic/portMicroQuarantine_default.png"
        png2 = "../pic/portMicroQuarantine.png"
        self.file_compare(Compare_png2, png2)

    # 沙箱检测
    def test_sandboxScan(self):
        self.open(conf.every_tab["沙箱检测"])
        # self.save_screenshot("sandboxScan_default", "../pic")
        Compare_png = "../comparePic/sandboxScan_default.png"
        png = "../pic/sandboxScan.png"
        self.file_compare(Compare_png, png)

    #  实时文件搜索
    def test_file(self):
        self.open(conf.every_tab["实时文件搜索"])
        # self.save_screenshot("file_default", "../pic")
        Compare_png = "../comparePic/file_default.png"
        png = "../pic/file.png"
        self.file_compare(Compare_png, png)

    #  风险事件溯源
    def test_incidentTrace(self):
        self.open(conf.every_tab["风险事件溯源"])
        # self.save_screenshot("incidentTrace_default", "../pic")
        Compare_png = "../comparePic/incidentTrace_default.png"
        png = "../pic/incidentTrace.png"
        self.file_compare(Compare_png, png)

    #  登录监控审计
    def test_loginAudit(self):
        self.open(conf.every_tab["登录监控审计"])
        # self.save_screenshot("onlineLogin_default", "../pic")
        Compare_png = "../comparePic/onlineLogin_default.png"
        png = "../pic/onlineLogin.png"
        self.file_compare(Compare_png, png)

        self.click("//div[contains(text(),'账号登录日志')]")
        # self.save_screenshot("dataLogin_default", "../pic")
        Compare_png1 = "../comparePic/dataLogin_default.png"
        png1 = "../pic/dataLogin.png"
        self.file_compare(Compare_png1, png1)

    #   操作命令审计
    def test_cmdLineAudit(self):
        self.open(conf.every_tab["操作命令审计"])
        # self.save_screenshot("cmdLineAudit_default", "../pic")
        Compare_png = "../comparePic/cmdLineAudit_default.png"
        png = "../pic/cmdLineAudit.png"
        self.file_compare(Compare_png, png)

    #    威胁事件日志
    def test_incidentLog(self):
        self.open(conf.every_tab["威胁事件日志"])
        # self.save_screenshot("sysIncidentLog_default", "../pic")
        Compare_png = "../comparePic/sysIncidentLog_default.png"
        png = "../pic/sysIncidentLog.png"
        self.file_compare(Compare_png, png)

        self.click("//div[contains(text(),'网络威胁日志')]")
        # self.save_screenshot("NetIncidentLog_default", "../pic")
        Compare_png1 = "../comparePic/NetIncidentLog_default.png"
        png1 = "../pic/NetIncidentLog.png"
        self.file_compare(Compare_png1, png1)

    # def test_incidentLog(self):
    #     self.open(conf.every_tab["威胁事件日志"])
    #     self.save_screenshot("sysIncidentLog_default", "../pic")
    #
    #     self.click("//div[contains(text(),'网络威胁日志')]")
    #     self.save_screenshot("NetIncidentLog_default", "../pic")

    #    微隔离日志
    def test_microQuarantineLog(self):
        self.open(conf.every_tab["微隔离日志"])
        # self.save_screenshot("microQuarantineLog_default", "../pic")
        Compare_png = "../comparePic/microQuarantineLog_default.png"
        png = "../pic/microQuarantineLog.png"
        self.file_compare(Compare_png, png)

    #    系统管理日志
    def test_systemLog(self):
        self.open(conf.every_tab["系统管理日志"])
        # self.save_screenshot("systemLog_default", "../pic")
        Compare_png = "../comparePic/systemLog_default.png"
        png = "../pic/systemLog.png"
        self.file_compare(Compare_png, png)

    #    报表管理
    def test_presentationReport(self):
        self.open(conf.every_tab["报表管理"])
        # self.save_screenshot("presentationReport_default", "../pic")
        Compare_png = "../comparePic/presentationReport_default.png"
        png = "../pic/presentationReport.png"
        self.file_compare(Compare_png, png)

    # 任务管理
    def test_task(self):
        self.open(conf.every_tab["任务管理"])
        # self.save_screenshot("task_default", "../pic")
        Compare_png = "../comparePic/task_default.png"
        png = "../pic/task.png"
        self.file_compare(Compare_png, png)

    # 参数设置
    def test_setting(self):
        self.open(conf.every_tab["参数设置"])
        # self.save_screenshot("setting_default", "../pic")
        Compare_png = "../comparePic/setting_default.png"
        png = "../pic/setting.png"
        self.file_compare(Compare_png, png)

    # 标签管理
    def test_tag(self):
        self.open(conf.every_tab["标签管理"])
        # self.save_screenshot("tab_default", "../pic")
        Compare_png = "../comparePic/tab_default.png"
        png = "../pic/tab.png"
        self.file_compare(Compare_png, png)

    # 账户配置
    def test_account(self):
        self.open(conf.every_tab["账户配置"])
        # self.save_screenshot("account_default", "../pic")
        Compare_png = "../comparePic/account_default.png"
        png = "../pic/account.png"
        self.file_compare(Compare_png, png)

    # 黑白名单管理
    def test_bwlist(self):
        self.open(conf.every_tab["黑白名单管理"])
        # self.save_screenshot("bwlist_default", "../pic")
        Compare_png = "../comparePic/bwlist_default.png"
        png = "../pic/bwlist.png"
        self.file_compare(Compare_png, png)

    # 隔离文件管理
    def test_quarantinedFile(self):
        self.open(conf.every_tab["隔离文件管理"])
        # self.save_screenshot("quarantinedFile_default", "../pic")
        Compare_png = "../comparePic/quarantinedFile_default.png"
        png = "../pic/quarantinedFile.png"
        self.file_compare(Compare_png, png)

    # 重要通知配置
    def test_alertSetting(self):
        self.open(conf.every_tab["重要通知配置"])
        # self.save_screenshot("alertSetting_default", "../pic")
        Compare_png = "../comparePic/alertSetting_default.png"
        png = "../pic/alertSetting.png"
        self.file_compare(Compare_png, png)

    # 探针部署
    def test_agent(self):
        self.open(conf.every_tab["探针部署"])
        # self.save_screenshot("agent_default", "../pic")
        Compare_png = "../comparePic/agent_default.png"
        png = "../pic/agent.png"
        self.file_compare(Compare_png, png)
