#!/usr/bin/python

import httpagentparser

#Open file
fo = open ("gistfile1.txt", "r")

#Get browser into the dict
browsers = dict()
for line in fo:
    os_browser = httpagentparser.simple_detect(line)
    browser = os_browser[1].split(" ")[0]
    if browser in browsers.keys():
        browsers[browser] += 1
    else :
        browsers[browser] = 1

#Show result
for keys, values in browsers.items():
    print(keys, values)
