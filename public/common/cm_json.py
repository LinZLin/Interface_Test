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

import json
import logging
from public.util.util_config import UtilConfig


class CmJson:
    '''
    json常用方法
    '''

    def __init__(self):
        UtilConfig().log_path()

    @staticmethod
    def get_value(path, key):
        try:
            with open(path, encoding='utf-8') as fp:
                file = json.load(fp)
                return file[key]
        except Exception:
            logging.error('%s取值错误' % key)

    @staticmethod
    def write_data(path, data):
        with open(path, 'a+', encoding='utf-8') as fp:
            json.dumps(data, fp)
        fp.close()
