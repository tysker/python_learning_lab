# Read file and close file
# file = open("file.txt")
# contents = file.read()
# print(contents)
# file.close()

# Read file and close file is implicit
def read_from_file():
    with open("file.txt") as file:
        contents = file.read()
        print(contents)


# Write to file
# mode a = append
# mode w = write
def write_to_file():
    with open("file.txt", mode="a") as file:
        file.write("My name is Steve/n")


write_to_file()
read_from_file()
