# -*- coding: utf-8 -*-
"""
@Time : 2020/5/21 16:49
@Author : Dufy
@Email : 813540660@qq.com
@File : ner_corpus.py
@Software: PyCharm 
Description :
1)
2)
Reference :       
"""
from data_operation import OperateExcel
import os

def excel_read2txt():

    # 先移除所有文件
    txt_file_path = r'.\corpus'
    txt_names = os.listdir(txt_file_path)
    for i, name0 in enumerate(txt_names):
        path = txt_file_path + '\\' + name0
        os.remove(path)

    bom_path = r'.\bom_test'  # 读取文件夹路径!!!!!!!!!!!!
    file_names = os.listdir(bom_path)

    for i, name0 in enumerate(file_names):  # 文件夹下文件循环
        if '~$' in name0:
            continue
        print('==========================')
        excel_path = bom_path + '\\' + name0

        print(name0)
        bom_i = OperateExcel(excel_path)
        bom_i_name = name0.split('.')[0]
        bom_i.excel_write_in(f'.\corpus\{bom_i_name}.txt')  # 追加



if __name__ == "__main__":
    pass

    excel_read2txt()