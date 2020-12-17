import unittest

from doy14.chax import TestInquire
from HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(TestInquire("testQuire"))
suite.addTest(TestInquire("testQuire1"))
suite.addTest(TestInquire("testQuire2"))

f = open("银行查询.html","w+",encoding="utf-8")
htmlrunner = HTMLTestRunner.HTMLTestRunner(
    stream = f, # 将生成的报告写入到f文件里
    title = "银行查询的测试报告", # 报告的标题
    description = "这是银行查询功能的测试", # 报告的描述
    verbosity = 1, # 粗细粒度
)
# 运行器运行测试集
htmlrunner.run(suite)