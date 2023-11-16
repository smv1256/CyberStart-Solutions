#
# Find the valid png file in the /tmp directory using magic bytes.
# The code is hidden in this file.
#

for x in range(2000):
  with open("/tmp/image-%s.png" % str(x), "rb") as file:
    r = bytes(file.read())
    if r.find(b"\x89PNG") > -1: print(r) # just print(r) actually gives the flag but this gets rid of the invalid files :p
