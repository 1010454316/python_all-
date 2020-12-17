import unittest
from HTMLTestRunner import HTMLTestRunner
suite   =   unittest.TestSuite()




loader  =   unittest.defaultTestLoader

cases   =   loader.discover("F:\\python\\PyCharm 2020.2.1\\pythonProject1\\tesecase",pattern="cha*.py")

suite.addTest(cases)

f   =   open("查询.html","w+",encoding="utf-8")
runner  =   HTMLTestRunner.HTMLTestRunner(
    stream=f
)









