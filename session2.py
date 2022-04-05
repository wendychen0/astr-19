#This program will perform arithmetic operations!

#This function prints the sum of two floating point numbers
def sum():
	a = 1.4
	b = 2.5
	print(a, "+", b, "=", a+b)
	print(type(a+b))
	
#This function prints the difference between two integers
def difference():
	a = 4
	b = 2
	print(a, "-", b, "=", a-b)
	print(type(a-b))

#This function prints the product of a floating point number
# and an integer
def product():
	a = 3.2
	b = 2
	print(a, "*", b, "=", a*b)
	print(type(a*b))

#This defines our main() function
#for our program
def main():
	sum()
	difference()
	product()

#When we run the program this 
#executes first
if __name__=="__main__":
	main()