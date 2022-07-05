import string

def cal_flag(flag):
	output=[]
	for i in range(len(flag)):
	    temp = ord(flag[i])**17%3233
	    output.append(temp)
	print(output)

def dec_flag(enc_flag):
	flag=''
	brute = string.printable
	for i in range(len(enc_flag)):
		for x in brute:
			tmp = ord(x)**17%3233
			if tmp==enc_flag[i]:
				flag+=x
	print(flag)

enc_flag = [604, 2170, 3179, 884, 1313, 3000, 1632, 884, 855, 3179, 119, 1632, 2271, 119, 612, 2412, 2185, 2923, 2412, 1632, 2271, 2271, 1313, 2412, 119, 3179, 119, 2170, 1632, 2578, 1313, 119, 2235, 2185, 119, 745, 3179, 1369, 1313, 1516]

if __name__ == '__main__':
	dec_flag(enc_flag)