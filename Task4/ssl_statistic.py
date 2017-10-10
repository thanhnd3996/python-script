#!/usr/bin/python

of = open('gistfile1.txt', 'r')

ssl_list = dict()
count = 0  # count the number of ssl

for line in of:
    count += 1
    protocol = line.split(' ')[3]
    cipher = line.split(' ')[4]
    ssl = protocol + "/" + cipher
    if ssl in ssl_list.keys():
        ssl_list[ssl] += 1
    else:
        ssl_list[ssl] = 1

for ssl, value in ssl_list.items():
    print ssl + ": %f" % ((value / float(count)) * 100)
