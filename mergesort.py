#!/usr/bin/env python
# -*- coding: utf-8 -*-
def MergeSort(A):
    if len(A) == 1:
        return A

    # 2つに分割した後、小さい配列をソート
    m = len(A)//2
    A_Dash = MergeSort(A[0:m])
    B_Dash = MergeSort(A[m:len(A)])

    # この時点で以下の2つの配列がソートされている
    # 列A'に相当するもの[A_Dash[0],A_Dash[1],...,A_Dash]
    # 列 B' に相当するもの [B_Dash[0], B_Dash[1], ..., B_Dash[len(A)-m-1]]
    # 以下がマージ

    c1 = c2 = 0
    C = []
    while(c1 < len(A_Dash) or c2 < len(B_Dash)):
        if c1 == len(A_Dash):
            # 列A'が空の場合
            C.append(B_Dash[c2])
            c2 += 1
        elif c2 == len(B_Dash):
            # 列B'が空の場合
            C.append(A_Dash[c1])
            c1 += 1
        else:
            if A_Dash[c1] <= B_Dash[c2]:
                C.append(A_Dash[c1])
                c1 += 1
            else:
                C.append(B_Dash[c2])
                c2 += 1
    return C

N = int(input())
A = list(map(int,input().split()))


Answer = MergeSort(A)
print(Answer)