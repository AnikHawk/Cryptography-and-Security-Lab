.global your_asm_fn
.section .text

mp: .string "coolfood"
sec: .int 0xc105ed

your_asm_fn:

push	%ebp
mov	%esp,%ebp

push $mp
push $sec
push $0xacce55ed
call practice

leave
ret
