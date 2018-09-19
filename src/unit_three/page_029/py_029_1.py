'''
    如果p是个多项式，r是个实数，我们就可以用p(r)表示当x = r时多项式的值。多项式p的根就是方程p = 0的解，也就是实数r,使得p(r)=0。
    例如，‘求24的近似平方根’这个问题可以用公式表示为：找到一个x,使得x^2 - 24 ≈0 。

    牛顿证明了一个定理：如果存在一个值guess是多项式p的根的近似值，那么guess - p(guess)/p'(guess)就是一个更好的近似值，其中p'是p的一次导数。

    对于任意的常数k和任意的系数c,多项式cx^2 + k的一次导数是2cx。 例如，x^2 - k 的一次导数是2x。因此，如果当前的猜测是y，那么可以选择y - (y^2 -k)/2y作为下一个猜测。
    这种方式称为逐次逼近。
'''

epsilon = 0.01
k = 24.0
guess = k / 2.0
while abs(guess * guess - k) >= epsilon:
    guess = guess - (((guess ** 2) - k) / (2 * guess))
print('Square root of', k, 'is about', guess)
