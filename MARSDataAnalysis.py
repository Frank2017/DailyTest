# _*_ coding: utf-8 _*_
import os
import time


def WriteFile(curPath, data):
    note_path = os.path.join(curPath,"details.txt")
    totalNum = 0
    fp = open(note_path,'w')
    if data != None:
        fp.write("There is " + data.__len__().__str__() + " cameras.\n")
        for k in sorted(data.keys()):
            fp.write('\n\n' + str(k) + ":\n")
            for kk in sorted(data[k].keys()):
                fp.write("tracklet: " + str(k) + '-' + str(kk) + " has " + data[k][kk].__str__() + ' pictures\n')
                totalNum += data[k][kk]
        pass
    fp.write("\n\n Total:" + totalNum.__str__())
    fp.close()
    pass


def SplitName(str):
    # fileName, fileExt = os.path.splitext(str)
    result = []
    result.append(str[0:4])
    result.append(str[4:6])
    result.append(str[6:11])
    result.append(str[11:15])
    return result
    pass


def AnalyzeDir(path, backupPath):
    childList = os.listdir(path)
    dict = {}
    for c in childList:
        if os.path.isfile(os.path.join(path, c)):
            temp = SplitName(c)
            if dict.has_key(temp[1]):
                tempCam = dict[temp[1]]
                if tempCam.has_key(temp[2]):
                    tempCam[temp[2]] += 1
                else:
                    tempCam[temp[2]] = 1
            else:
                dict[temp[1]] = {}
                dict[temp[1]][temp[2]] = 1
                pass
            pass  # if os.path.isfile(os.path.join(path, c)):
        pass  # for c in childlist:
    WriteFile(backupPath, dict)
    pass


def ReadFile(path, backupPath):
    childList = os.listdir(path)
    for c in childList:
        cpath = os.path.join(path, c)
        cpathBackup = os.path.join(backupPath, c)
        # 找到图片文件夹，开始统计各种信息，最后返回
        if os.path.isfile(cpath):
            AnalyzeDir(path, backupPath)
            return
        # 如果没有找到图片文件夹继续递归进入下一层
        if os.path.isdir(cpath):
            if not os.path.exists(cpathBackup):
                os.mkdir(cpathBackup)
            ReadFile(cpath, cpathBackup)
            pass  # if os.path.isdir(c):
        pass  # for c in childlist:
    # 本层的递归全部结束，返回上一层
    return
    pass  # def readFile(path)


if __name__ == '__main__':
    DIR = r'/home/frank/Desktop/MARS'
    BACKUP = r'/home/frank/Desktop/MARSDetails'
    # writeFile(DIR)
    # print os.path.abspath(os.path.join(DIR,os.path.pardir))
    st = time.time()
    ReadFile(DIR, BACKUP)
    en = time.time()
    print 'use time ' + (en-st).__str__()
    # print SplitName('0000C1T0001F001.jpg')
    # dist = {}
    # if dist != None:
    #     dist['name'] = {}
    #     dist['name']['bob'] = 'female'
    #     dist['name']['alice'] = 'male'
    #     dist['country'] = {}
    #     dist['country']['china'] = 1
    #     dist['country']['america'] = 2
    #     dist['country']['france'] = 3
    #     # for k in dist:
    #     #     for kk in dist[k]:
    #     #         print k,kk,dist[k][kk]
    #     WriteFile(r'/home/frank/Desktop',dist)
    pass