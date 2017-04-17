# coding: utf-8
import os
import smtplib
import ConfigParser
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import re
import time
from email.utils import parseaddr, formataddr


def sendMail(receiver):
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = _format_addr(u'<%s>' % sender)
    msg['To'] = _format_addr(u'<%s>' % receiver)
    # msg['Cc'] = _format_addr(u'<%s>' % receiver)
    #Create message html content
    att = MIMEText(content,'html','utf-8')
    att["Content-Type"] = 'application/octet-stream'
    msg.attach(att)
    # tls加密方式，通信过程加密，邮件数据安全，使用正常的smtp端口
    if auth == "ssl":
        smtp = smtplib.SMTP_SSL(smtpHost,hostPort)
        #mtp.ehlo()
        print  auth
    elif auth == "tls":
        smtp = smtplib.SMTP(smtpHost,hostPort)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
    else:
        # 普通方式，通信过程不加密
        smtp = smtplib.SMTP(smtpHost, hostPort)
        smtp.ehlo()
    if isdebug=="1":
        smtp.set_debuglevel(1)
    if startAuth=="1":
        smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))
#sendMail(subject);
def readMail():
    filename="emailList.xml"
    if os.path.exists(filename):
        message = 'Start SendMail Script'
    else:
        f = open('emailList.xml', 'a')
        exit("emailList.xml is empty !");

    file_object = open(filename,'r')
    try:
        all_the_text = file_object.read()
    finally:
        file_object.close()

    if all_the_text == "":
        exit("emailList is empty!");

    all_the_text,result=re.subn('\\n|\\r', "", all_the_text)

    print all_the_text;
    Emails=all_the_text.split(",")
    print Emails
    for email in Emails:
        if email !="" :
            print email+" Sendding ..."
            print "Date : "+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            sendMail(email);
            f = open('sendmail.log', 'a')
            f.write(email+","+ '\n')
            f.close();
            print email+" Send Complete\n"
            print "------------------------"
            time.sleep(5)

open('mailcontent.html', 'a')
open('emailList.xml', 'a')


content="";
filename = "mailcontent.html"
if os.path.exists(filename):
    print  ''
else:
    f = open('mailcontent.html', 'a')
    exit("mailcontent.html is not exit , we will create it!");

file_object = open(filename, 'r')
try:
    content = file_object.read()
finally:
    file_object.close()
if content=="":
    exit("mailcontent.html is empty!");

#####################################################

config = ConfigParser.ConfigParser()
config.read("config.ini")

print config.get("global", "startAuth")
print config.get("global", "username")
startAuth=config.get("global", "startAuth")#1
isdebug=config.get("global", "startAuth")#1
smtpHost=config.get("global", "smtpHost")#"smtp.gmail.com"
hostPort=config.get("global", "hostPort")#465
sender = config.get("global", "sender")#'woshishui888888@gmail.com'
username = config.get("global", "username")#'woshishui888888@gmail.com'
password =  config.get("global", "password")#'admin888'
subject=config.get("global", "subject")#"TESTmail"
auth=config.get("global", "auth")#"ssl"
print password

######################################################

print('')
print "\033[1;31;40m=========================================================\033[0m"
print "\033[1;32;40mWelCome Use SendMail By Python Script "
print "Please Create File 'emailList.xml' In Current Directory"
print "Email Address Split By ','"
print "Email Content Is In File 'mailcontent.html'"
print "==================== Power By Jason =====================\033[0m"
print "\033[1;31;40m=========================================================\033[0m"
print('')
readMail();