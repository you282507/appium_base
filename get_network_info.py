#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random
import socket


def socket_port(ip, port):
    """
    Enter the IP and port number, scan to determine whether the port is occupied
    """
    socket.setdefaulttimeout(3) 
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(ip, u':', port, u'port is occupied')
            return False
        return True
    except Exception as error:
        print('error:', error)
        return False


def generate_unoccupied_port(ip, frequency=10):
    ports = random.randint(1024, 49151)
    while frequency > 0:
        if socket_port(ip, ports):
            return ports
        ports += 1
        frequency -= 1
    return False


def get_host_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception as error:
        print(error)
        return False
    finally:
        s.close()
    return ip
