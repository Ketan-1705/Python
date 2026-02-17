#Write a Python program to open a file in write mode, write some text, and then close.

file=open("File.txt","w")
file.write("This is Python program to open a file in write mode ")
file.close()
print("File written successfully")
