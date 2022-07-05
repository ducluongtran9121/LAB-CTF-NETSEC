import base64
import string

def seek(flag,secret):
    result = ""
    brute = string.printable
    for i in range(len(flag)):
	    for char in brute:
		    if (char.isupper()):
		        tmp = chr((ord(char) + pow(-1,i)*secret - 65) % 26 + 65)
		    elif (char.islower()):
		        tmp = chr((ord(char) + pow(-1,i)*secret - 97) % 26 + 97)
		    elif (char.isdecimal()):
		        tmp = chr((ord(char) + pow(-1,i)*secret - 48) % 10 + 48)
		    else:
		        tmp = char
		    if tmp == flag[i]:
		    	result += char
    return result

def get_hidden_flag(enc_flag):
	result = []
	enc_flag = enc_flag.split(' ')
	enc_flag_array = [int(x) for x in enc_flag]
	result.append(enc_flag_array[0])
	i=1
	while i<len(enc_flag_array)-1:
		result.append(enc_flag_array[i] + enc_flag_array[i+1]*result[-1])
		i += 2
	tmp = ''.join([chr(x) for x in result]) 
	text = base64.b64decode(tmp).decode('ascii')
	bytes_object = bytes.fromhex(text)
	ascii_string = bytes_object.decode("ascii")
	return ascii_string
	

enc_flag = '78 6 1 65 0 57 1 78 0 28 1 99 0 23 1 78 0 9 1 2 1 33 1 78 0 6 1 81 0 39 1 78 0 9 1 2 1 50 0 40 1 16 1 82 0 25 1 77 0 45 1 103 0 49 0 41 1 16 1 77 0 42 1 78 0 6 1 23 1 15 1 79 0 5 1 77 0 50 0 28 1 28 1 1 1 15 1 79 0 68 0 31 1 53 0 25 1 9 1 2 1 49 0 29 1 44 1 77 0 50 0 27 1 45 1 107 0 50 0 29 1 5 1 77 0 52 0 52'
# enc_flag = '78 6 1 65 0 57 1 78 0 25 1 61 0 0 1 61'
secret = 5
print(seek(get_hidden_flag(enc_flag), secret))