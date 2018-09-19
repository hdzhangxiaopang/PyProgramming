'''
实际练习：1. page_026,如果语句x = 25被替换为x = -25,代码会如何运行？
        2.  如何修改page_026中的代码，才能求出一个数的立方根？这个数既可以是正数，也可以是负数。（提示：修改low保证答案位于待查找区域。）
'''

# 1. 程序进入无限循环

x = -25
epsilon = 0.01
numGuesses = 0
x_abs = abs(x)
low = 0.0
high = max(1.0, x_abs)
ans = (high + low) / 2.0
while abs(ans ** 3 - x_abs) >= epsilon:
    print('low =', low, 'high=', high, 'ans=', ans)
    numGuesses += 1
    if ans ** 3 < x_abs:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print('numGuesses=', numGuesses)
if x < 0:
    print(-ans, 'is close to squre root of', x)
else:
    print(ans, 'is close to squre root of', x)
