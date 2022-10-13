import os

def padZeros(name):
    lst = name.split('-')
    lst[0] = lst[0].zfill(4)
    return '-'.join(lst)

folderLst = os.listdir()
for folder in folderLst:
    os.rename(folder, padZeros(folder))


for folder in folderLst:
    if not folder.split('-')[0].isnumeric(): continue
    for path, subdirs, files in os.walk(folder):
        for name in files:
            if name.endswith('.py'):
                os.rename(os.path.join(path, name), os.path.join(path, padZeros(name)))