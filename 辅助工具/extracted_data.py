# -*- coding: gb2312 -*-

import re
import json

# ����ʹ�ò�ͬ�ı����ʽ���ļ�
encodings_to_try = ['utf-8', 'gbk', 'big5']  # ��Ҳ��������������ܵı����ʽ

for encoding in encodings_to_try:
    try:
        with open('danmaku_data-2.txt', 'r', encoding=encoding) as file:
            data = file.read()
        break  # ����ɹ����ļ�������ѭ��
    except UnicodeDecodeError:
        continue  # ������ֽ�����󣬳�����һ�������ʽ

# ʹ��������ʽ��ȡĿ������
pattern = re.compile(r'"nickname":"(.*?)"')
target_events = pattern.findall(data)

# ����ȡ�����ݱ��浽��һ���ı��ļ���
with open('extracted_data-2.txt', 'w', encoding='utf-8') as output_file:
    for nickname in target_events:
        output_file.write(f'{{"nickname":"{nickname}"}}\n')

# �������ɹ�����ʾ��Ϣ
print("��ȡ�������ѱ��浽 extracted_data.txt �ļ��С�")
