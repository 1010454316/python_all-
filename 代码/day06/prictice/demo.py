# 笔试的高频率题目
# 给一个字符串："hello  world"，求每个字符出现次数。
# 写一个冒泡排序，选择排序
string = "this is a dog,that is a monkey!"
# 将字符串转换成列表
li = list(string)

for i in range(0,len(li)):
    count = 0 # 计数器
    # 排重
    flag = True # 开关置位开
    for k in range(0,i):
        if li[k] == li[i]:
            flag = False # 一旦发现相同字符，开关置位关闭
            break

    if flag == False: # 判断开关是否是关闭状态，便于判断是否发现是否统计过
        continue # 终止循环，继续下一轮循环
    # 统计
    for j in range(0,len(li)):
        if li[i] == li[j]:
            count += 1
    print(li[i],"出现了",count,"次！")


































# 选择排序
# a = [6,9,7,1,3,4,8,5,10]
# 冒泡排序
'''
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[j] < a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
    print("第",(i+1),"轮的数据是：" , a)
'''
# 选择排序
'''
for i in range(len(a)):
    for j in range(i + 1,len(a)):
        if a[j] > a[i]:
            a[i],a[j]=a[j],a[i]
'''



