with open('misc05-Colorless summer.txt', 'r') as f:
	lines = f.readlines()

message = lines[0]

result=[]
cnt=0
for x in message:
	if x == '|':
		cnt+=1
	elif cnt > 0:
		result.append(cnt)
		cnt=0
flag=''
for x in result:
	flag += chr(x)

print(flag)