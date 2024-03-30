# -*- coding: gb2312 -*-

import re
import json

# 尝试使用不同的编码格式打开文件
encodings_to_try = ['utf-8', 'gbk', 'big5']  # 你也可以添加其他可能的编码格式

for encoding in encodings_to_try:
    try:
        with open('danmaku_data-2.txt', 'r', encoding=encoding) as file:
            data = file.read()
        break  # 如果成功打开文件，跳出循环
    except UnicodeDecodeError:
        continue  # 如果出现解码错误，尝试下一个编码格式

# 使用正则表达式提取目标数据
pattern = re.compile(r'"nickname":"(.*?)"')
target_events = pattern.findall(data)

# 将提取的数据保存到另一个文本文件中
with open('extracted_data-2.txt', 'w', encoding='utf-8') as output_file:
    for nickname in target_events:
        output_file.write(f'{{"nickname":"{nickname}"}}\n')

# 输出保存成功的提示信息
print("提取的数据已保存到 extracted_data.txt 文件中。")
