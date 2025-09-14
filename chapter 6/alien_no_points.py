alien_0 = {'color': 'green', 'speed': 'slow'}
#使用放在方括号内的键从字典中获取感兴趣的值，可能会引发问题：如果指定的键不存在，就将出错。
#print(alien_0['points']) 

# 就字典而言，为避免出现这样的错误，可使用 get() 方法在指定的键不存在时返回一个默认值。
# get() 方法的第一个参数用于指定键，是必不可少的；第二个参数为当指定的键不存在时要返回的值，是可选的：
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# 注意：在调用 get() 时，如果没有指定第二个参数且指定的键不存
# 在，Python 将返回值 None，这个特殊的值表示没有相应的值。这并
# 非错误，None 只是一个表示所需值不存在的特殊值。