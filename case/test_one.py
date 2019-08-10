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
from test_data.data import Data
from public.common.cm_excel import CmExcel
from public.util.util_config import UtilConfig
from public.util.util_run import UtilRun
import ddt


@ddt.ddt
class TestOne(unittest.TestCase):
    '''
    测试类
    '''
    config = UtilConfig()
    report_path = config.report_path()
    test_paths = config.test_path_tuple('test_one')
    excel_path = test_paths[0]
    sheet_index = test_paths[1]
    json_path = test_paths[2]
    excel = CmExcel(excel_path, sheet_index)
    run_list = Data(excel_path, sheet_index).get_run_list()

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.excel.excel_copy(cls.report_path)

    @ddt.data(*run_list)
    def test_one(self, data):
        result = UtilRun(self.excel_path, self.sheet_index, self.json_path).begin(data)
        self.assertTrue(result)
