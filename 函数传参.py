def delete(my_list: list):
    while 1:
        if len(my_list) != 0:
            my_list.pop()
        else:
            break


x = [1, 5, "545"]
delete(x[:])    # 不修改列表,传递的副本
print(x)
delete(x)
print(x)

