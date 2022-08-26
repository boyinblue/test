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
HOST = 'server.de'
USERNAME = 'user'
PASSWORD = 'password'

server = imaplib.IMAP4(HOST) # connect
server.login(USERNAME, PASSWORD) # login
server.select('INBOX',readonly=True) # select mailbox aka folder

result, data = server.search(None, "ALL") # search emails

ids = data[0] # data is a list.
id_list = ids.split() # ids is a space separated string
latest_email_id = id_list[-1] # get the latest
result, data = server.fetch(latest_email_id, "(RFC822)") # fetch email

for response_part in data:
    if isinstance(response_part, tuple):
        msg = email.message_from_string(response_part[1])
        varSubject = msg['subject']
        varFrom = msg['from']
        varDate = msg['Date']

        print(varDate + " " + varFrom.split()[-1] + " " + varSubject)

server.close()
server.logout()
