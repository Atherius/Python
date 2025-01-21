#importing the required modules.
import os
import shutil

#create a path to source file.
#create a path to small, medium and large directories.
src= r'E:\\Python\\Bizmetric python\\'
sdir= os.path.join(src, 'smoll')
mdir = os.path.join(src, 'mid')
ldir = os.path.join(src, 'lorge')

# Now check whether the directories exist or not. 
# if they do not exist we create them.
os.makedirs(sdir, exist_ok=True)
os.makedirs(mdir, exist_ok=True)
os.makedirs(ldir, exist_ok=True)

#iterating through each individual file in the source directory.
#checking the size of the file and moving it to the respective directory.
#using try and except block to handle the exceptions.
for i in os.listdir(src):
    fnm = os.path.join(src, i)
    
    try:
        if os.path.isfile(fnm):
            sz = os.stat(fnm).st_size / 1000  

            if 0 <= sz <= 200:
                shutil.move(fnm, sdir)
            elif 200 < sz <= 400:
                shutil.move(fnm, mdir)
            else:
                shutil.move(fnm, ldir)
    except FileNotFoundError:
        print(f"File not found: {fnm}")
    except PermissionError:
        print(f"Permission denied: {fnm}")
    except Exception as e:
        print(f"Error processing file {fnm}: {e}")