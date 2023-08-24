'''
Author: SpenserCai
Date: 2023-08-23 23:04:55
version: 
LastEditors: SpenserCai
LastEditTime: 2023-08-24 11:25:54
Description: file content
'''
import os
import launch
import urllib.request
from tqdm import tqdm
from scripts.base import *

init_base()

if (not check_bin()) or need_update():
    download_bin()