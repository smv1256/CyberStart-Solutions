#
# Find the file in the alien directories in /tmp/aliendir to get the flag
#

import os

# print(os.listdir("/tmp/aliendir"))

for x in range(200):
	print(os.listdir("/tmp/aliendir/folder-%s" % str(x)))
