'''
Author: SpenserCai
Date: 2023-08-23 23:04:55
version: 
LastEditors: SpenserCai
LastEditTime: 2023-08-24 00:13:14
Description: file content
'''
import os
import launch
import urllib.request
from tqdm import tqdm
from scripts.base import *

if not check_bin():
    download_bin()