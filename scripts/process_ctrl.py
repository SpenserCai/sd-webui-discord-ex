'''
Author: SpenserCai
Date: 2023-08-24 09:33:45
version: 
LastEditors: SpenserCai
LastEditTime: 2023-08-24 17:10:46
Description: file content
'''
import subprocess
import threading
from scripts.base import get_bin_process_path

# 单列类
class ProcessCtrl:
    __status = False
    __process = None
    __thread = None
    AllLogData = ""
    LogData = ""

    def _start_process():
        ProcessCtrl.__process = subprocess.Popen(get_bin_process_path(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        for line in iter(ProcessCtrl.__process.stdout.readline, ""):
            ProcessCtrl.AllLogData += line
            # LogData只保留最后20行
            if len(ProcessCtrl.AllLogData.split("\n")) > 20:
                ProcessCtrl.LogData = "\n".join(ProcessCtrl.AllLogData.split("\n")[-20:])
            else:
                ProcessCtrl.LogData = ProcessCtrl.AllLogData
        ProcessCtrl.__process.wait()
        ProcessCtrl.__process = None
        ProcessCtrl.__status = False


    def start():
        ProcessCtrl.__status = True
        ProcessCtrl.__thread = threading.Thread(target=ProcessCtrl._start_process)
        ProcessCtrl.__thread.start()

    def stop():
        if ProcessCtrl.__process != None:
            # 发送相当于Ctrl+C的信号
            ProcessCtrl.__process.send_signal(3)
            ProcessCtrl.__process = None

    def is_running():
        return ProcessCtrl.__status

