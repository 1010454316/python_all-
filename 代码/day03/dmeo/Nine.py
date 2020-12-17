'''
1x1=1
1x2=2   2x2=4
1x3=3   2x3=6   3x3=9
1x4=4   2x4=8   3x4=12  4x4=16
....
1x9=9   2x9=18  3x9=27  4x9=36  5x9=45  ........ 9x9=81
'''
num = int(input("请输入您要的层数："))
i = 1
while i <= num:
    print("第",i,"层",end="")
    j = 1
    while j <= i:
        print(j,"x",i,"=",(j*i),"\t",end="") # end="" 不换行
        j = j + 1
    print() # 换行
    i = i + 1
















