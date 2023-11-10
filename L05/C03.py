#
# Sample Alien Zip file found at /tmp/alien-zip-2092.zip is password protected
# We have worked out they are using three digit code
# Brute force the Zip file to extract to /tmp
#
# Note: The script can timeout if this occurs try narrowing
# down your search

"""zipfile mod to help with .zip and itertools used as nested for-loop"""
import zipfile, itertools

for x in itertools.product("0123456789", repeat = 3):
  password = "".join(x)
  try:
    with zipfile.ZipFile("/tmp/alien-zip-2092.zip", "r") as file:
      file.extractall(path = "/tmp", pwd = bytes(password, "utf-8"))
      print(password + " SUCCESS")
      break
  except:
    print(password + " failed")
    
