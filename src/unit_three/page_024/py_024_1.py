'''
实际练习：
    假设s是包含多个小数的字符串，由逗号隔开，如s = '1.23, 2.4, 3.123'。编写一个程序，输出s中所有数值的和。
'''

#method one

s = '1.23, 2.4, 3.123'
sum = 0.0
for i in map(lambda i: float(i), s.split(',')):
    sum += i
print(sum)

#method two

s = '1.23, 2.4, 3.123'
a = s.split(',')
t = 0
for i in a:
    t = t + float(i)
print(t)