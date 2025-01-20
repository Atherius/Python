import os
import shutil

for i in os.listdir(r'E:\\Python\\Bizmetric python\\'):
    fnm=r'E:\\Python\\Bizmetric python\\'+i
    #sz=(os.stat('E:\\Python\\Bizmetric python\\'+i).st_size)/1024
    sz=os.stat(fnm).st_size/1000

    if 0<=sz<=200:
        shutil.move(fnm,'E:\\Python\\Bizmetric python\\smoll')
    elif 200<=sz<=400:
        shutil.move(fnm,'E:\\Python\\Bizmetric python\\mid')
    else:
        shutil.move(fnm,'E:\\Python\\Bizmetric python\\lorge')