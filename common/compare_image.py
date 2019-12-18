# -*- coding:utf-8 -*-
import time

import cv2
import imutils

import numpy as np
import sys

from skimage.measure import compare_ssim

sys.path.append('E:\work\Base_test')


class Compare(object):
    def cv_imread(self, filePath):
        cv_img = cv2.imdecode(np.fromfile(filePath, dtype=np.uint8), -1)
        ## imdecode读取的是rgb，如果后续需要opencv处理的话，需要转换成bgr，转换后图片颜色会变化
        ##cv_img=cv2.cvtColor(cv_img,cv2.COLOR_RGB2BGR)
        return cv_img

    def compare_image(self, base_png, run_png,png_name):
        DiffSnapshot_Dir="../pic/diffrent_png"

        # image1 = cv2.imread(image_old)
        # image2 = cv2.imread(image_now)
        try:
            image1 = self.cv_imread(base_png)
            image2 = self.cv_imread(run_png)
            difference = cv2.subtract(image1, image2)
            result = not np.any(difference)  # if difference is all zeros it will return False
            if result is True:
                print("两张图片一样")
                return True
            else:
                # cv2.imwrite("result.jpg", difference)
                self.mark_diff_img(base_png,run_png,DiffSnapshot_Dir, png_name)
                print("两张图片不一样")
        except Exception as e:
            self.mark_diff_img(base_png, run_png,DiffSnapshot_Dir, png_name)
            print(e)
            return False
    #如果不一样时标记差异
    def mark_diff_img(self, basesnapshot_png, runningsnapshot_png, DiffSnapshot_Dir, name):
        """
        对比图片并标出差异，保存差异图片
        :param basesnapshot_png:
        :param runningsnapshot_png:
        :param DiffSnapshot_Dir:
        :param casename:
        :param name:
        :return:
        """
        # 加载两张图片并将他们转换为灰度：
        image_a = self.cv_imread(basesnapshot_png)
        image_b = self.cv_imread(runningsnapshot_png)
        gray_a = cv2.cvtColor(image_a, cv2.COLOR_BGR2GRAY)
        gray_b = cv2.cvtColor(image_b, cv2.COLOR_BGR2GRAY)

        # 计算两个灰度图像之间的结构相似度指数：
        (score, diff) = compare_ssim(gray_a, gray_b, full=True)
        diff = (diff * 255).astype("uint8")
        print("SSIM:{}".format(score))

        # 找到不同点的轮廓以致于我们可以在被标识为“不同”的区域周围放置矩形：
        thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        # 找到一系列区域，在区域周围放置矩形：
        for c in cnts:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(image_a, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.rectangle(image_b, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # 基础快照标出与运行时快照的差异 图片
        diffsnapshot_png_a = DiffSnapshot_Dir + '/' + name + '_base.png'
        # 运行时快照标出与基础快照的差异 图片
        diffsnapshot_png_b = DiffSnapshot_Dir + '/' + name + '_running.png'
        # 保存差异图片
        time.sleep(0.5)
        cv2.imencode('.jpg', image_a)[1].tofile(diffsnapshot_png_a)
        cv2.imencode('.jpg', image_b)[1].tofile(diffsnapshot_png_b)
        # result["对比快照-基础快照路径"] = diffsnapshot_png_a
        # result["对比快照-运行时快照路径"] = diffsnapshot_png_b
if __name__ == "__main__":
    #Compare().compare_image(r"D:\\work\\Base_test\\pic\\无线路由.png", r"D:\\work\Base_test\\comparePic\\无线路由_default.png")
    base_png="../pic/base_png/Linux漏洞_default.png"
    run_png="../pic/base_png/所有主机_default.png"
    DiffSnapshot_Dir = "../pic/diffrent_png"
    Compare().mark_diff_img(base_png,run_png,DiffSnapshot_Dir,"name")
