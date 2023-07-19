'''
思路就是用getpixel将对应坐标的像素点提取为rgb像素，再将rgb分别转化成二进制；
提取到rgb最后一位，再组合
'''

from PIL import Image 
rrr = Image.open("rrr.png")
ggg = Image.open("ggg.png")
bbb = Image.open("bbb.png")

height = rrr.height
width = rrr.width

rrr_list = ""
ggg_list = ""
bbb_list = ""

file = open("rgb.bpg","wb")
for j in range(20):
    for i in range(width):
        rrr_list += bin(rrr.getpixel((i ,j))[0])[2].zfill(8)[7]
        ggg_list += bin(ggg.getpixel((i ,j))[1])[2].zfill(8)[7]
        bbb_list += bin(bbb.getpixel((i ,j))[2])[2].zfill(8)[7]
print(rrr_list)

for i in range(0,len(rrr_list),8):
    file.write(int(rrr_list[i:i+8],2).to_bytes(1,byteorder="big"))
    file.write(int(ggg_list[i:i+8],2).to_bytes(1,byteorder="big"))
    file.write(int(bbb_list[i:i+8],2).to_bytes(1,byteorder="big"))

file.close()
bbb.close()
rrr.close()
ggg.close()
