var_string = 'wowhatamanwowowpagh'
i =1
count = 0
podstr = 'wow'
while i != -1:
		i = var_string.find(podstr)
		if i >= 0:
			count +=1
		var_string = var_string[i+1:]
print ("Count = %i \n " % (count))