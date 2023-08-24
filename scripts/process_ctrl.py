'''
Author: SpenserCai
Date: 2023-08-24 09:33:45
version: 
LastEditors: SpenserCai
LastEditTime: 2023-08-24 14:26:24
Description: file content
'''
import subprocess
from scripts.base import get_bin_process_path

# 单列类
class ProcessCtrl:
    __status = False
    __process = None

    def start():
        ProcessCtrl.__status = True

    def stop():
        ProcessCtrl.__status = False

    def is_running():
        return ProcessCtrl.__status

