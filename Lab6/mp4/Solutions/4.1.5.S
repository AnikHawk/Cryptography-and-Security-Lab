.global main
.section .text

.data
file_to_run: .string "/bin/sh"


main:
pushl %ebp
movl %esp, %ebp

movl $11, %eax                      # sys_execve
movl $file_to_run, %ebx              # file to execute       
movl $0, %ecx                       
movl $0, %edx                       
int  $0x80              

leave
ret
