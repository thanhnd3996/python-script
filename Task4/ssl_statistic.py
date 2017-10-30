#!/usr/bin/python
from datetime import datetime


of = open('gistfile1.txt', 'r')

ssl_list = dict()
count = 0  # count the number of ssl
now = str(datetime.today())[0:16]

for line in of:
    count += 1
    request_time = line.split(' ')[0][0:16].replace("T", " ")

    if request_time == now:
        protocol = line.split(' ')[3]
        cipher = line.split(' ')[4]
        ssl = protocol + "/" + cipher
        if ssl in ssl_list.keys():
            ssl_list[ssl] += 1
        else:
            ssl_list[ssl] = 1

for ssl, value in ssl_list.items():
    print ssl + ": %f" % ((value / float(count)) * 100)
