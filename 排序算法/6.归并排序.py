# -*- coding: utf-8 -*-
"""
Created on Wed May 29 17:15:11 2019

@author: Tang
"""

'''
归并排序（Merging Sort）：建立在归并操作上的一种有效的排序算法,该算法是采
用分治法（Divide and Conquer）的一个非常典型的应用。将已有序的子序列合并，
得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，
称为二路归并。
'''


def msort(s):
        if len(s)<=1:
             return s
        m = len(s)//2
        left=msort(s[:m])
        right=msort(s[m:])
        return  merge(left, right)

def merge(left,right):
        j = 0
        i=0
        result=[]
        while i <len(left) and j <len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    
a=[4, 1, 7, 3, 8, 5, 9, 2, 6, 0, 12, 77, 34, 23]
print(msort(a))

