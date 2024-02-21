#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


# 获取单个文件的行数
def count_lines_in_file(file_path):
    with open(file_path, 'rb') as file:
        count = 0
        for line in file:
            count += 1
        return count


# 获取文件夹中所有文件的总行数
def count_lines_in_directory(directory):
    total_lines = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):  # 确保是文件而不是文件夹
                total_lines += count_lines_in_file(file_path)
    return total_lines


directory_path = '/home/dd/Desktop/Repositories/LearningPythonFollowingTurtle'  # 文件夹路径
total_line_count = count_lines_in_directory(directory_path)
print(f"文件夹 '{directory_path}' 中所有文件的总行数为: {total_line_count}")
