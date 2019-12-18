import time

from selenium.common.exceptions import ElementNotVisibleException, ElementNotInteractableException
from seleniumbase import BaseCase


class MyElements(BaseCase):

    def elements_click(self,dr, selectory):
        """探针卸载获得的class都是第一个
        #elements=dr.find_visible_elements(".ivu-btn.ivu-btn-primary.ivu-btn-large")#确定
    """
        try:
            time.sleep(0.5)
            elements = dr.find_visible_elements(selectory[0])  # 确定
            if len(elements) == 1:  # 如果可见元素list的长度等于1
                time.sleep(0.5)
                elements[0].click()
            else:
                element = elements[selectory[1]]
                element.click()
        except IndexError:
            elements = dr.find_elements(selectory[0])  # 确定
            if len(elements) == 1:  # 如果可见元素list的长度等于1
                elements[0].click()
            else:
                element = elements[selectory[1]]
                element.click()
        except ElementNotInteractableException:
            time.sleep(2)
            elements = dr.find_elements(selectory[0])  # 确定
            if len(elements) == 1:  # 如果可见元素list的长度等于1
                elements[0].click()
            else:
                element = elements[selectory[1]]
                element.click()
        # if len(elements) > selectory[1] and len(elements)!=1: #list的长度大于预期值
        #     time.sleep(1)
        #     if len(elements) <= selectory[1] and len(elements)!=1: #list小于等于预期值。
        #         elements = dr.find_elements(selectory[0])
        #
        #         return 0
        # if len(elements) <= selectory[1] and len(elements) != 1:  # list小于等于预期值。
        #     elements = dr.find_elements(selectory[0])
        #     element = elements[selectory[1]]
        #     element.click()
        #     return 0



        #except ElementNotInteractableException:



    def elements_text_update(self,dr, selectory, msg):
        """探针卸载获得的class都是第一个
        #elements=dr.find_visible_elements(".ivu-btn.ivu-btn-primary.ivu-btn-large")#确定
    """
        # print(selectory)
        try:
            elements = dr.find_visible_elements(selectory[0])  # 确定
            if len(elements) == 1: #如果可见元素list的长度等于1
                element = elements[0]
                element.clear()
                element.send_keys(msg)
            if len(elements) >= selectory[1] and len(elements)!=1: #如果可见元素list的长度大于预期值
                element = elements[selectory[1]]
                element.clear()
                element.send_keys(msg)
            if len(elements) < selectory[1] and len(elements)!=1: #如果可见元素大于1，小于预期值。
                elements = dr.find_elements(selectory[0])
                element = elements[selectory[1]]
                element.clear()
                element.send_keys(msg)
        except ElementNotVisibleException:
            print('没有这个元素！')
            dr.assert_equal('', "页面上没有这个元素{}".format(selectory[0]))
        except IndexError:
            elements = dr.find_(selectory[0])
            element = elements[selectory[1]]
            element.clear()
            element.send_keys(msg)