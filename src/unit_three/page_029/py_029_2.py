'''
实际练习：
    在牛顿-拉弗森法的实现中添加一些代码，跟踪求平方根所用的迭代次数。在这段代码的基础上编写一个程序，
    比较牛顿-拉弗森法和二分查找的效率（你会发现牛顿-拉弗森法效率更高）。
'''

epsilon = 0.01
k = 24.0
guess = k / 2.0
a = 0
while abs(guess * guess - k) >= epsilon:
    guess = guess - (((guess ** 2) - k) / (2 * guess))
    a += 1
print('Square root of', k, 'is about', guess)
print('牛顿法迭代次数={}'.format(a))

x = 24.0
epsilon = 0.01
numGuesses = 0
low = 0.0
abs_x = abs(x)
high = max(1.0, abs_x)
ans = (high + low) / 2.0
b = 0
while abs(ans ** 2 - x) >= epsilon:
    numGuesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print(ans, 'is close to square root of', x)
print('二分法迭代次数={}'.format(numGuesses))
