from statistics import variance
from typing import Counter, List
import math

def zcount(list: List[float]) -> float:
    
    l = len(list)
    return l


def zmean(list: List[float]) -> float:
    
    return sum(list) / zcount(list)


def zmode(list: List[float]) -> float:

    return max(set(list), key = list.count)


def zmedian(list: List[float]) -> float:

    sortedLst = sorted(list)
    lstlen = len(list)
    index = (lstlen -1) // 2

    if (lstlen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index]+sortedLst[index +1] )/ 2.0
    
def zvariance(list: List[float]) -> float:

    n =zcount(list) - 1
    mean = zmean(list)
    deviations = [abs(mean -xi) ** 2 for xi in list]
    variance = sum(deviations) / n
    return variance

    
def zstddev(list: List[float]) -> float:

    std_dev = math.sqrt(zvariance(list))
    return std_dev


def zstderr(list: List[float]) -> float:

    std_err = zstddev(list)/(math.sqrt(zcount(list)))
    return std_err


def zcov(a,b):
    sum = 0
    if zcount(a) == zcount(b):
        for i in range(0, zcount(a)):
            sum += ((a[i]-zmean(a))* (b[i] - zmean(b)))
        cov = sum / (zcount(a)-1)
    return cov


def zcorr(listx: List[float], listy: List[float]) -> float:
    
    corr = zcov(listx,listy) / (zstddev(listx) * zstddev(listy))
    return corr

def readDataSets(files):
#    print("in readDataSets...", files)
    data = {}
    for file in files:
        twoLists = readDataFile(file)
        data[file] = twoLists
    return data
def readDataFile(file):
    x,y = [], []
    with open(file) as f:
        first_line = f.readline() # consume headers
        for l in f:
            row = l.split(',')
            #print(row, type(row))
            x.append(float(row[0]))
            y.append(float(row[1]))
    return (x,y)
