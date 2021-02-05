import os

for folderName, subFolders, fileNames in os.walk('C:\\9. Release'):
    print('The folder is ' + folderName)
    print('The subFolders in ' + folderName + ' are: ' + str(subFolders))
    print('The fileNames in: ' + folderName + ' are: ' + str(fileNames))
    print()

    for subFolder in subFolders:
        if 'fish' in subFolder:
            print('HI')
            ##os.rmdir(subFolder)

    for file in fileNames:
        if file.endswith('.py'):
            print('Hello')
            ##shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup)')