'''
@Author: lzl
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
 '''
import unittest
from public.BeautifulReport import BeautifulReport
from public.util.util_config import UtilConfig
import time


class Run:
    '''
    执行测试
    '''

    @staticmethod
    def __get_test_suite(test_dir, pattern='test_*.py'):
        return unittest.defaultTestLoader.discover(
            start_dir=test_dir,
            pattern=pattern
        )

    @staticmethod
    def __report(report_path, test_suite, filename: str = 'interface_report', description='interface_report'):
        report = BeautifulReport(test_suite)
        report.report(
            log_path=report_path,
            description=description,
            filename=filename
        )

    def run_tests(self, test_dir, report_path, report_name):
        test_suite = self.__get_test_suite(test_dir)
        self.__report(report_path=report_path, test_suite=test_suite, filename=report_name)


if __name__ == '__main__':
    config = UtilConfig()
    report_path = config.report_path()
    test_dir = config.test_case_path()
    time = time.strftime('%m-%d', time.localtime())
    report_name = str(time) + '_interface_report'
    Run().run_tests(test_dir=test_dir, report_path=report_path, report_name=report_name)
