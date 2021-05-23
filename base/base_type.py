#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  python base type
"""

__author__ = 'Gary.Hu'

import unittest


class BaseTypeTest(unittest.TestCase):

    @staticmethod
    def test_str():
        print('---------- test for str ----------')
        print('''the is a test for string''')
        print('''the is a test for 中文''')

    @staticmethod
    def test_int():
        print('---------- test for int ----------')
        print(-8)
        print(0xff00)

    @staticmethod
    def test_float():
        print('---------- test for float ----------')
        print(1.23e9)
        print(1.2e-5)

    @staticmethod
    def test_boolean():
        print('---------- test for boolean ----------')
        print(True and False)
        print(True or False)

    @staticmethod
    def test_format():
        print('---------- test for str format  ----------')
        print('test format name : %s age : %s' % ('KEN', 100))
        print('test format name : {0} age : {1}'.format('KEN', 100))

    @staticmethod
    def test_list():
        print('---------- test for list  ----------')
        names = ['name1', 'ken', 'gary']
        print(names)
        print('append now.....')
        names.append('name-append')
        print(names)
        names.pop()
        print('pop now.....')
        print(names)

    @staticmethod
    def test_tuple():
        print('---------- test for tuple  ----------')
        names = ('name1', 'ken', 'gary')
        print(names)


if __name__ == '__main__':
    unittest.main()
