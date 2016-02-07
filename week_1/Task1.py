original_string = "ambulance" #We define the string
reverse_string= ''            #converted string
for i in range(len(original_string)-1, -1, -1):# Create the loop that reverses the string
	reverse_string+=original_string[i]         #transformation original string into reverse string

print reverse_string # we output our changed string into the console