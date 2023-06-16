import hashlib
import itertools

# Brute Force方式破解哈希值
def brute_force_hash(hash, charset, length):
    for guess in itertools.product(charset, repeat=length):
        guess = ''.join(guess)
        if hashlib.sha256(guess.encode()).hexdigest() == hash:
            return guess

    return None

# Dictionary Attack方式破解哈希值
def dictionary_attack_hash(hash, dictionary_file):
    with open(dictionary_file) as file:
        for password in file:
            password = password.strip()
            if hashlib.sha256(password.encode()).hexdigest() == hash:
                return password

    return None

# 获取需要破解的哈希值和对应的密码字典文件
hash = 'cf175e05c9459e951204e6be4e3e9e65bcefb6b27c8c4f0ed4677fba02b41022'
dictionary_file = 'dictionary.txt'
charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# 使用Brute Force方式尝试破解哈希值
password = None
for i in range(1, 7):  # 设置猜测密码长度范围
    password = brute_force_hash(hash, charset, i)
    if password:
        print(f"Password found using Brute Force: {password}")
        break

# 如果Brute Force方式尝试失败，则使用Dictionary Attack方式尝试破解哈希值
if not password:
    password = dictionary_attack_hash(hash, dictionary_file)
    if password:
        print(f"Password found using Dictionary Attack: {password}")
    else:
        print("Password not found")