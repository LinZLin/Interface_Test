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
from public.common.cm_config import CmConfig
from public.common.cm_log import CmLog
import os
import time


class UtilConfig:
    '''
    获取config.ini的值
    '''

    def __init__(self):
        self.base_path = os.path.realpath(__file__).split('\\Interface')[0]
        config_path = os.path.join(self.base_path, 'Interface_Test\\config\\config.ini')
        self.config = CmConfig(config_path)

    def log_path(self):
        '''
        调用cm_log日志
        '''
        path = self.config.get_value('path', 'log_path')
        loc_time = time.strftime('%m_%d', time.localtime())
        log_name = str(loc_time) + '_error.log'
        log_path = os.path.join(self.base_path, path, log_name)
        return CmLog(log_path)

    def test_path_tuple(self, test_name):
        path_ex = self.config.get_value('test_excel_path', test_name)
        excel_path = os.path.join(self.base_path, path_ex)
        path_js = self.config.get_value('request_json_path', test_name)
        json_path = os.path.join(self.base_path, path_js)
        try:
            sheet_index = int(self.config.get_value('test_sheet_index', test_name))
        except:
            sheet_index = 0
        return excel_path, sheet_index, json_path

    def test_case_path(self):
        path = self.config.get_value('path', 'test_case_path')
        return os.path.join(self.base_path, path)

    def report_path(self):
        path = self.config.get_value('path', 'report_path')
        return os.path.join(self.base_path, path)

    def emil_params(self):
        email_host = self.config.get_value('server', 'email_host')
        host_port = self.config.get_value('server', 'host_port')
        from_addr = self.config.get_value('server', 'from_addr')
        pwd = self.config.get_value('server', 'pwd')
        email_from = self.config.get_value('content', 'email_from')
        to_addr_list = self.config.get_value('content', 'to_addr_list')
        email_content = self.config.get_value('content', 'email_content')
        email_subject = self.config.get_value('content', 'email_subject')
        params_dict = {
            'email_host': email_host,
            'host_port': host_port,
            'from_addr': from_addr,
            'pwd': pwd,
            'email_from': email_from,
            'to_addr_list': to_addr_list,
            'email_content': email_content,
            'email_subject': email_subject
        }
        return params_dict

# if __name__ == '__main__':
#     rs = UtilConfig().report_path()
#     print(rs)
