from input import main
import re
import unittest
import itertools
from random import randint

f = open("C:\Python27\input.py")
lineslist = f.readlines()
left = [] ## danh sach cac gia tri BIEN DUOI cua cac bien
right = []## danh sach cac gia tri BIEN TREN cua cac bien
ListPerLine = []## danh sach cac cap gia tri tuong ung voi cac mien dau vao
listValue = []## danh sach cac gia tri dai dien cho tung lop tuong duong
# sap xep lai cac cap gia tri tuong ung voi cac doan gia tri cua cac bien
def sortList(L1,L2):
    for j in range(len(L1)):
        for i in range((len(L1) - 1), j, -1):
            if (L1[i] < L1[i-1]):
                L1[i], L1[i-1] = L1[i-1], L1[i]
                L2[i], L2[i-1] = L2[i-1], L2[i]
# Kiem tra dieu kien lieu cac doan gia tri co trung len nhau khong
def checkCondition(leftList, rightList):
        for i in range(len(leftList)):
            for j in range(1, len(leftList[i])):
                if(rightList[i][j-1] > leftList[i][j]):
                    return 0
        return 1
# Sinh ngau nhien 1 gia tri giua cac doan gia tri
def randomList(L1,L2):
    listRandom = L1
    for i in range(len(L1)):
        for j in range(len(L1[i])):
            listRandom[i][j]= randint(L1[i][j], L2[i][j])
    return listRandom

for i in range(0,len(lineslist)):
    line = lineslist[i]
    
    if line.startswith("def main") and "'''" in lineslist[i+1]:
        for j in range(i+2,len(lineslist)):
            if "'''" in lineslist[j]:
                break
            List = re.findall(r'\d+',lineslist[j])## lay gia tri xac dinh mien dau vao
            ListPerLine.append(List)
            List = []

for i in range(0,len(ListPerLine)):
    l1 = []
    l2 = []
    for j in range(0,len(ListPerLine[i]),2):
        l1.append(int(ListPerLine[i][j]))
        l2.append(int(ListPerLine[i][j+1]))
    #print l1
    sortList(l1,l2)
    left.append(l1)
    right.append(l2)
print left
print right
listValue = randomList(left, right)
class TestSequense(unittest.TestCase):
    pass
def test_generator(a,b):
    def test(self):
        self.assertEqual(a,b)
    return test
if __name__ == '__main__':
    if (checkCondition(left, right) == 0):
        raise Exception("wrong input")
    else:
        m = 0;
        for i in itertools.product(*listValue):
            test_name = 'test_%d' %m
            m = m+1
            test = test_generator(main(*i),"abc")
            setattr(TestSequense,test_name,test)
        unittest.main()
