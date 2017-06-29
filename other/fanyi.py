# -*- coding:utf-8 -*-
'''
百度翻译接口测试
@author Veryci
'''
import requests,unittest,json,HTMLTestRunner
class Testbaiduapi(unittest.TestCase):
    def setUp(self):
        url = "http://fanyi.baidu.com/v2transapi"
    def testzhen(self):
        params = {
            "from" : "en",
            "to" : "zh",
            "query" : "study"
        }
        url = "http://fanyi.baidu.com/v2transapi"
        r = requests.request("post",url,params=params)
        r = json.loads(r.text)
        assert u'学习' in r['liju_result']['tag']
    def testzhen1(self):
        params = {
            "from" : "en",
            "to" : "h",
            "query" : "stud"
        }
        url = "http://fanyi.baidu.com/v2transapi"
        r = requests.request("post",url,params=params)
        r = json.loads(r.text)
        assert  u'学习' in r['liju_result']['tag']
    def tearDown(self):
        pass
if __name__ == '__main__':
    #unittest.main(verbosity=2)
    '''生成HTML测试报告'''
    report_dir = r's.html'
    re_open = open(report_dir,'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(Testbaiduapi)
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=re_open,
        title=u'百度翻译api测试接口报告',
        description = u'百度翻译api接口测试详情'
    )
    runner.run(suite)