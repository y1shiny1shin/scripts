code = '''
96 F5 c6 f6 67 56 F5 57 77 F6 F5 46 56 F5 26 16 F6
'''
lst = ([i for i in code if i != '\n' and i != ' '])
lst_ = []
for i in range(1,len(lst),2):
    name = lst[i-1]+lst[i]
    lst_.append(name[::-1])
for i in range(len(lst_)):
    print(lst_[i],end=" ")

#结果:69 5F 6c 6f 76 65 5F 75 77 6F 5F 64 65 5F 62 61 6F