#
# Write a script to generate a passphrase by taking words from
# /tmp/words.txt
# The wordNumbers array holds three random numbers. Each number
# corresponds to a word in words.txt. So for example
# wordNumbers[1] is the second word in /tmp/words.txt.
# Put a space between each word and print it out
#

# this is so bad and stupid and inefficient but I'll fix it later b'cuz it works and got the flag lol

with open("/tmp/randomwordsnumbers.txt", "r") as file:
    data = file.read()

wN = data.rstrip().split("\n")
w = []

# b'cuz it's a string not an int for array index
for x in wN:
  w.append(int(x))

with open("/tmp/words.txt", "r") as file:
  data2 = file.read().split("\n")

print(data2[w[0]] + " " + data2[w[1]] + " " + data2[w[2]])
  
