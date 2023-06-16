a = "884080810882108108821042084010421"
a = a.split("0")
flag = ''
for i in range(0, len(a)):
    str = a[i]
    sum = 0
    for i in str:
        sum += int(i)
    flag += chr(sum + 64)
print (flag)
