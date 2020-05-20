# -*- coding: utf-8 -*-
"""
@Time : 2020/5/20 14:16
@Author : Dufy
@Email : 813540660@qq.com
@File : log.py
@Software: PyCharm 
Description :
1)
2)
Reference :       
"""
import os
import time
from data_operation.function import get_logger

if __name__ == "__main__":
    logger = get_logger()
    time0 = time.time()
    pass
    logger.info('info test.....')
    logger.error('error test.....')
    logger.critical('critical test.....')
    print(f'用时：{time.time() - time0}')
