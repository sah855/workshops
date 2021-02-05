import os
totalSize = 0
for filename in os.listdir('c:\\1. General'):
	if not os.path.isfile(os.path.join('c:\\1. General', filename)):
		continue
	totalSize = totalSize + os.path.getsize(os.path.join('c:\\1. General', filename))
print(totalSize)
print('Size of file : ' + str(totalSize/1024/1024) + 'MB')