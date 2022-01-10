from PIL import Image                                              
import os, sys                       

path = ""
dirs = os.listdir( path )                                       

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((300,300), Image.ANTIALIAS)
            imResize.save(f+'.jpg', 'jpeg', quality=80)
            #os.remove(path+item) 

resize()