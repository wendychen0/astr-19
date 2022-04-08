def calc(x):
	return(x**3 + 8)

#This defines our main() function
#for our program
def main():
	x = 9
	y = calc(x)
	print(y)
	if (int(y) > 27):
		print("YAY!")

#When we run the program this 
#executes first
if __name__=="__main__":
	main()