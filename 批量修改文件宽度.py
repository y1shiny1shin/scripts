import os
import binascii
import struct
bp = open("white.jpg", "rb").read()    
for i in range(512,1500):
    png_name='white'+str(i)+'.jpg'#我是建立一个文件夹，可以不写前面的文件夹路径。
    png=open(png_name,"wb")
    data=bp[:165] + struct.pack('>h' ,i)+bp[167:]#这里可以直接写成bp[:16] + struct.pack('>i', i)+bp[20:]，我是把高度单独写出来了。
    png.write(data)
    png.close()
''''>h'是打包成两个字节；
    '>i'是打包成四个字节；
    JPG文件宽高是两个字节，PNG图片是四个字节
    JPG文件高的位置:[163:165] 宽的位置:[165:167]
    PNG文件高的位置:[20:24] 宽的位置:[16:20]
'''

# import zlib
# import struct
# filename = 'white.jpg'
# with open(filename, 'rb') as f:
#     all_b = f.read()
#     #w = all_b[159:161]
#     #h = all_b[157:159]
#     for i in range(512,1200):
#         name = str(i) + ".jpg"
#         f1 = open(r"./output/" + name,"wb")
#         im = all_b[:165]+struct.pack('>h',i)+all_b[167:]
#         f1.write(im)
#         f1.close()