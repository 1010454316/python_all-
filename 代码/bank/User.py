import datetime
from bank.tools import tools
class User:
    '''
    账号（int）、姓名(Str)、密码(6位数字)、地址、存款余额(double)
    、注册时间(date)、开户行（银行的名称（String））
    '''
    __account = None # 系统自动产生，不需要提供set方法，可以提供get方法
    __username = None
    __password = None
    __address = None
    __money = None
    __reg_date = None # 不需要提供set方法，可以提供get方法
    __bankname = None # 不需要提供set方法，提供get方法，应该去银行那边取数据

    def __init__(self,username,password,address,money):
        self.__username = username
        self.__password = password
        self.__address = address
        self.__money = money
        self.__account = tools().getRandom() # 获取随机码
        self.__bankname = "中国工商银行昌平支行"
        self.__reg_date = datetime()

    def getAccount(self):
        return self.__account
    def setUsername(self,username):
        self.__username = username