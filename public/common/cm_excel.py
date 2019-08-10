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

import xlrd
from xlutils.copy import copy
import shutil
from public.util.util_config import UtilConfig
import logging


class CmExcel:
    '''
    excel常用方法
    '''

    def __init__(self, path, sheet):
        self.path = path
        self.sheet = sheet
        self.excel = self.__get_sheet()
        UtilConfig().log_path()

    def __get_sheet(self):
        return xlrd.open_workbook(self.path).sheet_by_index(self.sheet)

    def get_rows(self):
        return self.excel.nrows

    def get_cols(self):
        return self.excel.ncols

    def get_value(self, row, col):
        value = self.excel.cell_value(rowx=row, colx=col)
        return value

    def get_row_values(self, row, start_col, end_col=None):
        return self.excel.row_values(row, start_col, end_col)

    def get_col_values(self, col, start_row, end_row=None):
        return self.excel.col_values(col, start_row, end_row)

    def write_data(self, row, col, data):
        try:
            new_excel = copy(xlrd.open_workbook(self.path))
            new_excel.get_sheet(self.sheet).write(row, col, str(data))
            new_excel.save(self.path)
        except Exception:
            logging.error('写入失败：Excel的第%s行、第%s列的内容：\n%s' % (row + 1, col, data))
            raise Exception

    def excel_copy(self, target_path):
        try:
            shutil.copy(self.path, target_path)
        except Exception:
            logging.error('%s中的excel文件复制到%s失败' % (self.path, target_path))
            raise Exception
