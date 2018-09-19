'''
编写一个函数isIn，接受两个字符串作为参数，如果一个字符串是另一个字符串的一部分，返回True,否则返回False。提示：你可以使用内置的str类型的操作符in。
'''

def isIn(s1,s2):
    if s1 in s2:
        return True
    else:
        return False
print(isIn('ab','123ab79'))