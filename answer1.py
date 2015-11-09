# -*- coding=utf-8 -*-
#DP思路求解，f(x) = f(x-1) + f(x-2)  (x > 3)

ResultMap = {}

def func(n):
    if n < 1:
        print 'params error'
        return
    for i in range(1, n + 1):
        if i == 1 or i == 2:
            ResultMap[i] = 1
        else:
            ResultMap[i] = ResultMap[i - 1] + ResultMap[i - 2]

if __name__ == '__main__':
    n = 40
    func(n)
    assert ResultMap.has_key(n)
    print ResultMap[n]
