my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# 如果只是将 my_foods 赋给 friend_foods，就不能得到两个列表
# 例如，下面演示了在不使用切片的情况下复制列表的情况：
my_foods = ['pizza', 'falafel', 'carrot cake']
# 这是行不通的：
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)