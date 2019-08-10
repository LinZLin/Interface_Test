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

import smtplib  # 导入smtplib发送邮件模块，发送和接收都是由smtplib.SMTP方法来完成的

from email.mime.multipart import MIMEMultipart  # 组装邮件的内容

# 主要用于完善邮箱内容和标题的定义
from email.mime.text import MIMEText
from email.header import Header

# 通过ini文件获取发送邮件所需的参数值
from public.util.util_config import UtilConfig

import os


class CmEmail:
    '''
    email方法
    '''

    @staticmethod
    def __get_email_obj(email_sub, email_from, email_to_list):
        '''
        构建邮件对象，设置邮件主题、发件人、收件人
        @param email_sub:  邮件主题
        @param email_from:  发件人昵称
        @param email_to_list: 收件人list
        @return: 邮件对象
        '''

        # 创建根容器
        email_obj = MIMEMultipart('related')
        # 邮件主题、发件人、收件人
        email_obj['Subject'] = Header(email_sub, 'utf-8')
        # 以,号连接收件人地址
        email_to = ''.join(email_to_list)
        email_obj['From'] = Header(email_from)
        email_obj['To'] = Header(email_to)
        return email_obj

    @staticmethod
    def __attach_content(email_obj, email_content='', content_type='plain', charset='utf-8'):
        '''
        创建邮件正文，并附加到根容器中。
        @param email_obj:  邮件对象，根容器
        @param email_content:  邮件正文
        @param content_type: 邮件内容格式，默认纯文本plain；可以是html
        @param charset: 编码格式，默认utf-8
        @return: null
        '''
        # 创建邮箱正文
        content = MIMEText(email_content, content_type, charset)
        # 将邮件正文附加到根容器
        email_obj.attach(content)

    @staticmethod
    def __attach_adjunct(email_obj, adjunct_paths):
        '''
        添加多个附件到根容器，可以是文件也可以是文档
        @param email_obj: 邮件对象：根容器
        @param adjunct_path:  附件文件的路径
        @param adjunct_name:  附件名称
        @return: null
        '''
        for adjunct_path in adjunct_paths:  # 遍历添加多个附件
            # 创建附件对象并将附件添加到附件对象上；'octet-stream': binary data
            adjunct = MIMEText(open(adjunct_path, 'rb').read(), 'base64', 'utf-8')
            adjunct["Content-Type"] = 'application/octet-stream'
            # 给附件添加头文件、设置名称，带格式
            adjunct_name = adjunct_path.split('result\\')[-1]  # 附件名称就是本身的文件名
            adjunct["Content-Disposition"] = 'attachment; filename="%s"' % adjunct_name
            # 附件添加到根容器中
            email_obj.attach(adjunct)

    @staticmethod
    def __send_mail(email_obj, email_host, host_port, email_from, email_pwd, email_to_list):
        '''
        发送邮件
        @param email_obj: 邮件对象
        @param email_host: SMTP服务器主机
        @param host_port: SMTP服务端口号
        @param email_from: 发件地址
        @param email_pwd: 发送地址的授权码，不是密码
        @param email_to_list: 收件地址：list
        @return: True：成功；False：失败
        '''
        try:
            # 连接smtp邮箱服务器
            smtp_obj = smtplib.SMTP_SSL(email_host, host_port)
            # 登陆发件邮箱：邮箱和对应授权码
            smtp_obj.login(email_from, email_pwd)
            smtp_obj.sendmail(email_from, email_to_list, email_obj.as_string())
            smtp_obj.quit()
            return True
        except smtplib.SMTPException:
            return False

    @staticmethod
    def __get_adjunct_list(report_path):
        '''
        获取指定报告目录下的所有文件的名称，并返回结果list
        :param report_path: 指定报告目录
        :return:
        '''
        adjunct_list = []
        reports = os.listdir(report_path)
        i = 0
        for adjunct in reports:
            adjunct = os.path.join(report_path + '\\' + reports[i])
            adjunct_list.append(adjunct)
            i += 1
        return adjunct_list

    @staticmethod
    def __send_config():
        '''
        读取email.ini文件中的邮件属性值发送邮件
        附件为report文件夹下最新的文件
        若有想更改的，直接更改ini文件
        :return: null
        '''
        # 拼接路径，读取ini文件中发送邮件所需要的参数值
        base_path = os.path.realpath(__file__).split('\\Interface_Data_Frame')[0]
        ini_path = base_path + '\Interface_Data_Frame\config\config.ini'
        config = UtilConfig()
        report_path = config.report_path()
        email_params = config.emil_params()

        # report文件夹下最新的一个文件为附件
        Email = CmEmail()
        adjunct_path = Email.__get_adjunct_list(report_path)

        # 调用本类方法，发送邮件
        email_obj = Email.__get_email_obj(email_params['email_subject'], email_params['email_from'],
                                          email_params['to_addr_list'])
        #  正文若是文本则不需要传参content_type
        Email.__attach_content(email_obj, email_params['email_content'])
        Email.__attach_adjunct(email_obj, adjunct_path)
        Email.__send_mail(email_obj, email_params['email_host'], email_params['host_port'], email_params['from_addr'],
                          email_params['pwd'], email_params['to_addr_list'].split(','))

    def send_email(self):
        '''
        调用私有方法进行邮件发送，可更改email.ini文件进行相关修改
        :return: null
        '''
        self.__send_config()


if __name__ == "__main__":
    CmEmail().send_email()
