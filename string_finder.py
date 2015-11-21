__author__ = 'rauts3'
import os
path = os.getcwd()

def _filetrav_(path):
    if os.path.isdir(path):
        dir = os.listdir(path)
        for item in dir:
            name = path + '/' + item
            file_path= _filetrav_(name)
            if (file_path)!= None:
               ##print(file_path)
               file_object = open(file_path, 'r')
               file_buffer = file_object.readlines()
               for line in file_buffer:
                  val =  line.find('get_parameter()')
                  if val != -1:
                      print("found", file_path)
    else:
        return path

_filetrav_(path)