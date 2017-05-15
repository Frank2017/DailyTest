# coding=UTF-8

import sys
import os
import shutil


def isEmptyDir(fpath):
    cnt = 0
    if os.path.exists(fpath):
        childList = os.listdir(fpath)
        for cl in childList:
            clpath = os.path.join(fpath, cl)
            if os.path.isdir(clpath):
                if not os.listdir(clpath):
                    cnt += 1
                    print(str(cl) + ' is Empty ------->')
                else:
                    cnt += 1
                    print(str(cl) + ' is not Empty!!!')
    else:
        print('fpath is not exists!')
    return cnt
    pass

def readFile(fpath, moveTo):
    if os.path.exists(fpath):
        childList = os.listdir(fpath)
        for cl in childList:
            clpath = os.path.join(fpath, cl)
            if os.path.isdir(clpath):
                readFile(clpath, moveTo)
            elif os.path.isfile(clpath):
                moveToFile = os.path.join(moveTo, cl)
                shutil.move(clpath, moveToFile)
    else:
        print('fpath is not exists!')
    pass


if __name__ == '__main__':
    OriginalPath = r'F:\论文集\论文集.Data\PDF'
    MoveToPath = r'C:\Users\磊\Desktop\EndNotePaper'
    if not os.path.exists(MoveToPath):
        os.mkdir(MoveToPath)
    # readFile(OriginalPath, MoveToPath)
    print(isEmptyDir(OriginalPath))
    pass
