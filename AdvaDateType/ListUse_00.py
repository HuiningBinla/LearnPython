name_list = ["zhangsan", "lisi", "wangwu"]

# 1. 取值和去索引
# list index out of range   -- 列表索引超出范围 
# print(name_list[3])
print(name_list[2])

# 知道数据的内容，想确定数据在列表中的内容
# 使用 index 方法需要注意，如果传递的数据不在列表中，程序会报错！
print(name_list.index("lisi"))


# 2. 修改
name_list[1] = "李四"
# list assignment index out of range
# 列表指定的索引超出范围，程序会报错！
# name_list[3] = "王小二"

# 3. 增加
# append 方法可以在列表的末尾追加数据
name_list.append("王小二")
# insert 方法可以在列表索引指定的位置插入数据
name_list.insert(1,"小美眉")

# extend 方法可以把其他列表中的完整内容，追加到当前列表的末尾！
temp_list = ["孙悟空","猪二哥","沙师弟"]
name_list.extend(temp_list)

# 4. 删除

print(name_list)