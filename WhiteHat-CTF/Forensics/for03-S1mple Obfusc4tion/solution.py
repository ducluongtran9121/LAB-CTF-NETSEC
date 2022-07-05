import base64
with open('text.txt','r') as f:
	lines = f.readlines()

messages = [chr(int(x.replace('\n', ''))) for x in lines]
message = ''.join(messages)
print(base64.b64decode(message))