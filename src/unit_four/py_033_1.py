'''
编写一个函数isIn，接受两个字符串作为参数，如果一个字符串是另一个字符串的一部分，返回True,否则返回False。提示：你可以使用内置的str类型的操作符in。
'''


def isIn(s1, s2):
    if s1 in s2:
        return True
    else:
        return False


print(isIn('ab', '123ab79'))

'''
关键字参数和默认值
在Python中，有两种方法可以将形参绑定到实参。最常用的方法是使用位置参数，即第一个形参绑定到第一个实参，第二个形参绑定到第二个实参，
依次类推。Python还支持关键字参数：形参根据名称绑定到实参。

'''


def printName(firstName, lastName, reverse):
    if reverse:
        print(lastName, firstName)
    else:
        print(firstName, lastName)


printName('zhangsan', 'lisi', False)
printName('zhangsan', 'lisi', reverse=False)
printName('zhangsan', lastName='lisi', reverse=False)
printName(lastName='zhangsan', firstName='lisi', reverse=False)

'''
尽管关键字参数可以在实参列表中以任意顺序出现，但是将关键字参数放在非关键字参数后面是不合法的。

printName('zhangsan', lastName='lisi', False)   //报错

关键字参数经常与默认参数值结合使用。例如下面代码：

def printName(firstName, lastName, reverse = False):
    if reverse:
        print(lastName, firstName)
    else:
        print(firstName, lastName)
        

允许不指定所有参数便可以调用函数，例如：
printName('zhangsan', 'lisi')

'''
