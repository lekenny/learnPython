#!/usr/bin/python3

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a,b = 0,1
while b < 10:
    print(b)
    a,b = b,a+b

# 手动输入一个人数
def fibs(n):
    a,b = 0,1
    result = []
    while a < n:
        result.append(a)
        a,b = b,a+b
    return result
n = int(input('请输入一个整数:\n'))
print(fibs(n))

# 请输入要生成的斐波纳契数列长度
def fibz(num):
    result = [0,1]
    for i in range(num - 2):
        result.append(result[-2]+result[-1])
    return result

n = int(input('请输入要生成的斐波纳契数列长度:\n'))
print(fibz(n))