__author__ = 'rauts3'
import os
path = "C:/Users/rauts3/Desktop/St. Thomas"

def _filetrav_(path):
    if os.path.isdir(path):
        dir = os.listdir(path)
        for item in dir:
            name = path + '/' + item
            file_path= _filetrav_(name)
            if (file_path)!= None:
               print(file_path)
    else:
        return path






