from PIL import Image

original_image = Image.open("arcaea.png")

width = original_image.width
height = original_image.height

result_image = Image.new("RGB",(width//12 ,height//12),(255 ,255 ,255))
for i in range(0,width,12):
    for j in range(0,height,12):
        data = original_image.getpixel((i ,j))
        result_image.putpixel((i//12 ,j//12),data)

result_image.save("result.png")

lsb_image = Image.open("result.png")
lsb_width = lsb_image.width
lsb_height = lsb_image.height
R_data = ""
G_data = ""
B_data = ""
for y in range(lsb_height):
    for x in range(lsb_width):
        R_data += bin(lsb_image.getpixel((x ,y))[0])[2:].zfill(8)[7]
        G_data += bin(lsb_image.getpixel((x ,y))[1])[2:].zfill(8)[7]
        B_data += bin(lsb_image.getpixel((x ,y))[2])[2:].zfill(8)[7]

file = open("flag.txt","wb")
flag_data = ""
for i in range(0 ,len(R_data)):
    flag_data += R_data[i] +G_data[i] +B_data[i]
for i in range(0 ,len(flag_data) ,8):
    file.write(int(flag_data[i:i+8] ,2).to_bytes(length=1 ,byteorder="big"))
    # print(chr(int(flag_data[i:i+8] ,2)),end="")
