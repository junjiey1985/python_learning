# 使用 sort() 方法对列表进行永久排序
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)


# 使用 sorted() 函数对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# 反向打印列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# 确定列表的长度
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

# 使用列表时避免索引错误
