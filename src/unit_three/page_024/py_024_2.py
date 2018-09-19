'''
    近似解和二分查找，近似解位于实际解附近的一个常数范围内，这个常数我们称为epsilon。
'''
x = 25
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans*ans <= x:
    ans += step
    numGuesses += 1
print('numGuesses = ',numGuesses)
if abs(ans**2 - x) >= epsilon:
    print('Failed on squre root of', x)
else:
    print(ans,'is close to squre root of', x)



