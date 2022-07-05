import base64

enc_flag = base64.b64decode('NFwcKxN4DxMGLVxFABUAADgQFgAqMgNRMQ89PAAbNyldXg4iF1xBJik=').decode('ascii')

flag = ''

key = 'c4u_v0ng}'

for i in range(len(enc_flag)):
	flag += chr(ord(key[i%len(key)]) ^ ord(enc_flag[i]))

print(flag)
#WhiteHat{Nh0_c0n_mu4_mua_h@_4nh_m0i_th4y_c4u_v0ng}

		


