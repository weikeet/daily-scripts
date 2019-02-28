# -*- coding=utf-8 -*-
import getpass
import sys, tty, termios

if __name__ == "__main__":
    pwd = getpass.getpass('password: ')
    print pwd