# -*- coding: utf-8 -*-
'''示例测试用例
'''
#2024/01/03 QTAF自动生成

from solarctldemolib.testcase import SolarctldemoTestCase


class HelloTest01(SolarctldemoTestCase):
    '''示例测试用例
    '''
    owner = "root"
    timeout = 5
    priority = SolarctldemoTestCase.EnumPriority.High
    status = SolarctldemoTestCase.EnumStatus.Design

    def run_test(self):
        self.log_info("hello testcase01")
        self.assert_equal("success", True, True)

class HelloTest02(SolarctldemoTestCase):
    '''示例测试用例
    '''
    owner = "root"
    timeout = 5
    priority = SolarctldemoTestCase.EnumPriority.High
    status = SolarctldemoTestCase.EnumStatus.Design

    def run_test(self):
        self.log_info("hello testcase02")
        self.assert_equal("failed", True, False)


if __name__ == '__main__':
    HelloTest01().debug_run()
