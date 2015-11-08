original_string = "123456 7 890 abc"
change_string= ''
for i in range(len(original_string)):
	change_string+=original_string[i]

print change_string[2::3]