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
import requests
import json
import logging
from public.util.util_config import UtilConfig


class CmRequest:
    '''
    requests常用方法
    '''

    def __init__(self):
        UtilConfig().log_path()

    def send_request(self, **kwargs):
        global response
        self.url = kwargs['url']
        timeout = kwargs['timeout']
        method = kwargs['method']
        headers = kwargs['headers']
        data = json.dumps(kwargs['data'], ensure_ascii=False).encode()  # 转成json格式

        if timeout != None:
            timeout = float(timeout)
        if method == 'get':
            response = requests.get(url=self.url, headers=headers, params=data, timeout=timeout, verify=False)
        elif method == 'post':
            response = requests.post(url=self.url, data=data, headers=headers, timeout=timeout,
                                     verify=False)
        # 输出到测试报告中
        print('\nurl ==》', self.url)
        print('header ==》', headers)
        print('response ==> ', response.text)
        print("响应时间 ==> ", response.elapsed.total_seconds(), '\n')

        json_response = self.__change_json(response)
        return json_response, response.status_code

    def __change_json(self, response):
        try:
            json_response = json.loads(response.text)
            # json_response = json.dumps(response.json(), indent=2)
            return json_response
        except Exception:
            error_msg = 'ERROR：响应文本不是json格式'
            print(error_msg)  # 输出到测试报告中
            logging.error('%s的响应文本不是json格式,\n响应文本是：%s' % (self.url, response.text))
            raise RuntimeError

# if __name__ == '__main__':
#     # url = 'http://www.baidu.com'
#     url = 'http://api.renxingge.cn/sys?hotel_id=28&room_id=2299'
#     method = 'get'
#     # headers = '{"X-Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjE2MzM1LCJpc3MiOiJtcnhkLXNjMDciLCJpYXQiOjE1NTk0NDQxMzEsImV4cCI6MTU1OTUzMDUzMSwianRpIjoiZXI4QUhOdUtBSUNUcDlzMSJ9.zPh7SfglH3AJ6Zp6AXP3ZCV1qxC7OzrLqmwlQJ-l-cA"}'
#     headers = '{"X-Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxNjMzNSIsImlzcyI6Im1yeGQtc2MwNyIsImlhdCI6MTU1NzYzMjEzMSwiZXhwIjoxNTU3NzE4NTMxLCJqdGkiOiJka1dnNXFubUJobTVhRzBQIn0.mWleOlXiiJ6udEJ4k6Eu5poHoDbraIRIzibHoHJ8-8c"}'
#     # headers = None
#     timeout = 10
#     rs = CmRequest().send_request(url=url, method=method, headers=headers, timeout=timeout)
#     print('rs:', rs)

# method = 'post'
# url = 'http://api.gosh666.com/api/admin/login'
# data = {
#     "cellphone": "17620066343",
#     "code": "123456"
# }
# time = 10
# print(CmRequest().send_request(url=url, data=data, method=method, headers=None, timeout=time))
