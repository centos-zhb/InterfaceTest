# -*- coding:utf-8 -*-
from Interface.TestRequest import reques
reques=reques()
class TestApi(object):
    def __init__(self,url,key,connent,fangshi):
        self.url = url
        self.key = key
        self.connent = connent
        self.fangshi = fangshi
    def testapi(self):
        if self.fangshi=='POST':
            self.parem = {
                'key' : self.key,
                'info' : self.connent
            }
            r = reques.post(self.url,self.parem)
        elif self.fangshi=='GET':
            self.parem = {
                'key' : self.key,
                'info' : self.parem
            }
            r = reques.post(self.url,self.parem)
        return r
    def getcode(self):
        code = self.testapi()['code']
        return code
    def getJson(self):
        json_data = self.testapi()
        return json_data