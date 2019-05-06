# A demonstration of some simple MIPS instructions
# used to test QtSPIM

	# Declare main as a global function
	.globl main 

	# All program code is placed after the
	# .text assembler directive
	.text 		

# The label 'main' represents the starting point
main:		# Load the word stored in value (see bottom)
	add $t4, $t2, $t3
    addi $t4, $t2, $t6