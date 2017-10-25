# coding:utf-8
# python 3.4
# author yinruyi
# email  yinruyi.hm@gmail.com
import poplib, email
from email.header import decode_header
import smtplib
import time
import os, sys


def accp_mail():
    host = "pop3.sina.com"
    username = "lugelc@sina.com"  # 关机邮箱
    password = "ll150705"  # 邮箱密码
    pp = poplib.POP3(host)
    pp.set_debuglevel(1)
    pp.user(username)
    pp.pass_(password)
    ret = pp.stat()
    ret = pp.list()
    down = pp.retr(len(ret[1]))
    a = down[1][10].decode('utf-8')
    b = down[1][33].decode('utf-8')
    if a != "X-Sender: luchige@qq.com":  # 我常用的邮箱
        pass
    else:
        if b == "Subject: shutdown":  # 发送关机主题
            # depend on the down itself
            return 0
    pp.quit()


def send_mail():
    handle = smtplib.SMTP('smtp.sina.com', 25)
    handle.login('lugelc@sina.com', 'll150705')  # 关机邮箱帐号和密码
    msg = "To: lugelc@sina.com\r\nFrom: lugelc@sina.com\r\nSubject: haha \r\n\r\nstart\r\n"
    # 从关机邮箱到关机邮箱主题为haha的邮件
    handle.sendmail('lugelc@sina.com', 'lugelc@sina.com', msg)
    # 发送
    handle.close()


def send_mail1():
    handle = smtplib.SMTP('smtp.sina.com', 25)
    handle.login('lugelc@sina.com', 'll150705')  # 关机邮箱帐号和密码
    msg = "To: luchige@qq.com\r\nFrom: lugelc@sina.com\r\nSubject: already shutdown \r\n\r\nstart\r\n"
    # 从关机邮箱到常用邮箱主题为已经关机的邮件
    handle.sendmail('lugelc@sina.com', 'luchige@qq.com', msg)
    handle.close()


if __name__ == '__main__':
    while 1:
        time.sleep(5)
        if accp_mail() == 0:
            # print('just success')
            send_mail()
            # 让关机邮箱自己给自己发一封不同于shutdown的邮件
            send_mail1()
            # 让关机邮箱给自己的常用邮箱发一封已经关机的邮件
            os.system('shutdown -f -s -t 10 -c closing...')
            # 关机
            break