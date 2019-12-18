# -*- coding: utf-8 -*-
import os
import ssl
import win32com.client
import win32api, win32con
import win32process
from time import sleep
from PIL import Image
import os, win32gui, win32ui
import cv2
import numpy as np


class ScreenPng(object):
    url = r"C:\Users\user\Desktop\pic\imag_"
    def screen_image(self, begin, dpath, image_name, weight, height, stop):

        # 截屏函数,调用方法window_capture('d:\\') ,参数为指定保存的目录
        # 返回图片文件名,文件名格式name.png

        hwnd = 0
        hwndDC = win32gui.GetWindowDC(hwnd)
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()
        saveBitMap = win32ui.CreateBitmap()
        MoniterDev = win32api.EnumDisplayMonitors(None, None)
        w = MoniterDev[0][2][2]
        h = MoniterDev[0][2][3]
        # print w,h　　　#图片大小
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
        saveDC.SelectObject(saveBitMap)
        saveDC.BitBlt((begin), (weight, height), mfcDC, (stop), win32con.SRCCOPY)
        # print(w,h)
        # cc=time.gmtime()
        # bmpname=str(cc[0])+str(cc[1])+str(cc[2])+str(cc[3]+8)+str(cc[4])+str(cc[5])+'.bmp'
        bmpname = image_name
        saveBitMap.SaveBitmapFile(saveDC, bmpname)
        Image.open(bmpname).save(bmpname + ".png")
        os.remove(bmpname)
        jpgname = bmpname + '.png'
        djpgname = dpath +r"/"+ jpgname
        copy_command = "move %s %s" % (jpgname, djpgname)
        os.popen(copy_command)
        return bmpname + '.png'

    # 调用截屏函数
    # url = r"C:\Users\user\Desktop\lvmeng\pic\u"
    # begin=(614,375)
    # stop=(781,402)
    # window_capture(stop,url,"ninstall",173,125,begin)
    # 比较截图
if __name__=="__main__":
    # def test_1(self):
    url = r"D:\imag_"
    name="new_uninstall"
    start = (0, 0)
    stop = (100, 100)
    ScreenPng().screen_image(start, url,name, 1600, 850, stop)

