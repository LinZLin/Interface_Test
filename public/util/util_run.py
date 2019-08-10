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
from public.common.cm_json import CmJson
from public.common.cm_request import CmRequest
from public.util.util_rely import UtilRely
import json
import logging
from public.util.util_config import UtilConfig


class UtilRun:
    '''
    传入行数，执行该行的测试用例，并返回结果
    '''

    def __init__(self, excel_path, sheet, json_path):
        self.data = Data(excel_path, sheet)
        self.json = CmJson()
        self.json_path = json_path
        self.excel_path = excel_path
        self.sheet = sheet
        self.request = CmRequest()
        UtilConfig().log_path()

    def begin(self, row):
        is_run = self.data.get_is_run(row)

        if is_run:
            self.url = self.data.get_url(row)
            self.method = self.data.get_method(row)
            self.header = self.data.get_header_by_json(self.json_path, row)
            self.out_time = self.data.get_out_time(row)
            ex_result = str(self.data.get_ex_result(row))
            is_rely = self.data.is_rely(row)
            self.parameter = self.data.get_data_by_json(self.json_path, row)  # 需最后执行，否则self.data会是空对象，句柄被持有

            if is_rely:
                rely_tuple = UtilRely(self.excel_path, self.sheet, self.json_path, row).get_rely_values()
                re_list = self.__replace_and_send(rely_tuple)
            else:
                re_list = self.request.send_request(url=self.url, method=self.method, data=self.parameter,
                                                    headers=self.header,
                                                    timeout=self.out_time)
        re_result = str(re_list[0])
        status_code = re_list[1]
        flag = False

        if ex_result in re_result and str(status_code) == '200':
            flag = True
            print('此次测试用例的执行结果 ==> PASS')
            self.data.write_re_result(row, 'PASS')
        else:
            print('此次用例的测试结果 ==> FAIL')
            self.data.write_re_result(row, re_result)
        return flag

    def __replace_and_send(self, rely_tuple):
        rely_field = rely_tuple[0]
        rely_value = rely_tuple[1]
        rely_field_place = rely_tuple[2]
        rely_replace_key = rely_tuple[3]
        rely_row = rely_tuple[4]
        try:
            if rely_field_place == 'url':
                url = '%s?%s&%s' % (self.url, rely_field, rely_value)  # 拼接新的url
                re_tuple = self.request.send_request(url=url, method=self.method, data=self.parameter,
                                                     headers=self.header,
                                                     timeout=self.out_time)
            elif rely_field_place == 'header':
                self.header[rely_field] = rely_value

                re_tuple = self.request.send_request(url=self.url, method=self.method, data=self.parameter,
                                                     headers=self.header,
                                                     timeout=self.out_time)
            elif rely_field_place == 'body':
                parameter = self.data.replace_dic_value(self.parameter, rely_replace_key, rely_value)
                re_tuple = self.request.send_request(url=self.url, method=self.method, data=parameter,
                                                     headers=self.header,
                                                     timeout=self.out_time)
        except Exception:
            logging.error("第%s行被依赖的请求数据被替换时出现错误" % rely_row)
            raise Exception
        return json.dumps(re_tuple[0]), re_tuple[1]

# if __name__ == '__main__':
# excel_path = r'E:\python\Frame\Interface\test_data\excel\test_rx.xls'
# sheet = 0
# json_path = r''
