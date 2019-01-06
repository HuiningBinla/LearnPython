# 定义一个列表
num_list = [1,2,3,4]

# 用type就可以查看属性
print(type(num_list))

# 定义一个元组，用 tuple 函数将 num_list 转换为 元组 类型
num_tuple = tuple(num_list)
print(type(num_tuple))

# 定义一个列表，用 list 函数将 num_tuple 转换为 列表 类型
num2_list = list(num_tuple)

print(type(num2_list))


print(num2_list)
print(num_tuple)
print(num_list)
