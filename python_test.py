import sys
 
print("printing input parameter value :", sys.argv[1])

#open text file
text_file = open("in_plan.yaml", "w")
#write string to file
n = text_file.write(sys.argv[2])
#close file
text_file.close()
 
print(n)