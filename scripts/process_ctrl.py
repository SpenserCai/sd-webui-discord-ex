import subprocess
import threading
import os
from scripts.base import get_bin_process_path

class ProcessCtrl:
    __status = False
    __process = None
    __thread = None
    AllLogData = ""
    LogData = ""

    def _start_process():
        ProcessCtrl.AllLogData = ""
        ProcessCtrl.LogData = ""
        ProcessCtrl.__process = subprocess.Popen(get_bin_process_path(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        for line in iter(ProcessCtrl.__process.stdout.readline, ""):
            ProcessCtrl.AllLogData += line
            # Limit LogData to 10 lines
            #if len(ProcessCtrl.AllLogData.split("\n")) > 10:
            #    ProcessCtrl.LogData = "\n".join(ProcessCtrl.AllLogData.split("\n")[-10:])
            #else:
            ProcessCtrl.LogData = ProcessCtrl.AllLogData
        ProcessCtrl.__process.wait()
        ProcessCtrl.__process = None
        ProcessCtrl.__status = False

    def start():
        ProcessCtrl.__status = True
        ProcessCtrl.__thread = threading.Thread(target=ProcessCtrl._start_process)
        ProcessCtrl.__thread.start()

    def stop():
        if ProcessCtrl.__process is not None:
            # Terminate the subprocess (Windows compatible)
            ProcessCtrl.__process.terminate()

    def is_running():
        return ProcessCtrl.__status
