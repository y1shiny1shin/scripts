normal_byte = open('flag.png','rb') #以二进制形式读取原文件的byte数据
new_byte = open('new.png','wb') #打开一个文件，以二进制的形式写入byte数据
new_byte = new_byte.write(normal_byte.read()[::-1]) 