import hashlib

def md5hash(flag: str):  
	result = hashlib.md5(flag.encode())
	return result.hexdigest()  

for cnt in range(10):
	for minute in range(14,16):
		for second in range(60):
			flag = "WhiteHat{" + str(cnt) + "_12042022-07:" + str(minute) + ":" + str(second) + "_282087703_longnte_21.2.1}"
			md5_hash = md5hash(flag)
			if md5_hash == "2f2fc213b8a42eefcee4301fdb0459d8":
				print(flag)
				break


