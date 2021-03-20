import os, sys, platform

class PassnerFileManager:
    def __init__(self):
        self.__system = platform.system()
        self.__dirs = { 'Windows' : 'C:/Program Files/Passner', 'Linux' : '/home/User/Passner' }
        self.__cdir = self.__dirs[self.__system]
    
    def existDir(self): return os.path.exists(self.__cdir)

    def createDir(self):
        try:
            os.mkdir(self.__cdir)
            return True
        except OSError as exc:
            return False, exc.strerror