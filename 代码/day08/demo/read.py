# author:jason

f = open("../123.jpg","rb") # 读取
w = open("../猫.jpg","wb") # 写入

#读取一个图片
data = f.read()
# 将读取数据写入到另一个文件中
w.write(data)
# 关闭读取和写入资源

f.close()
w.close()

# 如何复制一首诗到另一个文件







