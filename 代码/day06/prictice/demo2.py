# author:jason

string = "this is a dog,that is a monkey!"
# 身份运算符 in    not in
# print("is" in string[:12]) # 判断is 是否在前面12个字符串里出现过

for index,ch in enumerate(string): # 枚举每一个字符出现的角标  +  字符
    if ch in string[:index]:   # 通过切片来判断是否之前是否出现过
        continue
    print(ch,"出现了",string.count(ch))   # 通过count()方法来统计全文出现次数
















