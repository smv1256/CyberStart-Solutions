#
# One of the agents has intercepted a file from the aliens
# The flag is hidden in large amount of non alphanumeric characters.
# The file lives at /tmp/destroymoonbase.gif
#

import re

with open("/tmp/destroymoonbase.gif") as file:
  print(re.sub("\W", "", file.read()))
