var_string = 'wowhatamanwowowpagh' #We define the string
i =1            #Define the variable that will store the number of found substrings
count = 0       #The variable that counts the number of occurrences
podstr = 'wow'  #Determine the substring that will be sought in the sting
while i != -1:  #Until we get to the end
		i = var_string.find(podstr)  #We search substring 'wow' in a string and write it in a variable i
		if i >= 0:    #Create a condition if found substrings will be >=0
			count +=1 #We count the number of occurrences
		var_string = var_string[i+1:] #Counting the number of occurrences if the last letter of the word is the first letter of another word
print ("Count = %i \n " % (count))    #Print number of occurrences into the console