'''
实际练习：
    编写一个程序，要求用户输入一个整数，然后输出两个整数root和pwr,满足0 < pwr < 6,并且root**pwr等于用户输入的整数。
    如果不存在这样一对整数，则输出一条消息进行说明。
'''
r = int(input('input an integer:'))
root = 0
i = 0
for pwr in range(1,6):
    result = -1
    while result < abs(r):
        root += 1
        result = root**pwr
    if result == abs(r):
        if r < 0:
            root = -root
        print('root:{},pwr:{}'.format(root,pwr))
        i += 1
    root = 0
if i:
    print('总共有{}种输出结果'.format(i))
else:
    print('未发现存在这样的整数')
