1.Case文件夹用来存放我们的测试用例相关的，
2.Data用来存储我们的测试数据，Excel管理测试用例，yaml文件管理测试用例，后续要把yaml管理测试用例的也封装出来。
3.Interface对测试接口相关的封装，包括requests库，发送测试报告的email的封装，从Excel取测试数据的封装
4.Public 展示测试报告相关的脚本，这里可以自己封装，也可以使用现成的，我这里是基于我自己封装的，最后生成的测试报告更加易懂，出错可以尽快排查相关原因
5.report 存放测试报告，
6.main.py 主运行文件。