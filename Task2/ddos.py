#!/usr/bin/python

import socket

valid_ip = []


def get_valid_ip():  # get google, bing, facebook ip
    valid_site = ['www.google.com.vn', 'www.facebook.com.vn', 'www.bing.com.vn']
    for site in valid_site:
        ai = socket.getaddrinfo(site, 80, 0, 0, 0)
        for element in ai:
            valid_ip.append(element[-1][0])
    return valid_ip


def is_valid_ip(ip):  # check if ip request google, face, bing
    if ip in valid_ip:
        return True
    else:
        return False


def get_ip_dict():  # get ip from access.log to ip_dict
    of = open('access.log', 'r')
    ip_dict = dict()
    for line in of:
        ip = line.split(' ')[0]
        if ip in ip_dict.keys():
            ip_dict[ip] += 1
        else:
            ip_dict[ip] = 1
    return ip_dict


def filter_ip(ip_dict=None):
    # add ip to block list
    if ip_dict is None:
        ip_dict = dict()
    block_ip_list = []
    for ip, time in ip_dict.items():
        if is_valid_ip(ip):
            continue
        if time > 120:
            block_ip_list.append(ip)
    return block_ip_list


def block(list_ip=None):
    count = 0
    if list_ip is None:
        list_ip = []
    for ip in list_ip:
        print ip


if __name__ == '__main__':
    get_valid_ip()
    block(filter_ip(get_ip_dict()))
