import unittest
from HTMLTestRunner import HTMLTestRunner
from doy14.kaih import TestBank
suite = unittest.TestSuite()
suite.addTest(TestBank("testSaveUser"))
f = open("银行开户.html","w+",encoding="utf-8")
runer = HTMLTestRunner.HTMLTestRunner(
    stream=f,
    title="银行测试",
    verbosity=1,
    description="这是银行测试"
)
runer.run(suite)
