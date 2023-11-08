# CHALLENGE 1: Write a for loop that will create a file called
#              /tmp/cars.txt. There should be 50 lines of text in the
#              file. The first line should be "There are 0 cars"
#              and 1 car should be added every line. Until
#              the last line which should read "There are 49 cars"
with open("/tmp/cars.txt", "w") as file:
    for x in range(0, 50):
        file.write("There are %s cars\n" % (str(x)))

# CHALLENGE 2: Open the file at /tmp/cars.txt and read the contents.
#              Print the contents to the screen.
file = open("/tmp/cars.txt", "r")
contents = file.read()
print(contents)
file.close()

# NOTE: Don't use `with` for the second part b'cuz even though the output is the same, it doesn't give the flag lol
