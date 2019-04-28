	.data
	intPrompt:	.asciiz "\nPlease enter an integer: "
	opPrompt:	.asciiz "Please enter an operation (+,-,*,/): " 
	oflow: 		.asciiz "I'm sorry that would overflow."
	divide0:	.asciiz "I'm sorry, you cannot divide by 0."
	result:		.asciiz "Thank you. "
	remainder:	.asciiz " r "
	space:		.asciiz " = "
	a1 : 		.word 0
    	a2 : 		.word 0
    	op:  		.byte '-'
#-------------------------
#------Calculator App-----
#---Author: Jiman Kim-----
#-------------------------	
	.text
main:	addi 	$sp,$sp,-16
	sw	$a0, 0 ($sp)
	sw	$s0, 4 ($sp)
	sw	$s1, 8 ($sp)
	sw	$ra, 12 ($sp)

	#Prints 1st int
	li	$v0, 4
	la	$a0, intPrompt
	syscall 
	
	#Reads 1st int
	li	$v0, 5
	syscall	
	sw 	$v0 a1
	
	#Prints Operator
	li 	$v0, 4
	la	$a0, opPrompt
	syscall
	
	#Reads Operator
	li 	$v0,12
	syscall
	sw 	$v0 op
	
	#Prints 2nd int
	li 	$v0, 4
    	la 	$a0, intPrompt
    	syscall

	#Reads 2nd int
    	li 	$v0,5        
        syscall
    	sw 	$v0 a2
	
	#Loads in the ints and operator
    	lw 	$s0 a1
     	lw	$s1 a2
    	lw	$s2 op
	
	#Checks to see which operator to do
	li	$t3, '+'
	li	$t4, '-'
	li	$t5, '*'
	li	$t6, '/'
	#Calls the correct math function
	beq	$s2, $t3, addition   
	beq	$s2, $t4, subtraction 
	beq	$s2, $t5, multiplication 
	beq	$s2, $t6, division  	

#-------------------------
#------Prints function----
#-------------------------	
print:
	#Prints Thank you message
	li 	$v0 4
    	la 	$a0 result
    	syscall 
    	#Prints first int
    	li 	$v0 1
    	move 	$a0 $s0
    	syscall
    	#Prints operator
        li 	$v0 11
    	move 	$a0 $s2
    	syscall
    	#Prints second int
        li 	$v0 1
    	move 	$a0 $s1
    	syscall
    	#Prints space
    	li 	$v0 4
    	la 	$a0 space
    	syscall 
    	jr 	$ra	
    	
exitCode:
	#Puts registers back 
	lw	$a0, 0 ($sp)
	lw	$s0, 4 ($sp)
	lw	$s1, 8 ($sp)
	lw	$ra, 12 ($sp)
	#Exits code
	li 	$v0, 10
	syscall	
	
overflow:
	#Prints overflow message
	li	$v0, 4
	la	$a0 oflow
	syscall
	j 	exitCode
#-------------------------
#------Add function-------
#-------------------------
addition:
	#Adds and checks if signs are the same and branch to either
	#possible overflow or no overflow
	addu  	$t2, $s0, $s1
	xor	$t3, $s0, $s1
	bgez 	$t3, add_overflow
	blez 	$t3, add_no_overflow

	
add_no_overflow:
	#Prints the sum
	jal 	print
	li 	$v0 1
	move $a0, $t2	
	syscall
	j exitCode
	
add_overflow:
	#Check if sum overflowed or not
	xor	$t0, $t2, $s0
	blez	$t0, overflow
	bgez	$t0, add_no_overflow
	
#-------------------------
#------Sub function-------
#-------------------------	
subtraction:
	#Checks if b > a, then possible overflow
	#Or no overflow possible
	subu	$t2, $s0, $s1
	bgt	$s1, $s0, sub_overflow 
	blt	$s1, $s0, sub_no_overflow

sub_no_overflow:
	#Prints the difference
	jal print
	li	$v0, 1
	move 	$a0, $t2
	syscall
	j exitCode
	
sub_overflow:
	#Checks difference sign with sign of a to catch overflow
	xor	$t0, $t2, $s0
	bltz	$t0, overflow
	bgez	$t0, sub_no_overflow
	
#-------------------------
#------Multiply function--
#-------------------------
multiplication:
     	# multiplies ints and stores the lower 32 bits	
	multu $s0, $s1
	mflo $t5
	#Checks if signs are the same 
	xor $t0, $s0, $s1 
	bgez $t0, multi_pos
	#Else, checks for a negative input
	bltz $s0, multi_neg
	bltz $s1, multi_neg

multi_neg:
	#If there is a negative input
	#Overflow if product is positive
	slt $t0, $t5, $zero
	beqz $t0, overflow	
	#Else, print product
	jal print
	li $v0, 1
	move $a0, $t5
	syscall
	j exitCode

	
multi_pos:
	#If signs are the same, check if product is negative
	#If so, overflow, else print product
	slt  $t0, $t5, $zero
	bgtz $t0, overflow  
	jal print
	li $v0, 1
	move $a0, $t5
	syscall
	j exitCode
#-------------------------
#------Divide function----
#-------------------------
division:
	#Base case variables
	li	$t4, 0x80000000
	li 	$v0 1
	#Check divide by 0 case
	beqz	$s1, div_by_zero
	#Check single overflow case
	seq     $t1, $s0, $t4
	seq	$t2, $s1, -1
	and 	$t3, $t1, $t2
	beq     $t3, 1, overflow 
	#Divdes and prints quotient and remainder
	div  	$s0, $s1 
	mflo	$t0
	mfhi	$t1
	jal print
	li $v0, 1
	move $a0, $t0
	syscall
	li $v0, 4
	la $a0, remainder
	syscall
	li $v0, 1
	move $a0, $t1
	syscall
	j exitCode

div_by_zero:
	#Call divide by zero error string
	li $v0, 4
	la $a0, divide0
	syscall
	j exitCode
