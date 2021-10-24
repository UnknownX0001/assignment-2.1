
def triangle(abc):

	space = abc - 1

	for i in range(0, abc):

		for x in range(0, space):
			print(end=" ")

		space = space - 1
	
		for x in range(0, i+1):
		
		
			print("* ", end="")
	
		print("\r")

abc = 25
triangle(abc)
