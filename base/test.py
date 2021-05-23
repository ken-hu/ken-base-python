#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  demo
"""

__author__ = 'Gary.Hu'

import requests


def main():
    url = 'http://www.cntour.cn/'
    strhtml = requests.get(url)
    print(strhtml.text)


if __name__ == '__main__':
    main()
