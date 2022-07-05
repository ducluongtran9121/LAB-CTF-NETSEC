def zero_to_one(bin_):
	str_ = ''
	for i in bin_:
		if i == '0': 
			str_ +='1'
		elif i == '1': 
			str_ += '0'
		else:
			str_ += i
	return str_

def convert(flag):
	bin_flag = ''
	i=0
	while i*8 < len(flag):
		bin_flag += flag[i*8:(i+1)*8-1]
		bin_flag += ' '
		i += 1
	
	return zero_to_one(bin_flag)

if __name__ == '__main__':
	flag = '01010000001011100010110000010110001101000110111000111100000101100000100000101100001001000001111000100000000110100001011001000000010000000011101000010100000101100100000000101100010000000011011000100000001000100001011001000000001110000011110000011010001101000000010'
	print(convert(flag))