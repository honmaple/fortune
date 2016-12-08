#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: fortune.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-06 22:58:57 (CST)
# Last Update:星期四 2016-12-8 23:3:36 (CST)
#          By:
# Description:
# **************************************************************************
import os
import random


def get_random_file():
    dir = os.path.join(os.path.dirname(__file__), 'data')
    files = os.listdir(dir)
    files = [f for f in files if not f.endswith('.dat')]
    fortune_file = random.choice(files)
    fortune_file = os.path.abspath(os.path.join(dir, fortune_file))
    return fortune_file


def get_random_forturn(file):
    results = []
    result = ''
    with open(file) as fp:
        for line in fp:
            if line == '%\n':
                results.append(result)
                result = ''
            else:
                result += line
    result = random.choice(results)
    return result


def show():
    fortune_file = get_random_file()
    try:
        fortune = get_random_forturn(fortune_file)
    except UnicodeDecodeError:
        fortune = 'Hello World!'
    return fortune
