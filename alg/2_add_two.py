#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0开头。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
实例
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
"""
__author__ = "Gary.Hu"


def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    num0 = l1[0] + l2[0]
    num1 = l1[1] + l2[1]
    num2 = l1[2] + l2[2]
    lys = [num0, num1, num2]
    print('lys ==> ' + lys.__str__())
    for inx, y in enumerate(lys):
        test = y
        if y == 10:
            test = 1
        elif y > 10:
            test = y % 10
        next_inx = inx - 1
        if next_inx > 0:
            lys[inx] = test
            lys[next_inx] = lys[next_inx] + test
            print(inx.__str__() + 'lys ==> ' + lys.__str__())
    return lys


if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    res = add_two_numbers(l1, l2)
    print(res)
