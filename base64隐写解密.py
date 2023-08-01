# import base64

# b64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
# with open('telephone.txt', 'rb') as f:
#     flag = ''
#     bin_str = ''
#     for line in f.readlines():
#         stegb64 = str(line, "utf-8").strip("\n")
#         rowb64 = str(base64.b64encode(base64.b64decode(stegb64)), "utf-8").strip("\n")
#         offset = abs(b64chars.index(stegb64.replace('=', '')[-1]) - b64chars.index(rowb64.replace('=', '')[-1]))
#         equalnum = stegb64.count('=')  # no equalnum no offset
#         if equalnum:
#             bin_str += bin(offset)[2:].zfill(equalnum * 2)
#             # flag += chr(int(bin(offset)[2:].zfill(equalnum * 2), 2))
#             # print(flag) 这样写得不出正确结果
#         print([chr(int(bin_str[i:i + 8], 2)) for i in range(0, len(bin_str), 8)])

#-*other version*-

import base64

path = "d:\\downloads\\GXYCTF_2019_SXMgdGhpcyBiYXNlPw==\\"
Base64Char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def str_to_bin_fromBase64char(strings:str) -> int:
    result = ""
    for i in range(len(strings)):
        result += bin(Base64Char.find(strings[i]))[2:].zfill(6)
    return int(result)

file = open(path + "flag-2.txt","r")
result = ""

for i in range(66):
    data = file.readline().strip("\n")
    normal_code = base64.b64encode(base64.b64decode(data)).decode("utf-8").strip("=")
    stego_code = data.strip("=")
    two_gap = abs(str_to_bin_fromBase64char(normal_code[-4:]) - str_to_bin_fromBase64char(stego_code[-4:]))
    if data.count("=") == 1:
        result += str(two_gap).zfill(2)
    elif data.count("=") == 2:
        result += str(two_gap).zfill(4)
    elif data.count("=") == 3:
        result += str(two_gap).zfill(6)
print("[+] : "result)
