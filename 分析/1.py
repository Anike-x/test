from collections import defaultdict


with open('D:\\python\\.vscode\\lianxi\\分析\\台词.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
name_mapping = {
    '李相如': '李相如',
    '徐栋鑫': '徐栋鑫',
    '王俞鑫': '王俞鑫',
    '吴佳豪': '吴佳豪',
}
# 创建一个默认字典，用于存储每个人的词数
word_counts = defaultdict(int)

# 打开一个新的txt文件，用于写入每个人的词
with open('D:\\python\\.vscode\\lianxi\\分析\\输出台词_1.txt', 'w', encoding='utf-8') as f_out:
    # 分割姓名和台词，只保留姓名，并将原始的名字替换为新的名字
    for line in lines:
        name, dialogue = line.split(' ', 1)
        name = name_mapping.get(name, 'E')
        words = dialogue.split()
        word_counts[name] += len(words)
        if name == "吴佳豪":
            f_out.write(f'{name}: {" ".join(words)}\n')  # 将每个人的词作为句子写入到新的txt文件中
    f_out.write("\n")
    for line in lines:
        name, dialogue = line.split(' ', 1)
        name = name_mapping.get(name, 'E')
        words = dialogue.split()
        word_counts[name] += len(words)
        if name == "徐栋鑫":
            f_out.write(f'{name}: {" ".join(words)}\n')  # 将每个人的词作为句子写入到新的txt文件中
    f_out.write("\n")
    for line in lines:
        name, dialogue = line.split(' ', 1)
        name = name_mapping.get(name, 'E')
        words = dialogue.split()
        word_counts[name] += len(words)
        if name == "王俞鑫":
            f_out.write(f'{name}: {" ".join(words)}\n')
    f_out.write("\n")
    for line in lines:
        name, dialogue = line.split(' ', 1)
        name = name_mapping.get(name, 'E')
        words = dialogue.split()
        word_counts[name] += len(words)
        if name == "李相如":
            f_out.write(f'{name}: {" ".join(words)}\n')

# 计算每个人的词占比
total = sum(word_counts.values()) / 4
for name, count in word_counts.items():
    percentage = count / total * 100
    print(f'{name}: {percentage:.2f}%')
print('总词数:', total)