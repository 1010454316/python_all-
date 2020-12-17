
import random

#银行库
bank = {}  # username : {password,money......}
bank_name = "中国工商银行昌平支行"
bank_choice = {"1":"开户","2":"存钱","3":"取钱","4":"转账","5":"查询","6":"Bye"}  # 银行业务选项

# 开户成功的信息模板
myinfo='''
\033[0;32;40m
------------账户信息------------
账号：{account}
姓名：{username}
密码：{password}
地址：
    国家：{country}
    省份：{province}
    街道：{street}
    门牌号：{door}
账户余额：{money}
注册银行名：{bank_name}
-------------------------------
\033[0m
'''

# 欢迎模板
welcome = '''
***********************************
*      中国工商银行账户管理系统       *
***********************************
*               选项              *
'''

welcome_item = '''*              {0}.{1}             *'''

def print_welcome():
    print(welcome,end="")
    keys = bank_choice.keys()
    for i in keys:
        print(welcome_item.format(i,bank_choice[i]))
    print("**********************************")

# 输入帮助方法：chose是打印选项
def inputHelp(chose,datatype="str"):
    while True:
        print("请输入",chose,":")
        i = input(">>>:")
        if len(i) == 0:
            print("该项不能为空！请重新输入！")
            continue
        if datatype != "str":
            return int(i)
        else:
            return i

# 判断是否存在该银行选项
def  isExists(chose,data):
    if chose in data:
        return True
    return False

# 获取随机码
def  getRandom():
    li = "0123456789qwertyuiopasdfghjklzxcvbnmZXCVBNMASDFGHJKLQWERTYUIOP"
    string = ""
    for i in range(8):
        string =  string + li[int(random.random()* len(li))]
    return string

# 银行的开户方法
def bank_addUser(username,password,country,province,street,door,money):
    # for i in range(100):
    #     bank["张三"  + str(i)] = {}
    if len(bank) >= 100:
        return 3
    elif username in bank:
        return 2
    else:  # 正常开户：存储到银行
        bank[username] = {
            "account":getRandom(),
            "password":password,
            "country":country,
            "province":province,
            "street":street,
            "door":door,
            "money":money,
            "bank_name":bank_name
        }
    return 1

# 开户方法
def  addUser():
    username = inputHelp("用户名")
    password = inputHelp("密码")
    country = inputHelp("居住地址：1.国家：")
    province =  inputHelp("省份")
    street = inputHelp("街道")
    door = inputHelp("门牌号")
    money =  inputHelp("银行卡余额","int")

    # 调用银行的开户方法完成开户操作  返回 1 2 3
    status = bank_addUser(username,password,country,province,street,door,money)
    # 判断1   2   3
    if status == 1:
        user = bank[username]
        print("恭喜开户成功！以下是您的开户信息：")
        print(myinfo.format(account=user["account"],
                            username=username,
                            password=user["password"],
                            country=user["country"],
                            province=user["province"],
                            street=user["street"],
                            door=user["door"],
                            money=user["money"],
                            bank_name=user["bank_name"]
                            ))
    elif status == 2:
        print("该用户已经存在！请携带证件到其他银行办理！谢谢！！！！！")
    elif status == 3:
        print("银行库已满！请携带证件到其他银行办理！谢谢！！！！！")
#
#存钱
# def cunqian():
#     zhanghao=inputHelp('请输入用户名')
#     if not zhanghao in bank:
#         print('该用户不存在')
#     if zhanghao in bank:
#         cunqu = inputHelp('存钱的金额', 'int')
#         if cunqu<=0:
#             print('无效的存款金额！')
#             return -1
#         else:
#             bank[zhanghao]['money']+=cunqu
#         print ('存款成功，卡内的余额为：',bank[zhanghao]['money'])
#
#取钱
#
#
#转账
#
#
#查询
def chaxun():
    username=inputHelp("请输入用户名")
    password=inputHelp("请输入密码")
    if username not in bank:
        print("该用户不存在")
    elif password!=bank[username]["password"]:
        print("密码错误")
    else:
        print("查询信息如下：")
        print(myinfo.format(account=bank[username]["account"],
                            username=username,
                            password=bank[username]["password"],
                            country=bank[username]["country"],
                            province=bank[username]["province"],
                            street=bank[username]["street"],
                            door=bank[username]["door"],
                            money=bank[username]["money"],
                            bank_name=bank[username]["bank_name"]))

# 核心程序
while True:
    print_welcome()
    chose = inputHelp("选项")
    if isExists(chose,bank_choice):
        if chose  == "1":
            addUser()
        elif chose == "2":
            cunqian()
        elif chose == "3":
            pass
        elif chose == "4":
            pass
        elif chose == "5":
            chaxun()
        elif chose == "6":
            print("Bye,Bye您嘞！！！！")
            break
    else:
        print("不存在改选项，别瞎弄！")







