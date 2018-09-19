'''
实际练习：
    编写一个程序，要求用户输入10个整数，然后输出其中最大的奇数。如果用户没有输入奇数，则输出一个消息进行说明。
'''

#循环从控制台输入程序
num_list = []
for i in range(10):
    num = int(input('第'+str(i+1)+'个数：'))
    num_list.append(num)

#遍历原列表，将其中的奇数添加到odd列表中
odd = []
for numb in num_list:
    if numb % 2 ==1:
        odd.append(numb)

#如果odd不为空
if odd:
    print(sorted(odd)[-1])
else:
    print("没有奇数")
