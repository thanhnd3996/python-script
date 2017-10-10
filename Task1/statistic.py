#!/usr/bin/python

import httpagentparser

count = 0  # count the number of user-agent

fo = open("gistfile1.txt", "r")  # Open file

# Get browser into the dict
browsers = dict()
for line in fo:
    count += 1
    os_browser = httpagentparser.simple_detect(line)
    browser = os_browser[1].split(" ")[0]
    if browser in browsers.keys():
        browsers[browser] += 1
    else:
        browsers[browser] = 1

# Show result
for key, value in browsers.items():
    print key + ": %f" % ((value / float(count)) * 100)
