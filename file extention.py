filename = input("Enter the file name: ")
fileextension = filename.split(".")
print(fileextension)
print ("The extension of the file " + filename + " is: ." + (fileextension[-1]))
