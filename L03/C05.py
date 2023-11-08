# CHALLENGE 1: Write a regex search that extracts all the classes from
#             the divs and saves them into an array.
reg = re.findall("'(.*)'", html)

# CHALLENGE 2: Write a loop that goes through the array from
#              CHALLENGE 1 and prints the contents.
for x in reg:
  print(x)
