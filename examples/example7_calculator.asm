.data
Question1:
	.asciiz	"Please enter an integer: "
Question2:
	.asciiz	"Please enter an operation (+,-,*,/): "
Right:
	.asciiz	"Thank you. "
Overflow:
	.asciiz	"I'm sorry, that would overflow."
Div_By_0:
	.asciiz "I'm sorry, you can't divide by zero."

Buffer:
	.space 4

.text
main:	
	la 	$a0, Question1	#load the address Question and store it into $a0
	jal 	display_question
	jal	get_int
	move	$s0, $v0	#Store the first operand in $s0
	
	la	$a0, Question2
	jal	display_question
	jal	get_operator
	
	lb	$s2, 0($a0)	#Operator in $s2
	
	la	$a0, Question1
	jal	display_question
	jal	get_int
	move	$s1, $v0	#Store the second operand in $s1
	
	move	$a0, $s0
	move	$a1, $s2
	move	$a2, $s1
	li	$v1, 0
	jal	operate

	move	$a0, $s0
	move	$a1, $s2
	move	$a2, $s1
	move	$a3, $v0
	jal	display_end

	jal	exit		#Exit
	
operate:	#$v0 will be the result if it succeeds. System will end if not.
#Args: $a0 is first operand, $a1 is operator, $a2 is second operand
	li      $t0, 43
	beq 	$a1, $t0, plus
	li      $t0, 45
	beq 	$a1, $t0, minus
	li      $t0, 42
	beq 	$a1, $t0, multiply
	li      $t0, 47
	beq 	$a1, $t0, divide
	jal	exit	#If all fails, exit
	
plus:
	addu  	$v0, $a0, $a2	#Add the two
	#Only time there is overflow is when both operators have a different sign from the result
	xor	$t0, $a0, $v0	#High bit will be 1 if different
	xor	$t1, $a2, $v0	#High bit will be 1 if different
	and	$t0, $t0, $t1	#High bit will be 1 if both are different
	bltz 	$t0, overflow	#If high bit is 1, then the number is less than 0. Therefore overflow
	jr	$ra		#Else return

minus:
	subu	$v0, $a0, $a2
	#Only time there is an overflow is when one operator is a different sign from the result
	not	$t1, $a2	#Flip the second operator (pos - neg = pos) to make them the same
	xor	$t0, $a0, $v0	#High bit will be 1 if different
	xor	$t1, $t1, $v0	#High bit will be 1 if different
	and	$t0, $t0, $t1	#High bit will be 1 if both are different
	bltz 	$t0, overflow	#If high bit is 1, then the number is less than 0. Therefore overflow
	jr	$ra		#Else Return


multiply:
	mult 	$a0, $a2	#Multiply the two
	mfhi	$t0		#Get the high
	mflo	$v0		#Get the result
	li		$t1, 4294967295
	beq	$t0, $t1,multiply_cont
	beq	$t0, $zero,multiply_cont
	j	overflow	#If the high bits are not equal to 0xffffffff or 0x00000000 then it has overflown
multiply_cont:
	xor	$t0, $v0, $t0	#See if these have different signs
	bltz	$t0, overflow
	jr	$ra
	
divide:
	beqz	$a2, divide_by_zero		#Divide by zero
	li      $t3, 0x80000000
	bne 	$a0, $t3, no_div_overflow #If a0 isn't the largest signed number, we can't have an overflow
	li      $t3, -1
	beq 	$a2, $t3, overflow		#If a0 is the largest signed number and a2 is -1, we overflow
	
no_div_overflow:
	div	$a0, $a2
	mflo	$v0
	mfhi	$v1
	jr	$ra
	
divide_by_zero:
	la	$a0, Div_By_0
	jal	display_question
	jal	exit
	
overflow:
	la	$a0, Overflow
	jal	display_question
	jal	exit
	
display_question:		#Mutates $v0
	li	$v0, 4
	syscall
	jr	$ra

get_int:			#Result is in $v0
	li	$v0, 5
	syscall
	jr	$ra
	
print_int:
	li	$v0, 1
	syscall
	jr	$ra
	
print_char:
	li	$v0, 11
	syscall
	jr	$ra

get_operator:			#Result pointer in $a0
	li	$v0, 8		#code for reading a string
	la	$a0, Buffer	#Load input buffer address
	li	$a1, 4		#Set maximum chars to 4 (Character and null terminator)
	syscall
	jr	$ra
	
compare:			#v0 is 1 if true, 0 if false
	li	$v0, 0
	beq 	$a0, $a1, compare_equal
	jr	$ra
compare_equal:
	li	$v0, 1
	jr	$ra
	
display_end:
	move	$t0, $a0	#Store $a0 for later
	move	$t1, $a1
	move	$t2, $a2
	move	$t3, $a3
	move	$t4, $ra
	la	$a0, Right
	jal	display_question
	move	$a0, $t0
	jal	print_int	#Print the first int
	li	$a0,	32	#Space
	jal	print_char
	move	$a0, $t1	#Print the operator
	jal	print_char
	li	$a0,	32	#Space
	jal	print_char
	move	$a0, $t2
	jal	print_int	#Print the second int
	li	$a0,	32	#Space
	jal	print_char
	li	$a0,	61	#Space
	jal	print_char
	li	$a0,	32	#Space
	jal	print_char
	move	$a0, $t3
	jal	print_int	#Print the answer
	bnez 	$v1, remainder
	jr	$t4
remainder:
	li	$a0,	32	#Space
	jal	print_char
	li	$a0,	114	#r
	jal	print_char
	li	$a0,	32	#Space
	jal	print_char
	move	$a0, $v1
	jal	print_int	#Print the remainder
	jr	$t4
	
exit:
	li	$v0, 10
	syscall			#Exit cleanly