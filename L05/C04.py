#
# Write a script to generate a passphrase by taking words from
# /tmp/words.txt
# The wordNumbers array holds three random numbers. Each number
# corresponds to a word in words.txt. So for example
# wordNumbers[1] is the second word in /tmp/words.txt.
# Put a space between each word and print it out
#

# yay I made it a bit better now
# lemme just wait for ski to yell at me now btw

with open("/tmp/randomwordsnumbers.txt", "r") as file:
    data = file.read()

wordNumbers = data.rstrip().split("\n")
w = [ int(x) for x in wordNumbers ] # convert wordNumbers arr from str to int

with open("/tmp/words.txt", "r") as file:
  data2 = file.read().split("\n")
  
for x in range(3):
  print(data2[w[x]], end = " ") # replace default print \n with space
    
