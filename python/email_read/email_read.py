#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from email.parser import HeaderParser

import imaplib, email, re

list_response_pattern = re.compile(r'\((?P<flags>.*?)\) "(?P<delimiter>.*)" (?P<name>.*)')

def parse_list_response(line):
    flags, delimiter, mailbox_name = list_response_pattern.match(line).groups()
    return (flags, delimiter, mailbox_name)

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

result, data = server.search(None, "ALL") # search emails

ids = data[0] # data is a list.
id_list = ids.split() # ids is a space separated string
latest_email_id = id_list[-1] # get the latest
result, data = server.fetch(latest_email_id, "(RFC822)") # fetch email
content = data[0][1].decode('ascii')
#print("Data :", content)
msg = email.message_from_string(content)
#print("Msg :", msg)
varSubject = msg['Subject']
print("[Subject]", varSubject)
varFrom = msg['From']
print("[From]", varFrom)
varDate = msg['Date']
print("[Date]", varDate)

server.close()
server.logout()
