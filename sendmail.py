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
    msg['From'] = Header(sendername, 'utf-8').encode()+'<'+sender+'>' #_format_addr(u'tester<%s>' % sender)
    msg['To'] = _format_addr(u'<%s>' % receiver)
    # msg['Cc'] = _format_addr(u'<%s>' % receiver)
    #Create message html content
    att = MIMEText(content,'html','utf-8')
    #att["Content-Type"] = 'application/octet-stream'
    #att["Content-Type"] = 'application/alternative'
    msg.attach(att)
    # tls加密方式，通信过程加密，邮件数据安全，使用正常的smtp端口
    if auth == "ssl":
        smtp = smtplib.SMTP_SSL(smtpHost,hostPort)
        #mtp.ehlo()
        #print auth
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
    print name
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))
#sendMail(subject);
def readMail():
    print Sleep
    #exit()
    filename="emailList.xml"
    if os.path.exists(filename):
        message = 'Start SendMail Script'
    else:
        f = open('emailList.xml', 'a')
        print "emailList.xml is empty !"
        time.sleep(5)
        exit("emailList.xml is empty !");

    file_object = open(filename,'r')
    try:
        all_the_text = file_object.read()
    finally:
        file_object.close()

    if all_the_text == "":
        print "emailList.xml is empty !"
        time.sleep(5)
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
            print "sleep -----> "+Sleep
            time.sleep(float(Sleep))

open('mailcontent.html', 'a')
open('emailList.xml', 'a')


content="";
filename = "mailcontent.html"
if os.path.exists(filename):
    print  ''
else:
    f = open('mailcontent.html', 'a')
    print "mailcontent.html is not exit , we will create it!"
    time.sleep(5)
    exit("mailcontent.html is not exit , we will create it!");

file_object = open(filename, 'r')
try:
    content = file_object.read()
finally:
    file_object.close()
if content=="":
    print "mailcontent.html is empty!"
    time.sleep(5)
    exit("mailcontent.html is empty!");

#####################################################

config = ConfigParser.ConfigParser()
config.read("config.ini")

#print config.get("global", "startAuth")
#print config.get("global", "username")
Sleep=config.get("global", "sleep")
startAuth=config.get("global", "startAuth")
isdebug=config.get("global", "startAuth")
smtpHost=config.get("global", "smtpHost")
hostPort=config.get("global", "hostPort")
sendername=config.get("global", "sendername")
sender = config.get("global", "sender")
username = config.get("global", "username")
password =  config.get("global", "password")
subject=config.get("global", "subject")
auth=config.get("global", "auth")


#print proccessSleep

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