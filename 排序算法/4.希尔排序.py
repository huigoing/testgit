# -*- coding: utf-8 -*-
"""
Created on Wed May 29 13:00:43 2019

@author: Tang
"""
'''
希尔排序（Shell Sort）是插入排序的改进版本，其核心思想是将原数据集合分割成若干个子序列，
然后再对子序列分别进行直接插入排序，使子序列基本有序，最后再对全体记录进行一次直接插入排序。

这里最关键的是跳跃和分割的策略，也就是我们要怎么分割数据，间隔多大的问题。
通常将相距某个“增量”的记录组成一个子序列，这样才能保证在子序列内分别进行直接插入排序后得
到的结果是基本有序而不是局部有序。下面的例子中通过：increment = increment//2来确定“增量”的值。
'''
class SQList:
    def __init__(self, lis=None):
        self.r = lis

    def shell_sort(self):
        """希尔排序"""
        lis = self.r
        length = len(lis)
        increment = len(lis)
        while increment > 1:
            increment = increment//2
            for i in range(increment, length):
                if lis[i] < lis[i - increment]:
                    temp = lis[i]
                    j = i - increment
                    while j >= 0 and temp < lis[j]:
                        lis[j+increment] = lis[j]
                        j -= increment
                    lis[j+increment] = temp
                    print(lis)

    def __str__(self):
        ret = ""
        for i in self.r:
            ret += " %s" % i
        return ret

if __name__ == '__main__':
    sqlist = SQList([4, 1, 7, 3, 8, 5, 9, 2, 6, 123,0])
    sqlist.shell_sort()
    print(sqlist)
