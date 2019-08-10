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


class ExcelField:
    '''
    excel用例字段常量类
    '''

    ID = 0
    NAME = 1
    URL = 2
    IS_RUN = 3
    REQUEST_METHOD = 4
    REQUEST_HEADER_KEY = 5
    REQUEST_DATA_KEY = 6
    RELY_ID = 7
    RELY_FIELD = 8
    RELY_FIELD_PLACE = 9
    RELY_REPLACE_KEY = 10
    OUT_TIME = 11
    EX_RESULT = 12
    RE_RESULT = 13


def get_id():
    return ExcelField.ID


def get_name():
    return ExcelField.NAME


def get_url():
    return ExcelField.URL


def get_is_run():
    return ExcelField.IS_RUN


def get_request_method():
    return ExcelField.REQUEST_METHOD


def get_request_header_key():
    return ExcelField.REQUEST_HEADER_KEY


def get_request_data_key():
    return ExcelField.REQUEST_DATA_KEY


def get_rely_id():
    return ExcelField.RELY_ID


def get_rely_field():
    return ExcelField.RELY_FIELD


def get_rely_field_place():
    return ExcelField.RELY_FIELD_PLACE


def get_rely_replace_key():
    return ExcelField.RELY_REPLACE_KEY


def get_out_time():
    return ExcelField.OUT_TIME


def get_ex_result():
    return ExcelField.EX_RESULT


def get_re_result():
    return ExcelField.RE_RESULT
