'''
num1 = int(input("请输入第一个数："))  # -->  "34"  -->  34
num2 = int(input("请输入第二个数："))
num3 = int(input("请输入第三个数："))
num4 = int(input("请输入第四个数："))
num5 = int(input("请输入第五个数："))
num6 = int(input("请输入第六个数："))
num7 = int(input("请输入第七个数："))
num8 = int(input("请输入第八个数："))
num9 = int(input("请输入第九个数："))
num10 = int(input("请输入第十个数："))

print("总和为：" ,(num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10))
'''

'''
姓名，身份证号，年龄，性别，身高，体重

'''
name = input("请输入姓名：")
id = input("请输入身份证号：")
age = int(input("请输入年龄："))
sex = input("请输入性别：")
high = int(input("请输入身高："))
weight = int(input("请输入体重："))
#print("我叫",name,"，我的身份证号",id,"，我今年",age,"岁了,","我是",sex,"生,我的身高",high,"厘米，我的体重",weight,"公斤！")
# 个人信息显示模板
info = '''
-------------[ 中国工商银行  |   个人信息系统]-------------
姓名：{name}
年龄：{age}
身份证：{id}
身高：{high}
体重：{weight}
性别：{sex}
-------------------------------------------------------
'''
print(info.format(
    name=name,
    age=age,
    id=id,
    high=high,
    sex=sex,
    weight=weight
))





