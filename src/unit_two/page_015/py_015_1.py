'''
Python 3 中有一个input函数，可以直接接受用户输入。它可以使用一个字符串作为参数，显示在shell中作为提示信息，
然后等待用户输入，用户输入以回车键结束。用户输入的行信息被看做一个字符串，并成为这个函数的返回值。
'''

name = input('Enter your name:')
college = input('Enter you college:')
print('I am ' + name + ' graduated from ' + college)
