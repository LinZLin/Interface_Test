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

from public.common.cm_excel import CmExcel
from test_data.excel import excel_field as field
from public.common.cm_json import CmJson


class Data:
    '''
    从excel、json中获取接口测试所需的值
    '''

    def __init__(self, excel_path, sheet):
        self.excel = CmExcel(excel_path, sheet)

    def get_id(self, row):
        id = str(self.excel.get_value(row, field.get_id()))
        if id.strip() == '':
            return None
        return id

    def get_name(self, row):
        name = str(self.excel.get_value(row, field.get_name()))
        if name.strip() == '':
            return None
        return name

    def get_url(self, row):
        url = str(self.excel.get_value(row, field.get_url()))
        if url.strip() == '':
            return None
        return url

    def get_is_run(self, row):
        flag = False
        is_run = str(self.excel.get_value(row, field.get_is_run()))
        if is_run == 'yes':
            flag = True
        return flag

    def get_method(self, row):
        method = str(self.excel.get_value(row, field.get_request_method()))
        if method.strip() == '':
            return None
        return method

    def get_header_by_json(self, json_path, row):
        header_key = str(self.excel.get_value(row, field.get_request_header_key()))
        if header_key.strip() != '':
            return CmJson.get_value(json_path, header_key)
        return None

    def get_data_by_json(self, json_path, row):
        request_key = str(self.excel.get_value(row, field.get_request_data_key()))
        if request_key != '':
            return CmJson.get_value(json_path, request_key)
        return None

    def is_rely(self, row):
        flag = False
        rely_id = self.get_rely_id(row)
        if rely_id != None:
            flag = True
        return flag

    def get_rely_id(self, row):
        rely_id = str(self.excel.get_value(row, field.get_rely_id()))
        if rely_id.strip() != '':
            return rely_id
        return None

    def get_rely_field(self, row):
        rely_field = str(self.excel.get_value(row, field.get_rely_field()))
        if rely_field.strip() == '':
            return None
        return rely_field

    def get_rely_field_place(self, row):
        rely_field_place = str(self.excel.get_value(row, field.get_rely_field_place()))
        if rely_field_place.strip() == '':
            return None
        return rely_field_place

    def __rely_row_values(self, rely_id):
        '''
        根据依赖id，返回该行的内容和行数
        '''
        col_values = self.excel.get_col_values(field.get_id(), 0)
        row = 0
        for value in col_values:
            if str(value) == rely_id:
                row_values = self.excel.get_row_values(row, 0)
                return row_values, row
            row += 1
        return None

    def get_rely_tuple(self, row):
        rely_id = str(self.excel.get_value(row, field.get_rely_id()))
        if rely_id.strip() != '':
            return self.__rely_row_values(rely_id)
        return None

    def get_rely_replace_key(self, row):
        rely_replace_key = str(self.excel.get_value(row, field.get_rely_replace_key()))
        print("rely_replace_key", rely_replace_key)
        if rely_replace_key.strip() == '':
            return None
        return rely_replace_key

    def get_out_time(self, row):
        out_time = self.excel.get_value(row, field.get_out_time())
        if not isinstance(out_time, float):
            return 10
        return out_time

    def get_ex_result(self, row):
        ex_result = str(self.excel.get_value(row, field.get_ex_result()))
        if ex_result.strip() == '':
            return None
        return ex_result

    def write_re_result(self, row, data):
        self.excel.write_data(row, field.get_re_result(), data)

    def get_run_list(self):
        '''
        返回所有运行的用例的行数（ddt需要list）
        '''
        case_list = []
        rows = self.excel.get_rows()
        for row in range(1, rows):
            is_run = self.get_is_run(row)
            if is_run:
                case_list.append(row)
        return case_list

    def replace_dic_value(self, data_dic, key, data):
        if not isinstance(data_dic, dict):
            raise RuntimeError('data_dic is not dic')
        elif key != None:
            if key in data_dic:
                print("dic[key]", data_dic[key])
                data_dic[key] = data
                return data_dic
        raise RuntimeError('key is NULL or inexistence')

# if __name__ == '__main__':
#     excel_path = r'E:\python\Frame\Interface\test_data\excel\test_one.xls'
#     sheet = 0
#     data = Data(excel_path, sheet).get_out_time(2)
#     print(data, type(data))
#     dic = {'keyword': '', 'openId': '123', 'pageNum': 1, 'pageSize': 10}
#     key = "openId"
#     data = 'replace'
#     value = Data(excel_path, sheet).replace_dic_value(dic, key, data)
#     print(value)
