# -*- coding:utf-8 -*-
'''
 @Time : 2017/06/28
 @Author : Veryci
 @Site :
 @File : Get_excel.py
 @Software : Pycharm
'''
import xlrd,xlwt
import unittest,sys
from xlutils.copy import copy
from Interface.TestRequest import reques
def datacel():
    filepath = 'D:\\software\\Python\\workspace\\InterfaceTest\\Data\\data.xlsx'
    file = xlrd.open_workbook(filepath)
    me = file.sheets()[0]
    nrows = me.nrows
    listid = []
    listkey = []
    listconeent = []
    listurl = []
    listfangshi = []
    listqiwang = []
    listresult = []
    listname = []
    for i in range(1,nrows):
        listid.append(me.cell(i,0).value)
        listkey.append(me.cell(i,2).value)
        listconeent.append(me.cell(i,3).value)
        listurl.append(me.cell(i,4).value)
        listname.append(me.cell(i,1).value)
        listfangshi.append(me.cell(i,5).value)
        listqiwang.append(me.cell(i,6).value)
    return listid,listkey,listconeent,listurl,listfangshi,listqiwang,listname