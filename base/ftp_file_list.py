#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    python-ftp-list
    Recursion query ftp file, You can decide whether to list files , or just list directory
"""
__author__ = "Gary.Hu"

import ftplib

scan_path_array = ["more1", "", "test1"]


def traverse(ftp, list_file=False, depth=0):
    result_list = {}
    if depth > 10:
        return ['depth > 10']
    for entry in (path for path in ftp.nlst() if path not in ('.', '..')):
        try:
            ftp.cwd(entry)
            result_list[entry] = traverse(ftp, list_file, depth + 1)
            ftp.cwd('..')
        except ftplib.error_perm:
            if list_file:
                result_list[entry] = "File"
            else:
                pass

    return result_list


def main():
    for scan_path in scan_path_array:
        ftp = ftplib.FTP("172.18.5.169")
        ftp.connect()
        ftp.login("ftpuser", "123456")
        ftp.set_pasv(True)
        ftp.encoding = 'GBK'
        ftp.cwd(scan_path)
        result = traverse(ftp, False)
        print(result)
        ftp.close()


if __name__ == '__main__':
    main()
