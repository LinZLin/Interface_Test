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
import logging


class CmLog:
    '''
    设置日志文件的基本属性
    '''

    def __init__(self, log_path, log_level=logging.WARNING):
        logging.basicConfig(
            filename=log_path,
            filemode='a+',
            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s ==> %(message)s',  # 内容格式；单词错误的话，message报错
            datefmt='%Y-%m-%d %H:%M:%S',
            level=log_level
        )

        # 设置编码
        encode_header = logging.FileHandler(log_path, encoding='utf-8')
        logging.getLogger(log_path).addHandler(encode_header)
