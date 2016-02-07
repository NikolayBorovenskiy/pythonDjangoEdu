def double_turple(value): #Create a function with argument "value"

	
	return tuple([(value[i:i+2]) for i in range(0, len(value), 2)]) #Returns a turple of turples by outputting every two elements using a loop



print double_turple((1, 4, 8, 6, 3, 7, 1))  #We print the result of the function with given values