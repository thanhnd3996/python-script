#!/usr/bin/python

of = open('gistfile1.txt', 'r')

protocol_list = dict()
cipher_list = dict()

for line in of:
    time = line.split(' ')[0]
    host = line.split(' ')[1]
    protocol = line.split(' ')[3]
    cipher = line.split(' ')[4]
    if protocol in protocol_list.keys():
        protocol_list[protocol] += 1
    else:
        protocol_list[protocol] = 1
    if cipher in cipher_list.keys():
        cipher_list[cipher] += 1
    else:
        cipher_list[cipher] = 1

count = 0 # count the number of protocol/cipher
for protocol in protocol_list:
    for cipher in cipher_list:

