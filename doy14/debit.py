import unittest
from doy14.bank import bank_takeMoney
from doy14.bank import findByAccount
from doy14.bank import bank_saveMoney



class TestBank1(unittest.TestCase):
    def testBank_transformMoney(self):
        outputaccount=165146145
        inputaccount=9842894892
        outputpassword="1652454526"
        outputmoney="4524654425"



        status = bank_takeMoney(outputaccount, outputpassword, outputmoney)
        if status == 1:
            return status
        elif status == 2:
            return status
        elif status == 3:
            return status

        if inputaccount != None and findByAccount(inputaccount) != None:
            bank_saveMoney(inputaccount, outputmoney)
            return 0
        else:
            return 1


