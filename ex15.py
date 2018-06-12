from sys import argv

script, filename = argv

# opens a file and then returns a file object
txt = open(filename)

print(f"Here's your file {filename}:")
#reads lines from this file object
print(txt.read())
txt.close()
#prints a string and then requests input from the user and assigns
# the input to file_again
print("Type the filename again:")
file_again = input("> ")

#opens file again and gets txt_again to be this new file
txt_again = open(file_again)
#prints out the contents of the file
print(txt_again.read())
txt_again.close()
