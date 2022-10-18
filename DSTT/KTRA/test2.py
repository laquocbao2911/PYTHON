import numpy as np
import math

def req1(A):
    A = A.T
    result = []
    for i in range(len(A)):
        result.append(sum(A[i]))
    mx = max(result)
    ketqua = [i for i in range(len(A)) if sum(A[i])==mx]
    return ketqua

def req2(A):
    lst = []
    for i in range(len(A)):
        lst.append(A[i][i])
    re = []
    for i in lst:
        flag = 1
        if (i<2):
            flag = 0
        for p in range(2, i):
            if i % p == 0:
                flag = 0
                break
        if flag == 1:
            re.append(i)
    ketqua = sum(re)
    return ketqua

def req3(A):
    dic = {}
    for i in A:
        for j in i:
            if j%2==0 and j not in dic:
                dic[j] = 1
            elif j%2==0 and j in dic:
                dic[j] +=1
    dic = dict(sorted(dic.items(),key = lambda key:key[0]))
    mx = max(dic.values())
    temp = 0
    if dic == {}:
        temp = 1000
    else:
        temp = [key for key,value in dic.items() if value == mx][0]
    # result = np.where(A>0,[key for key,value in dict.items() if value == mx][0],1000)
    result = np.where(A>0,temp,A)
    return result

def req4(A,gioihan):
    A = np.where(A<gioihan,1,0)
    for hang in range(len(A)):
        for cot in range(len(A[hang])):
            
    return A
A = np.array([[1,3,4,5],[2,2,4,3],[-1,1,3,-6],[0,-4,-3,5]])
print(req4(A,2))