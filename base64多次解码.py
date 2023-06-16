import base64

def decode(f):
	n = 0;
	while True:
		try:
			f = base64.b64decode(f)
			n += 1
		except:
			print('[+]Base64共decode了{0}次，最终解码结果如下:'.format(n))
			print(str(f,'utf-8'))
			break

if __name__ == '__main__':
	f = open('./base64.txt','r').read()
	decode(f)
