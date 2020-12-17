import random
class tools:
    # 获取随机码
    def  getRandom(self):
        li = "0123456789qwertyuiopasdfghjklzxcvbnmZXCVBNMASDFGHJKLQWERTYUIOP"
        string = ""
        for i in range(8):
            string =  string + li[int(random.random()* len(li))]
        return string

    # 输入帮助方法：chose是打印选项
    def inputHelp(self,chose,datatype="str"):
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