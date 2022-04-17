import string

z = "\x71\x11\x24\x59\x8d\x6d\x71\x11\x35\x16\x8c\x6d\x71\x0d\x39\x47\x1f\x36\xf1\x2f\x39\x36\x8e\x3c\x4b\x39\x35\x12\x87\x7c\xa3\x10\x74\x58\x16\xc7\x71\x56\x68\x51\x2c\x8c\x73\x45\x32\x5b\x8c\x2a\xf1\x2f\x3f\x57\x6e\x04\x3d\x16\x75\x67\x16\x4f\x6d\x1c\x6e\x40\x01\x36\x93\x59\x33\x56\x04\x3e\x7b\x3a\x70\x50\x16\x04\x3d\x18\x73\x37\xac\x24\xe1\x56\x62\x5b\x8c\x2a\xf1\x45\x7f\x86\x07\x3e\x63\x47"
a = [ord(i) for i in z]

def xor(x, y):
	return x ^ y

def pow2_to8(y):
	return sum(2 ** i for i in range(8 - y, 8))

def compute(x, y):
	y = y % 8;
	s = pow2_to8(y)
	s = (x & s) >> (8 - y)
	return (s + (x << y)) & 0x00FF

def decrypt_ciphertext(a, key):
	result = ""
	for i in range(len(a)):
		if i:
			if ord(result[i - 1]) & 1:
				tmp = compute(a[i], ord(key[i % len(key)]))
			else:
				tmp = xor(a[i], ord(key[i % len(key)]))
		else:
			tmp = xor(a[i], ord(key[i % len(key)]))
		result += chr(tmp)
	return result

def check(plaintext):
	n = 0
	for i in (plaintext):
		n += ord(i)
	if n == 8932:
		return 1
	return 0

def brute(a, key: str):
	for c in list(string.printable):
		new_key = key + c
		plaintext = decrypt_ciphertext(a, new_key)
		if plaintext[:len(new_key)] == "<html>"[:len(new_key)]:
			d = check(plaintext)
			if d == 1:
				print(new_key)
				print(plaintext)
			else:
				brute(a, new_key)

brute(a, '')
