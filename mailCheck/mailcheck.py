# coding:utf-8
"""
python2
"""
import poplib
import smtplib
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
from email.mime.text import MIMEText
import os

import time


def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def guess_charset(msg):
    # 先从msg对象获取编码:
    charset = msg.get_charset()
    if charset is None:
        # 如果获取不到，再从Content-Type字段获取:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


def get_email_headers(msg):
    # 邮件的From, To, Subject存在于根对象上:
    headers = {}
    for header in ['From', 'To', 'Subject', 'Date']:
        value = msg.get(header, '')
        if value:
            if header == 'Date':
                headers['date'] = value
            if header == 'Subject':
                # 需要解码Subject字符串:
                subject = decode_str(value)
                headers['subject'] = subject
            else:
                # 需要解码Email地址:
                hdr, addr = parseaddr(value)
                name = decode_str(hdr)
                value = u'%s <%s>' % (name, addr)
                if header == 'From':
                    from_address = value
                    headers['from'] = from_address
                else:
                    to_address = value
                    headers['to'] = to_address
    content_type = msg.get_content_type()
    print 'head content_type: ', content_type
    return headers


# indent用于缩进显示:
def get_email_cntent(message, base_save_path):
    j = 0
    content = ''
    attachment_files = []
    for part in message.walk():
        j = j + 1
        file_name = part.get_filename()
        contentType = part.get_content_type()
        # 保存附件
        if file_name:  # Attachment
            # Decode filename
            h = email.Header.Header(file_name)
            dh = email.Header.decode_header(h)
            filename = dh[0][0]
            if dh[0][1]:  # 如果包含编码的格式，则按照该格式解码
                filename = unicode(filename, dh[0][1])
                filename = filename.encode("utf-8")
            data = part.get_payload(decode=True)
            att_file = open(base_save_path + filename, 'wb')
            attachment_files.append(filename)
            att_file.write(data)
            att_file.close()
        elif contentType == 'text/plain' or contentType == 'text/html':
            # 保存正文
            data = part.get_payload(decode=True)
            charset = guess_charset(part)
            if charset:
                charset = charset.strip().split(';')[0]
                print 'charset:', charset
                data = data.decode(charset)
            content = data
    return content, attachment_files


def send_mail(to_list, sub, content):
    """
    :param to_list: 发给谁
    :param sub: 主题
    :param content: 内容
    :return:
    """
    # 连接到
    me = "陆驰" + "<" + emailaddress + ">"
    msg = MIMEText(content)
    msg['Subject'] = sub  # 主题
    msg['From'] = me  # 发件人
    msg['To'] = ';'.join(to_list)  # 收件人
    try:
        smtp = smtplib.SMTP()
        smtp.connect(mail_host)
        smtp.login(emailaddress, password)
        smtp.sendmail(me, to_list, msg.as_string())
        smtp.close()
        return True
    except Exception, e:
        print str(e)
        return False


def directory_check(path):
    '''

    :param path: 路径，是不是文件没判断
    :return: Boolean
    '''
    if os.path.exists(path):
        return True
    else:
        if os.mkdir(path):
            return True
        else:
            return False


def get_last_email():  # 获取最新一封邮件信息
    try:
        # 连接到POP3服务器:
        server = poplib.POP3(pop3_server)
        # 可以打开或关闭调试信息:
        # server.set_debuglevel(1)
        # POP3服务器的欢迎文字:
        # print server.getwelcome()
        # 身份认证:
        server.user(emailaddress)
        server.pass_(password)

        # stat()返回邮件数量和占用空间:  (5, 19913)
        messagesCount, messagesSize = server.stat()
        resp, mails, octets = server.list()
        down = server.retr(len(mails))  # 返回最新一封邮件
        server.quit()
        return (1, messagesCount, down)
    except poplib.error_proto, e:
        print 'Login failed:', e


