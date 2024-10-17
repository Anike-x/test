from collections import defaultdict

# 原始的名字和新的名字的映射
name_mapping = {
    '李相如': '李相如',
    '徐栋鑫': '徐栋鑫',
    '王俞鑫': '王俞鑫',
    '吴佳豪': '吴佳豪',
}

# 读取文件内容
with open('D:\\python\\.vscode\\lianxi\\分析\\台词.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 创建一个默认字典，用于存储每个人的词数
word_counts = defaultdict(int)

# 分割姓名和台词，只保留姓名，并将原始的名字替换为新的名字
for line in lines:
    name, dialogue = line.split(' ', 1)
    name = name_mapping.get(name, 'E')
    words = dialogue.split()
    word_counts[name] += len(words)
    print(f'{name}的词: {words}')  # 打印每个人的词

# 计算每个人的词占比
total = sum(word_counts.values())
for name, count in word_counts.items():
    percentage = count / total * 100
    print(f'{name}: {percentage:.2f}%')
print('总词数:', total)