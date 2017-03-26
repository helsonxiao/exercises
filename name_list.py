names = []
for append_name in range(5):
    append_name = input("请输入待添加的姓名：")
    names.append(append_name)
names.sort()
print("The names are", end=" ")
for i in names:
    print(i, end=" ")
print()
print("The third name is "+ str(names[2]))
name_index = int(input("想替换第几个名字？"))
del names[name_index - 1]
name_append = input("输入替换的名字：")
names.insert(name_index - 1,name_append)
print("The names are", end=" ")
for i in names:
    print(i, end=" ")