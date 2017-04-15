# coding: utf-8
import os
import smtplib
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
    smtp.set_debuglevel(1)
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
            print email+"Sendding ..."
            print "Date : "+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            sendMail(email);
            f = open('sendmail.log', 'a')
            f.write(email+","+ '\n')
            f.close();
            print email+" Send Complete\n"
            print "------------------------"
            time.sleep(5)


content="";
filename = "mailcontent.html"
if os.path.exists(filename):
    print  ''
else:
    f = open('mailcontent.html', 'a')
    exit("mailcontent.html is empty!");

file_object = open(filename, 'r')
try:
    content = file_object.read()
finally:
    file_object.close()


#####################################################
smtpHost="smtp.gmail.com"
hostPort=465
sender = 'woshishui888888@gmail.com'
username = 'woshishui888888@gmail.com'
password = 'admin888'
subject="TESTmail"
auth="ssl"

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