def continue_get_mail():  # 持续获取信息
    mail_number_old = 0
    while 1:
        (error, mail_number, down) = get_last_email()
        if (error == 1) and (mail_number != mail_number_old):  # 没有保报错，并且有新邮件
            mail_number_old = mail_number
            resp, lines, octets = down
            # lines存储了邮件的原始文本的每一行,
            # 可以获得整个邮件的原始文本:
            msg_content = '\n'.join(lines)
            # 把邮件内容解析为Message对象：
            msg = Parser().parsestr(msg_content)

            # 但是这个Message对象本身可能是一个MIMEMultipart对象，即包含嵌套的其他MIMEBase对象，
            # 嵌套可能还不止一层。所以我们要递归地打印出Message对象的层次结构：
            print '---------- 解析之后 ----------'
            base_save_path = 'C:/Users/luchi/Desktop/email/'
            print directory_check(base_save_path)
            msg_headers = get_email_headers(msg)
            content, attachment_files = get_email_cntent(msg, base_save_path)

            print 'subject:', msg_headers['subject']
            print 'from_address:', msg_headers['from']
            print 'to_address:', msg_headers['to']
            print 'date:', msg_headers['date']
            # print 'content:', content
            print 'attachment_files: ', attachment_files
        time.sleep(10)
        print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def email_message():  # 获取所有邮件信息
    """
    :return:
    """
    # 连接到POP3服务器:
    server = poplib.POP3(pop3_server)
    # 可以打开或关闭调试信息:
    # server.set_debuglevel(1)
    # POP3服务器的欢迎文字:
    # print server.getwelcome()
    # 身份认证:
    server.user(emailaddress)
    server.pass_(password)
    # stat()返回邮件数量和占用空间:  (5, 19913)
    messagesCount, messagesSize = server.stat()
    print 'messagesCount:', messagesCount
    print 'messagesSize:', messagesSize
    # list()返回所有邮件的编号:
    resp, mails, octets = server.list()
    print '------ resp ------'
    print resp  # +OK 5 messages (19913 octets) 响应的状态 邮件数量 邮件占用的空间大小
    print '------ mails ------'
    print mails  # 所有邮件的编号及大小的  list，['1 2211', '2 29908', ...]
    print '------ octets ------'
    print octets

    # 获取最新一封邮件, 注意索引号从1开始:
    length = len(mails)
    for i in range(length):
        resp, lines, octets = server.retr(i + 1)
        # lines存储了邮件的原始文本的每一行,
        # 可以获得整个邮件的原始文本:
        msg_content = '\n'.join(lines)
        # 把邮件内容解析为Message对象：
        msg = Parser().parsestr(msg_content)

        # 但是这个Message对象本身可能是一个MIMEMultipart对象，即包含嵌套的其他MIMEBase对象，
        # 嵌套可能还不止一层。所以我们要递归地打印出Message对象的层次结构：
        print '---------- 解析之后 ----------'
        base_save_path = 'C:/Users/luchi/Desktop/email/'
        print directory_check(base_save_path)
        msg_headers = get_email_headers(msg)
        content, attachment_files = get_email_cntent(msg, base_save_path)

        print 'subject:', msg_headers['subject']
        print 'from_address:', msg_headers['from']
        print 'to_address:', msg_headers['to']
        print 'date:', msg_headers['date']
        # print 'content:', content
        print 'attachment_files: ', attachment_files


if __name__ == '__main__':
    # 输入邮件地址, 口令和POP3服务器地址:
    emailaddress = 'lugelc@sina.com'
    # 注意使用开通POP，SMTP等的授权码
    password = 'll150705'
    pop3_server = 'pop.sina.com'
    mail_host = 'smtp.sina.com'

    # email_message()
    continue_get_mail()

    # 发送邮件测试
    send_list = ['luchige@qq.com']  # 发送邮件列表
    flag = False
    # flag= send_mail(send_list,'标题测试','内容测试')   #发送邮件
    if flag:
        print '发送ok'
        flag = False
    else:
        print '发送失败'
