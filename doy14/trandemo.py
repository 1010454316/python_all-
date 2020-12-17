import unittest
from doy14.debit import TestBank1
from HTMLTestRunner import HTMLTestRunner

#创建测试集
suite = unittest.TestSuite()
suite.addTest(TestBank1("testBank_transformMoney"))

f = open("银行转账.html","w+",encoding="utf-8")
htmlrunner = HTMLTestRunner.HTMLTestRunner(
    stream=f,  # 将生成的报告写入到f文件里
    title="银行转账的测试报告",  # 报告的标题
    description="这是一个银行转账的测试",  # 报告的描述
    verbosity=1,
)
htmlrunner.run(suite)
