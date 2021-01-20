# # 这个文件是配置发送邮件的主题，正文等，将测试报告发送并抄送到相关人员邮箱的逻辑
#
# import os
# import smtplib
# import base64
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from testfile.readConfig import ReadConfig
#
#
# class SendEmail(object):
#     def __init__(self, username, passwd, recv, title, content, email_host,
#                  file=None, ssl=False, port=25, ssl_port=994):
#         self.smtp = smtplib.SMTP(self.email_host, self.port)
#         self.username = username  # 用户名
#         self.passwd = passwd  #密码
#         self.recv = recv  # 收件人，多个要传list["a@qq.com","b@qq.com"]
#         self.title = title  # 邮件标题
#         self.content = content  # 邮件正文
#         self.email_host = email_host  # smtp服务器地址
#         self.file = file  # 附件路径，如果不在当前目录下，要写绝对路径
#         self.ssl = ssl  # 是否安全连接
#         self.port = port  # 普通端口
#         self.ssl_port = ssl_port  # 安全连接端口
#
#     def send_email(self):
#         msg = MIMEMultipart()  # https://blog.csdn.net/Winnycatty/article/details/84548381
#         # 发送内容的对象
#
#         if self.file:  # 处理附件
#             file_name = os.path.split(self.file)[-1] # 只取文件名，不取路径
#             try:
#                 f = open(self.file, "r", encoding="gb18030", errors="ignore").read()
#             except Exception as e:
#                 raise Exception("附件打不开")
#             else:
#                 att = MIMEText(str(f), "base64", "utf-8")
#                 att["Content-Type"] = "application/octet-stream"
#                 new_file_name = "=?utf-8?b" + base64.b64encode(file_name.encode()).decode() + "?="
#                 # 这里是处理文件名为中文名的，必须这么写
#                 att["Content-Disposition"] = 'attachment; filename="%s"' % (new_file_name)
#                 msg.attach(att)
#
#
#         msg.attach(MIMEText(self.content))  # 邮件正文内容
#         msg["Subject"] = self.title  # 邮件主题
#         msg["From"] = self.username  # 发送者账号
#         msg["To"] = ",".join(self.recv)  # 接收者账号列表
#         if self.ssl:
#             self.smtp = smtplib.SMTP_SSL(host=self.email_host, port=self.ssl_port)
#         else:
#             pass
#
#         # 发送邮件服务器的对象
#         self.smtp.login(str(self.username), str(self.passwd))
#
#
#         try:
#             self.smtp.sendmail(self.username, self.recv, msg.as_string())
#             pass
#         except Exception as e:
#             print("出错啦", e)
#         else:
#             print("发送成功！")
#         self.smtp.quit()
#
#
# if __name__ == "__main__":
#
#
#     m = SendEmail(
#         username=ReadConfig().get_email("username"),
#         passwd=ReadConfig().get_email("passwd"),  # 授权码
#         recv=ReadConfig().get_email("recv"),
#         title=ReadConfig().get_email("title"),
#         content=ReadConfig().get_email("content"),
#         file="E:\\python_project\\python_unittest\\testfile\\case\\UserCase.xlsx",
#         ssl=ReadConfig().get_email("ssl"),
#         email_host=ReadConfig().get_email("email_host"),
#     )
#
#     m.send_email()

# 这个文件是配置发送邮件的主题，正文等，将测试报告发送并抄送到相关人员邮箱的逻辑

import os
import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendEmail(object):
    def __init__(self, username, passwd, recv, title, content,
                 file=None, ssl=False,
                 email_host="smtp.126.com", port=25, ssl_port=465):
        self.username = username  # 用户名
        self.passwd = passwd  #密码
        self.recv = recv  # 收件人，多个要传list["a@qq.com","b@qq.com"]
        self.title = title  # 邮件标题
        self.content = content  # 邮件正文
        self.file = file  # 附件路径，如果不在当前目录下，要写绝对路径
        self.email_host = email_host  # smtp服务器地址
        self.port = port  # 普通端口
        self.ssl = ssl  # 是否安全连接
        self.ssl_port = ssl_port  # 安全连接端口

    def send_email(self):
        msg = MIMEMultipart()  # https://blog.csdn.net/Winnycatty/article/details/84548381
        # 发送内容的对象
        if self.file:  # 处理附件
            file_name = os.path.split(self.file)[-1] # 只取文件名，不取路径
            try:
                f = open(self.file, "rb").read()
            except Exception as e:
                raise Exception("附件打不开")
            else:
                att = MIMEText(f, "base64", "utf-8")
                att["Content-Type"] = "application/octet-stream"
                new_file_name = "=?utf-8?b" + base64.b64encode(file_name.encode()).decode() + "?="
                # 这里是处理文件名为中文名的，必须这么写
                att["Content-Disposition"] = 'attachment; filename="%s"' % new_file_name
                msg.attach(att)
        msg.attach(MIMEText(self.content))  # 邮件正文内容
        msg["Subject"] = self.title  # 邮件主题
        msg["From"] = self.username  # 发送者账号
        msg["To"] = ",".join(self.recv)  # 接收者账号列表
        if self.ssl:
            self.smtp = smtplib.SMTP_SSL(self.email_host, port=self.ssl_port)
        else:
            self.smtp = smtplib.SMTP(self.email_host, port=self.port)

        # self.smtp = smtplib.SMTP_SSL(self.email_host, port=self.ssl_port)
        # 发送邮件服务器的对象
        self.smtp.login(self.username, self.passwd)
        try:
            self.smtp.sendmail(self.username, self.recv, msg.as_string())
            pass
        except Exception as e:
            print("出错啦", e)
        else:
            print("发送成功！")
        self.smtp.quit()


if __name__ == "__main__":

    m = SendEmail(
        username="suntingting_100@126.com",
        passwd="BTHSVBTDJRABAUOJ",  # 授权码
        recv=["suntingting_100@126.com"],
        title="测试",
        content="测试发送邮件",
        file=r"E:\python_project\python_unittest\picture\smtp2.jpg",
        ssl=True,
    )

    m.send_email()