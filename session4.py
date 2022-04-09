class Animal(object):

	#Initialization function
	def __init__(self, arm_length, leg_length, eyes, tail, furry):
		self.arm_length = arm_length
		self.leg_length = leg_length
		self.eyes = eyes
		self.tail = tail
		self.furry = furry

	#Function to print out and describe the data members
	def describe(self):
		print("Length of the arms: ", self.arm_length)
		print("Length of the legs: ", self.leg_length)
		print("Number of eyes: ", self.eyes)
		print("Does it have a tail?", self.tail)
		print("Is it furry?", self.tail)

#This defines our main() function
#for our program
def main():
	a = Animal(6.5, 8.2, 2, True, True)
	#a = Animal()
	a.describe()
	

#When we run the program this 
#executes first
if __name__=="__main__":
	main()