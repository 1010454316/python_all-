f = open("魔法学院成绩.txt","r+",encoding="utf-8")
dic = {}# 姓名:总分

lines = f.readlines()# ["罗恩 23 35 44" , "哈利 60 77 68 88 90"...]

for line in lines:
    li = line.replace("\n","").split(" ") # ["罗恩","23","35","44"]
    name = li[0] # "罗恩"
    scores = li[1:] # ["23","35","44"]
    dic[name] = sum([int(i) for i in scores])# [23 35 44]  lambda   兰不大表达式：效率更高

print(dic)












