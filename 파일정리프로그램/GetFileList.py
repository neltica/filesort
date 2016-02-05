# -*- coding: utf-8 -*-
import os

def getFileList(path):
    return os.listdir(path.decode('utf-8'))



if __name__=="__main__":
    print getFileList("F:/Documents and Settings/사진/새 폴더/새 폴더 (4)")
