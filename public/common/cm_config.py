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
from configparser import ConfigParser


class CmConfig:
    '''
    config配置文件的方法
    '''

    def __init__(self, path):
        self.cp = ConfigParser()
        self.cp.read(path, encoding='utf-8')

    def get_sections(self):
        return self.cp.sections()

    def get_items_by_section(self, section):
        return self.cp.items(section)

    def get_value(self, section, option):
        return self.cp.get(section, option)
