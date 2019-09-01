# -*- coding: utf-8 -*-
"""
Created on Wed May 29 11:35:33 2019

@author: Tang
"""
'''
简单选择排序（simple selection sort）:时间复杂度O(n^2)
通过n-i次关键字之间的比较，从n-i+1个记录中选出关键字最小的记录，并和第i（1<=i<=n)个记录进行交换。

通俗的说就是，对尚未完成排序的所有元素，从头到尾比一遍，记录下最小的那个元素的下标，也就是该元素的位置。再把该元素交换到当前遍历的最前面。其效率之处在于，每一轮中比较了很多次，但只交换一次。因此虽然它的时间复杂度也是O(n^2)，但比冒泡算法还是要好一点。
'''

class SQList:
    def __init__(self, lis=None):
        self.r = lis

    def swap(self, i, j):
        """定义一个交换元素的方法，方便后面调用。"""
        temp = self.r[i]
        self.r[i] = self.r[j]
        self.r[j] = temp

    def select_sort(self):
        """
        简单选择排序，时间复杂度O(n^2)
        """
        lis = self.r
        length = len(self.r)
        for i in range(length):
            minimum = i
            for j in range(i+1, length):
                if lis[minimum] > lis[j]:
                    minimum = j
            if i != minimum:
                self.swap(i, minimum)

    def __str__(self):
        ret = ""
        for i in self.r:
            ret += " %s" % i
        return ret

if __name__ == '__main__':
    sqlist = SQList([4, 1, 7, 3, 8, 5, 9, 2, 6, 0])
    sqlist.select_sort()
    print(sqlist)