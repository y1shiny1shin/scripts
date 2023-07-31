'''这个版本是完全逆转'''
normal_byte = open('flag.png','rb') #以二进制形式读取原文件的byte数据
new_byte = open('new.png','wb') #打开一个文件，以二进制的形式写入byte数据
new_byte = new_byte.write(normal_byte.read()[::-1]) 

'''这个版本是逐个逆转文件中的hex'''
#other version
file = open("Reverse.piz","rb").read()
new_file = open("result1.zip","wb")

result = b""
for byte in file:
    data = hex(byte)[2:].zfill(2)[::-1]
    result += bytes.fromhex(data)
new_file.write(result)

print("[+]运行结束")
'''
原理是将源文件以byte形式读取，再将byte转换成hex
将hex逆转后，再转换成byte形式写入
'''
