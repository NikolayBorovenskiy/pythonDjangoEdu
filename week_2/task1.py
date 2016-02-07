def func(var_a, var_b):   #Create a function with arguments
	
	if type(var_a) == str or type(var_b) == str:   #Condition:if at least one of the variables is a string we type "str"
		print "type(func(5, '2') ='str'"
	
	elif type(var_a) == int or type(var_b) == int: #Condition: if the variablea are integers we print "int"
		print "'int'"
	
	elif var_a > var_b:  #Condition: if var_a more then var_b we print ">"  
		print ">"

	elif var_a == var_b: #Condition: if var_a is equal var_b we print "=" 
		print "="

	elif var_a < var_b: #Condition: if var_a less then var_b we print "<" 
		print "<"



print func(5, '2') #We print the result of the function with given values