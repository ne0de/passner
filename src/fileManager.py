import os, platform

class PassnerFileManager:
    def __init__(self):
        self.__system = platform.system()
        self.__dirs = { 
            'Windows' : 'C:/Program Files/Passner',
            'Linux' : '/home/User/Passner'
        }
    
    def search(self): return os.path.exists(self.__dirs[self.__system])

    def createDir(self):
        pass
            