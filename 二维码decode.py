from PIL import Image 

qr_code_bin = open('二维码.txt','r')

x,y = 45,45
qr_code_image = Image.new('RGB',(x,y))

for i in range(0,x):
    line = qr_code_bin.readline()
    for j in range(0,y):
        if line[j] == '0':
            qr_code_image.putpixel((i,j),(255,255,255))
        else:
            qr_code_image.putpixel((i,j),(0,0,0))

qr_code_image.show()