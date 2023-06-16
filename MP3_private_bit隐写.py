# import re
# import binascii
# n = 235986 #用010打开后的文件内容起始位置，"struct MPEG FRAME mf[0]"转化为10进制
# result = ''
# fina = ''
# number = 0
# list = [0,1,26,50,75,99,124,148,173,197,222,246,271,295,320,344,369,393,418]
# file = open('1.mp3','rb')
# while n < 1369844 :
#     file.seek(n,0)
#     if number in list:
#         n += 417
#     else:
#         n += 418
#     file_read_result = file.read(1)
#     read_content = bin(ord(file_read_result))[-1]
#     result = result + read_content
#     number += 1
# #print result

# fina = ''
# textArr = re.findall('.{'+str(8)+'}', result)
# # textArr.append(result[(len(textArr)*8):])
# for i in textArr:
#     fina = fina + chr(int(i,2)).strip('\n')
# print (fina)

# import re
# import binascii
# n = 235986
# result = ''
# fina = ''
# file = open('1.mp3','rb')
# while n < 1369844 :
#     file.seek(n,0)
#     n += 417
#     file_read_result = file.read(1)
#     read_content = bin(ord(file_read_result))[-1]
#     result = result + read_content
# print (result)


import re
n = 235986
result = ''
number = 0
file = open('1.mp3', 'rb')
l = []
while n < 1369844 :
    file.seek(n, 0)
    '''
    file.seek(n,0) ,移动光标到从头开始的第n位;
    seek(n,1),移动光标到从当前位置移动n位;
    seek(n,2),移动光标到从末尾开始移动n位;
    '''
    head = file.read(1)
    padding = '{:08b}'.format(ord(head))[-2]
    # print(padding,end="---------------------------------------------\n")
    result += '{:08b}'.format(ord(head))[-1]
    # print(len(result),end="--------------------------------------\n")
    if padding == "0":
        n += 417
    else:
        n += 418
    # file.seek(n, 0)
# 拼接
flag = ''
textArr = re.findall('.{' + str(8) + '}', result)
 
for i in textArr:
    flag = flag + chr(int(i, 2)).strip('\n')
print(flag)