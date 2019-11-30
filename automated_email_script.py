import smtplib
import re 

'''Email file path'''
fileName = "emails.txt"

'''Open and read the contents of email txt file
and then put each email into a list'''
def readEmailsFromFile(fileName):
    validEmailFormat = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    file = open(fileName, "r")
    '''File in read mode + Email validation + creation of email list'''
    if(file.mode == "r"):
        contents = file.readlines()
        emailList = []
        for email in contents:
            if(re.search(validEmailFormat,email)):
                emailList.append(email)
    return emailList


'send emails retrieved from the list'
def sendEmail(emailList):
    conn = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    conn.ehlo()
    conn.login("your gmail", "your 16 digit app code")

    for emailPosition in range(len(emailList)):
        conn.sendmail("from email", emailList[emailPosition], 'Subject: Mail Subject' +
                      'test\n\nMailContent') 

'''read the file and send email'''
sendEmail(readEmailsFromFile(fileName))

