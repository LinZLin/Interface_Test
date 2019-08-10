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
from test_data.data import Data
from public.common.cm_request import CmRequest
from test_data.excel import excel_field as field
from jsonpath_rw import parse
import json


class UtilRely:
    '''
    根据传入的依赖id，处理被依赖的用例
    '''

    def __init__(self, excel_path, sheet, json_path, row):
        self.data = Data(excel_path, sheet)
        self.json_path = json_path
        self.row = row

    def __send_rely(self):
        rely_values_tuple = self.data.get_rely_tuple(self.row)
        rely_values_list = rely_values_tuple[0]
        rely_row = rely_values_tuple[1]
        url = rely_values_list[field.get_url()]
        method = rely_values_list[field.get_request_method()]
        out_time = rely_values_list[field.get_out_time()]
        data = self.data.get_data_by_json(self.json_path, rely_row)
        header = self.data.get_header_by_json(self.json_path, rely_row)
        rely_response = CmRequest().send_request(url=url, method=method, data=data, headers=header, timeout=out_time)[0]
        return json.loads(json.dumps(rely_response)), rely_row  # 需要转成dict类型，方便使用jsonpath_rw进行解析

    def get_rely_values(self):
        rely = self.__send_rely()
        rely_tuple = rely[0]
        rely_row = rely[1]
        response_json = rely_tuple

        rely_replace_key = self.data.get_rely_replace_key(self.row)
        rely_field_place = self.data.get_rely_field_place(self.row)
        rely_field = self.data.get_rely_field(self.row)
        json_exe = parse(rely_field)  # 1、建立规则：需要查找的元素的层级
        result_set = json_exe.find(response_json)  # 2、从dict类型的json数据中查找，返回list集合
        rely_value = [result.value for result in result_set][0]  # 3、遍历取想要的值,返回list，需要索引取值
        print('依赖的键值对：%s:%s，所处位置是:%s' % (rely_field, rely_value, rely_field_place))  # 加入到测试报告中的内容
        return rely_field, rely_value, rely_field_place, rely_replace_key, rely_row
