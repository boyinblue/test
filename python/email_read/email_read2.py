#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from email.parser import HeaderParser
import imaplib, email, re

list_response_pattern = re.compile(r'\((?P<flags>.*?)\) "(?P<delimiter>.*)" (?P<name>.*)')

def parse_list_response(line):
    flags, delimiter, mailbox_name = list_response_pattern.match(line).groups()
    return (flags, delimiter, mailbox_name)

def email_login():
    # Add your data here
    HOST = 'imap.daum.net'
    PORT = 993
    USERNAME = input("ID : ")
    PASSWORD = input("PW : ")

    print("Step 1. Open SSL")
    server = imaplib.IMAP4_SSL(HOST, port=PORT, timeout=5) # connect
    print("Step 2. Login")
    server.login(USERNAME, PASSWORD) # login
    print("Step 3. Select INBOX")
    #server.select('INBOX',readonly=True) # select mailbox aka folder
    server.select()

    return server

def email_save(id, msg):
    from datetime import datetime
    
#    print("Date :", msg['Date'])
    try:
        datetime_obj = datetime.strptime(msg['Date'],
                        "%a, %d %b %Y %X %z (%Z)")
    except:
        datetime_obj = datetime.strptime(msg['Date'],
                        "%a, %d %b %Y %X %z")

    format_date = datetime_obj.strftime("%y%m%d_%H%M%S")
#    print("date =", format_date)

    with open('tmp/{}'.format(id), 'w') as file:
        file.write(msg['Subject'])

def email_read_by_id(server, id):
    #print("bid :", id)
    try:
        result, data = server.fetch(id, "(RFC822)") # fetch email
        content = data[0][1].decode('ascii')
        #print("Data :", content)
        msg = email.message_from_string(content)
    except:
        print("[Fetch Error]", id)
        msg = None

    return msg

def email_print(id, msg):
    print("=====================================")
    varSubject = msg['Subject']
    print("[{}] {}".format(id, varSubject))
    varFrom = msg['From']
    print("[From]", varFrom)
    varDate = msg['Date']
    print("[Date]", varDate)
    varContent = msg['Content']
    print("[Content]")
    print("")

def is_email_exist(id):
    import os

    if not os.path.isdir("tmp"):
        os.mkdir("tmp")

    if os.path.isfile("tmp/{}".format(id)):
        return True
    return False

def main():
    server = email_login()
    result, data = server.search(None, "ALL") # search emails

    ids = data[0] # data is a list.
    id_list = ids.split() # ids is a space separated string
    for bid in id_list:
        id = bid.decode()
        if is_email_exist(id):
            print("[{}] Skip!".format(id))
            continue
        msg = email_read_by_id(server, bid)
        if not msg:
            continue
        #print("Msg :", msg)

        email_print(id, msg)
        email_save(id, msg)

    server.close()
    server.logout()

if __name__ == "__main__":
    main()
