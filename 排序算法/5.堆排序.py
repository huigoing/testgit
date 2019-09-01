# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:22:17 2019

@author: Tang
"""

'''
堆是具有下列性质的完全二叉树：
 每个分支节点的值都大于或等于其左右孩子的值，称为大顶堆；
 每个分支节点的值都小于或等于其做右孩子的值，称为小顶堆；
 因此，其根节点一定是所有节点中最大（最小）的值。
堆排序（Heap Sort）就是利用大顶堆或小顶堆的性质进行排序的方法。堆排序的总体时间复杂度为O(nlogn)。
（下面采用大顶堆的方式）

其核心思想是：将待排序的序列构造成一个大顶堆。此时，整个序列的最大值就是堆的根节点。
将它与堆数组的末尾元素交换，然后将剩余的n-1个序列重新构造成一个大顶堆。反复执行前面的操作，
最后获得一个有序序列。
'''
class SQList:
    def __init__(self, lis=None):
        self.r = lis

    def swap(self, i, j):
        """定义一个交换元素的方法，方便后面调用。"""
        temp = self.r[i]
        self.r[i] = self.r[j]
        self.r[j] = temp

    def heap_sort(self):
        length = len(self.r)
        i = int(length/2)-1
        # 将原始序列构造成一个大顶堆
        # 遍历从中间开始，到0结束，其实这些是堆的分支节点。
        while i >= 0:
            self.heap_adjust(i, length-1)
            print(self.r)
            i -= 1
        # 逆序遍历整个序列，不断取出根节点的值，完成实际的排序。
        j = length-1
        while j > 0:
            # 将当前根节点，也就是列表最开头，下标为0的值，交换到最后面j处
            self.swap(0, j)
            # 将发生变化的序列重新构造成大顶堆
            self.heap_adjust(0, j-1)
            j -= 1

    def heap_adjust(self, s, m):
        """核心的大顶堆构造方法，维持序列的堆结构。"""
        lis = self.r
        temp = lis[s]
        i = 2*s+1
        #print(s,i)
        while i <= m:
            if i < m and lis[i] < lis[i+1]:
                i += 1
            if temp >= lis[i]:
                break
            lis[s] = lis[i]
            s = i
            i=i*2+1
        lis[s] = temp

    def __str__(self):
        ret = ""
        for i in self.r:
            ret += " %s" % i
        return ret

if __name__ == '__main__':
    sqlist = SQList([4, 1, 7, 3, 8, 5, 9, 2, 6, 0, 123, 22])
    sqlist.heap_sort()
    print(sqlist)

