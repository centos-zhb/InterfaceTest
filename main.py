# -*- coding:utf-8 -*-
import os,time,unittest,datetime
from Case.TestCase import Testinface
from Public.py_Html import createHtml
'''
这里你可以分开执行上面你case里面包含的用例。也可以单独执行里面的某一个的测试用例。
'''
from Public import BSTestRunner
from Interface.Email import sendmail
if __name__ == '__main__':
    starttime = datetime.datetime.now()
    suite = unittest.TestSuite()
    suite.addTest(Testinface("testinterface"))
    me = Testinface()
    list_fail,list_pass,list_json,listurls,list_keys,listconeents,listfangshis, listqiwangs, listids, listrelust, listnames=me.testinterface()
    filepath = r'D:\\software\\Python\\workspace\\InterfaceTest\\report\\pyresult.html'
    if os.path.exists(filepath) is False:
        os.system(r'touch %s' % filepath)
    endtime = datetime.datetime.now()
    createHtml(titles='接口测试报告',filepath=filepath,starttime=starttime,endtime=endtime,passge=list_pass,fail=list_fail,id=listids,name=listnames,key=list_keys,coneent=listconeents,url=listurls,meth=listfangshis,yuqi=listqiwangs,json=list_json,relusts=listrelust)
    sendmail(filepath)