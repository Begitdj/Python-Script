import os
print("Folder Creator")
test = input("Enter path to create folder Example:/folder/Folder1 this example create in folder with name folder folder with name Folder1:")
if not os.path.exists(test):
	os.mkdir(test)
