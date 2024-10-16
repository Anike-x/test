dic = {"color": "red", "size": "big", "weight": 100, "price": 1000}
print(dic)
for key in dic:
    print(key, dic[key])
for value in dic.values():
    print(value)
# x, y = map(int, input().split())
# print(x, y)
# print(dir())  # 输出当前范围内的变量、方法和定义的类型列表
# print(dir([]))  # 输出列表的所有属性和方法
user = {
    "Tom": {
        "location": "UK",
        "money": "$500"
    },
    "Anime": {
        "location": "US",
        "money": "$900"
    }
}
# item方法返回元组
for username, userInfo in user.items():
    for location, money in userInfo.items():
        print(location, money)
