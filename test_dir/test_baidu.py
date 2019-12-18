from seleniumbase import BaseCase

from common.login_page import MyTest


class TestBaidu(BaseCase):

    def test_open(self):
        MyTest().admin_loggin(self)

        print(self.get_current_url())