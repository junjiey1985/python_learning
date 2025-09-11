
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# 修改列表元素
motorcycles[0] = 'ducati'
print(motorcycles)

# 在列表末尾添加元素
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# 在列表中插入元素
motorcycles.insert(0, 'ducati')
print(motorcycles)

# 使用 del 语句删除元素
del motorcycles[0]
print(motorcycles)

# 使用 pop() 方法删除元素
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# 删除列表中任意位置的元素
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")


# 如果不确定该使用 del 语句还是 pop() 方法，下面是一个简单的判
# 断标准：如果要从列表中删除一个元素，且不再以任何方式使用它，
# 就使用 del 语句；如果要在删除元素后继续使用它，就使用 pop()
# 方法。


# 根据值删除元素
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)