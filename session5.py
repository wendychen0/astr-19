import numpy as np
from astropy.table import Table

def main():
	x = np.linspace(0, 2*np.pi, 1000)
	sinx = np.sin(x)

	table = Table([x, sinx], names=['x','sin(x)'])
	print(table)

#When we run the program this 
#executes first
if __name__=="__main__":
	main()