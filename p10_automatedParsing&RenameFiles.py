# AUTOMATE PARSING AND RENAMING OF MULTIPLE FILES
# orginal file : Earth-Sun-#4.mp4
# renamed file : 04-Earth.mp4

import os
print(os.getcwd())
os.chdir('/Users/shriyays/Desktop/cs/LANGUAGES/python/child_dir2')
print(os.getcwd())

#prints list of files
for f in os.listdir():
    print(f)

#prints in tuples of format (name, extension)
for f in os.listdir():
    print(os.path.splitext(f))

#only file names get printed
for f in os.listdir():
    fname,fext = os.path.splitext(f)
    print(fname)

for f in os.listdir():
    fname,fext = os.path.splitext(f)
    print(fname.split('-'))

for f in os.listdir():
    fname,fext = os.path.splitext(f)
    ftitle, fcourse,fnum = fname.split('-')
    #to remove extra spaces at split postions
    ftitle = ftitle.strip()
    fcourse = fcourse.strip()
    #to remove '#' and zero pad 2 strings
    fnum=fnum.strip()[1:].zfill(2)
    newname='{}-{}{}'.format(fnum,ftitle,fext)
    os.rename(f,newname)

    

