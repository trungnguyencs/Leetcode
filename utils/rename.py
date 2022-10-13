import os

folderLst = os.listdir()
for folder in folderLst:
	lst = folder.split('-')
	lst[0] = lst[0].zfill(4)
	newName = '-'.join(lst)
	os.rename(folder, newName)