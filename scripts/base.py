'''
Author: SpenserCai
Date: 2023-08-23 23:12:27
version: 
LastEditors: SpenserCai
LastEditTime: 2023-10-08 12:43:57
Description: file content
'''
import os
import modules.scripts as scripts
import requests
import sys
import tarfile
import shutil

bin_path = None
api_url = "https://api.github.com/repos/SpenserCai/sd-webui-discord/releases/latest"

def init_base():
    global bin_path
    bin_path = os.path.join(get_my_dir(), "bin")

def get_bin_path():
    return os.path.join(get_my_dir(), "bin")

def get_bin_process_path():
    if sys.platform == "win32":
        return os.path.join(get_bin_path(), "sd-webui-discord.exe")
    elif sys.platform == "linux":
        return os.path.join(get_bin_path(), "sd-webui-discord")

def get_my_dir():
    if os.path.isdir("extensions/sd-webui-discord-ex"):
        return "extensions/sd-webui-discord-ex"
    return scripts.basedir()

def check_bin():
    print(bin_path)
    if os.path.isfile(get_bin_process_path()):
        return True
    return False

def need_update():
    response = requests.get(api_url)
    data = response.json()
    tag_name = data["tag_name"]
    with open(os.path.join(bin_path, ".version"), "r") as file:
        version = file.read()
    version = version.strip()
    if tag_name == version:
        return False
    return True

def download_bin():
    response = requests.get(api_url)
    data = response.json()
    tag_name = data["tag_name"]
    print(f"Downloading sd-webui-discord {tag_name}...")
    download_url = f"https://github.com/SpenserCai/sd-webui-discord/releases/download/{tag_name}/sd-webui-discord-release-{tag_name}.tar.gz"
    response = requests.get(download_url)
    release_path = os.path.join(bin_path, f"sd-webui-discord-{tag_name}.tar.gz")
    with open(release_path, "wb") as file:
        file.write(response.content)
    print("Extracting sd-webui-discord...")
    with tarfile.open(release_path, "r:gz") as tar:
        members = [m for m in tar.getmembers() if m.name.startswith("release")]
        tar.extractall(path=bin_path, members=members)
    # 如果bin目录下存在location目录，删除
    if os.path.isdir(os.path.join(bin_path, "location")):
        shutil.rmtree(os.path.join(bin_path, "location"))
    # 如果bin目录下存在website目录，删除
    if os.path.isdir(os.path.join(bin_path, "website")):
        shutil.rmtree(os.path.join(bin_path, "website"))
    # 如果bin目录下存在dist目录，删除
    if os.path.isdir(os.path.join(bin_path, "dist")):
        shutil.rmtree(os.path.join(bin_path, "dist"))
    # 判断release目录是否存在，如果存在把里面的文件移动到bin目录下，然后删除release目录
    if os.path.isdir(os.path.join(bin_path, "release")):
        for file in os.listdir(os.path.join(bin_path, "release")):
            # 如果config.json存在，不移动
            if file == "config.json":
                if os.path.isfile(os.path.join(bin_path, file)):
                    continue
            # 如果文件存在，删除
            if os.path.isfile(os.path.join(bin_path, file)):
                os.remove(os.path.join(bin_path, file))
            shutil.move(os.path.join(bin_path, "release", file), bin_path)
        shutil.rmtree(os.path.join(bin_path, "release"))
    
    os.remove(release_path)

    with open(os.path.join(bin_path, ".version"), "w") as file:
        file.write(tag_name)
    print("Done!")
    

    