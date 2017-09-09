# coding:utf-8
# 筛选法求素数
# 算法思路：
# 	某个数为素数，他的倍数都不是素数·mark
import math
MAX = 10000
mark = [True] * (MAX + 1)
list = []
for i in range(2,int(math.sqrt(MAX)) + 1):
    j = i
    k = j
    while j * k <= MAX:
        mark[j * k] = False
        k += 1
for i in range(2,MAX + 1):
    if mark[i] is True:
        print(i)