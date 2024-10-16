import json

with open("test.txt", "r") as f:
    for _ in f:
        print(_, end="")

print()

with open("test.txt", "r") as f:
    x = f.readlines()
    for i in x:
        print(i.rsplit())

with open("test.txt", "a+") as f:
    json.dump({"name": "张三", "age": 18}, f)

try:
    with open("test.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("文件不存在")
else:
    print("文件存在")
