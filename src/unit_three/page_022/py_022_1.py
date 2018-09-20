# x = 4
# for i in range(0, x):
#     print(i)

'''
output
0
1
2
3
'''

# x = 4
# for i in range(0, x):
#     print(i)
#     x = 5


'''
如果在循环中改变x的值，能否影响迭代次数？ 答案是‘不能’。在for循环那行代码中，range函数的参数在循环的第一次迭代之前已经被解释器求值，
随后的迭代中不会再次求值。
'''
x = 4
for j in range(x):
    for i in range(x):
        print(i)
        x = 2

'''
output
0
1
2
3
0
1
0
1
0
1
'''

'''
注：因为外层循环中的range函数只被求值一次，而内层循环中的range函数则在每次执行内层for语句时都被求值。
'''