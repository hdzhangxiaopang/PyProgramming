'''
遍历字符串中的字符,并对字符串中的数字求和
'''
total = 0
for c in '1234567890':
    total = total + int(c)
print(total)