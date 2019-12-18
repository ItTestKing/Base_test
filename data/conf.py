import sys
sys.path.append('E:\work\Base_test\data\conf.py')


# WEB_SERVER_URL="https://10.10.59.100/"
WEB_SERVER_URL = "https://10.11.64.244/"
#WEB_SERVER_URL = "https://10.11.64.239/"
event_base_url=WEB_SERVER_URL+"admin/majorSec.php?pageID="
# dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
# radiansdict.setdefault(key, default=None)
every_tab = {"安全总览": event_base_url+"dashboard",
             "风险终端概览": event_base_url+"riskClient",
             "风险事件概览": event_base_url+"riskEvent",
             "文件执行分析": event_base_url+"execFile",
             "网络访问分析": event_base_url+"netAccess",
             "所有主机": event_base_url+"device",
             "未注册主机": event_base_url+"unRegDevices",
             "无线路由": event_base_url+"wirlessHub",
             "安装软件": event_base_url+"software",
             "资产变化轨迹": event_base_url+"deviceTrace",
             "漏洞管理": event_base_url+"patches",
             "安全基线": event_base_url+"safeBaseline",
             "弱密码检测": event_base_url+"weakPassword",
             "网站后门检测": event_base_url+"webshell",
             "运行风险": event_base_url+"runtimeRisk",
             "多维威胁检查": event_base_url+"multiThreat",
             "威胁防护策略": event_base_url+"safePolicy",
             "微隔离": event_base_url+"microQuarantine",
             "沙箱检测": event_base_url+"sandboxScan",
             "实时文件搜索": event_base_url+"file",
             "风险事件溯源": event_base_url+"incidentTrace",
             "登录监控审计": event_base_url+"loginAudit",
             "操作命令审计": event_base_url+"cmdLineAudit",
             "威胁事件日志": event_base_url+"incidentLog",
             "系统威胁日志": event_base_url+"incidentLog",
             "网络威胁日志": event_base_url+"netThreatLog",
             "微隔离日志": event_base_url+"microQuarantineLog",
             "系统管理日志": event_base_url+"systemLog",
             "报表管理": event_base_url+"presentationReport",
             "任务管理": event_base_url+"task",
             "参数设置": event_base_url+"setting",
             "标签管理": event_base_url+"tag",
             "账户配置": event_base_url+"account",
             "黑白名单管理": event_base_url+"bwlist",
             "隔离文件管理": event_base_url+"quarantinedFile",
             "重要通知配置": event_base_url+"alertSetting",
             "探针部署": event_base_url+"agent",
             }
