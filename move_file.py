import os
import shutil

from_dir='C:/Users/user/Downloads'
to_dir='C:/Users/user/Documents/Document_files'

list_of_files=os.listdir(from_dir)
#print(list_of_files)

for files in list_of_files:
    name,extension=os.path.splitext(files)
    print(name)
    print(extension)

    if extension=="":
        continue
    if extension in[ '.txt',' .doc',' .docx','.pdf']:
        path1=from_dir+"/"+files
        path2=to_dir+'/'+'Document_files'
        path3=to_dir+'/'+"Document_files"+'/'+files

        if os.path.exists(path2):
            print('Moving files',files,'....')
            shutil.move(path1,path3)
        else :
            os.makedirs(path2)
            print('Moving files',files,'....')
            shutil.move(path1,path3)
