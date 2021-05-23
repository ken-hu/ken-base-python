#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 的那两个整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

你可以按任意顺序返回答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
__author__ = "Gary.Hu"


def two_sum(nums: [int], target: int) -> [int]:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []


def two_sum_2(nums: [int], target: int) -> [int]:
    hashtable = dict()
    for i, num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num], i]
        hashtable[nums[i]] = i
    return []


if __name__ == '__main__':
    res = two_sum([1, 2, 3], 5)
    print(res)

    res = two_sum_2([2, 3, 5], 5)
    print(res)
