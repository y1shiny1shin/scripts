#先用Tshark提取出传输的键盘8位字节
normalKeys = {
    "04":"a", "05":"b", "06":"c", "07":"d", "08":"e",
    "09":"f", "0a":"g", "0b":"h", "0c":"i", "0d":"j",
    "0e":"k", "0f":"l", "10":"m", "11":"n", "12":"o",
    "13":"p", "14":"q", "15":"r", "16":"s", "17":"t",
    "18":"u", "19":"v", "1a":"w", "1b":"x", "1c":"y",
    "1d":"z","1e":"1", "1f":"2", "20":"3", "21":"4",
    "22":"5", "23":"6","24":"7","25":"8","26":"9",
    "27":"0","28":"<RET>","29":"<ESC>","2a":"<DEL>", "2b":"\t",
    "2c":"<SPACE>","2d":"-","2e":"=","2f":"[","30":"]","31":"\\",
    "32":"<NON>","33":";","34":"'","35":"<GA>","36":",","37":".",
    "38":"/","39":"<CAP>","3a":"<F1>","3b":"<F2>", "3c":"<F3>","3d":"<F4>",
    "3e":"<F5>","3f":"<F6>","40":"<F7>","41":"<F8>","42":"<F9>","43":"<F10>",
    "44":"<F11>","45":"<F12>","46":"<PRTSC>","47":"<SCR>","48":"<PAUSE>","49":"<INSERT>",
    "4a":"<HOME>","4b":"<PGUP>","4c":"<DEL FORWARD>","4d":"<END>","4e":"<PGDW>","4f":"<RIGHTARROW>",
    "50":"<LEFTARROW>","51":"<DOWNARROW>","52":"<UPARRWO>","00":"","":""}
shiftKeys = {
    "04":"A", "05":"B", "06":"C", "07":"D", "08":"E", 
    "09":"F", "0a":"G", "0b":"H", "0c":"I", "0d":"J", 
    "0e":"K", "0f":"L", "10":"M", "11":"N", "12":"O", 
    "13":"P", "14":"Q", "15":"R", "16":"S", "17":"T", 
    "18":"U", "19":"V", "1a":"W", "1b":"X", "1c":"Y", 
    "1d":"Z","1e":"!", "1f":"@", "20":"#", "21":"$", 
    "22":"%", "23":"^","24":"&","25":"*","26":"(",
    "27":")","28":"<RET>","29":"<ESC>","2a":"<DEL>", 
    "2b":"\t","2c":"<SPACE>","2d":"_","2e":"+","2f":"{","30":"}",
    "31":"|","32":"<NON>","33":"\"","34":":","35":"<GA>","36":"<",
    "37":">","38":"?","39":"<CAP>","3a":"<F1>","3b":"<F2>", 
    "3c":"<F3>","3d":"<F4>","3e":"<F5>","3f":"<F6>","40":"<F7>",
    "41":"<F8>","42":"<F9>","43":"<F10>","44":"<F11>","45":"<F12>",
    "46":"<PRTSC>","47":"<SCR>","48":"<PAUSE>","49":"<INSERT>",
    "4a":"<HOME>","4b":"<PGUP>","4c":"<DEL FORWARD>","4d":"<END>","4e":"<PGDW>","4f":"<RIGHTARROW>",
    "50":"<LEFTARROW>","51":"<DOWNARROW>","52":"<UPARRWO>","00":""}
f = open("data.txt","r")
flag = 0
result = ""
for i in range(174):
    file = f.readline().strip('\n')
    simple = file[4:6]
    if file[0:2] == "00":
        if normalKeys[simple] == "<DEL>" or normalKeys[simple] == "<DEL FORWARD>":
            result = result[:-1]
        elif normalKeys[simple] == "<CAP>":
            flag += 1
        elif flag % 2 != 0:
            result += normalKeys[simple].upper()
        elif flag % 2 == 0:
            result += normalKeys[simple]
    elif file[0:2] == "02" or file[0:2] == "20":
        if shiftKeys[simple] == "<DEL>" or shiftKeys[simple] == "<DEL FORWARD>":
            result = result[:-1]
        elif shiftKeys[simple] == "<CAP>":
            flag += 1
        elif flag % 2 != 0:
            result += shiftKeys[simple].lower()
        elif flag % 2 == 0:
            result += shiftKeys[simple]

print("here is ur result:\n",result)