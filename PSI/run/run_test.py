import unittest
import time
#导入该类之前需要先配置环境
import HTMLTestRunner
def  testAll():
    #实现指定测试脚本文件夹进行执行所有的测试脚本
    dis=unittest.defaultTestLoader.discover(start_dir='E:\longer\\test\PSI\suite',
                                            pattern='*_TestSuite.py',top_level_dir=None)
    print(dis)
    #runner=unittest.TextTestRunner()
    #获取系统时间
    timapath=time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
    path=open('E:\longer\\test\PSI\\report\PsiTestReport%s.html'%timapath,'wb')
    #第一个参数stream表示的是报告生成的路径
    #title表示的是报告的标题
    #description表示的是报告的描述
    runner=HTMLTestRunner.HTMLTestRunner(stream=path,title='所有测试脚本文件报告',description='以下是报告详情',verbosity=2)
    runner.run(dis)

testAll()

