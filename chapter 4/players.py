# 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# 提取列表的第二、第三和第四个元素，可将起始索引指定为 1，并将终止索引指定为 4.
print(players[1:4])

# 如果没有指定第一个索引，Python 将自动从列表开头开始：
print(players[:4])

# 要让切片终止于列表末尾，也可使用类似的语法
print(players[2:])

# 负数索引返回与列表末尾有相应距离的元素，因此可以输出列表末尾的任意切片。如果要输出名单上最后三名队员的名字，可使用切片 players[-3:]：
print(players[-3:])