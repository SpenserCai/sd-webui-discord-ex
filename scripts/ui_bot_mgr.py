'''
Author: SpenserCai
Date: 2023-08-23 23:07:15
version: 
LastEditors: SpenserCai
LastEditTime: 2023-08-24 14:08:44
Description: file content
'''
from modules import script_callbacks, paths_internal
import gradio as gr
import tempfile
import os
import shutil
import json
from scripts import base

def load_config(key):
    jsonObject = {}
    config_path = os.path.join(base.get_bin_path(), "config.json")
    print(config_path)
    if os.path.isfile(config_path):
        with open(config_path, "r") as file:
            jsonObject = json.load(file)
    print(jsonObject)
    if key == "token":
        return jsonObject.get("discord", {}).get("token", "")
    elif key == "server_id":
        return jsonObject.get("discord", {}).get("server_id", "")
    elif key == "node_list":
        return jsonObject.get("sd_webui", {}).get("servers", [])
    
def get_desensitization_token(token):
    print(token)
    # 如果token不是<your token here>，则只保留开头和结尾各5个字符，如果总长度小于10，则全部替换为*
    if token != "<your token here>":
        if len(token) < 10:
            return "*" * len(token)
        return token[:5] + "*" * (len(token) - 10) + token[-5:]
    return token


def discord_tab():
    with gr.Blocks(analytics_enabled=False) as ui:
        with gr.Row():
            with gr.Column():
                gr.Label("DISCORD TOKEN:" + get_desensitization_token(load_config("token")))
                gr.Label("DISCORD SERVER ID:" + load_config("server_id"))

                gr.Label("WebUI NODE LIST")
                node_list = load_config("node_list")
                node_array = []
                for node in node_list:
                    node_array.append([node.get("name", ""), node.get("host", ""), node.get("max_concurrent", "")])
                n_dataframe = gr.Dataframe(headers=["Name","Host","MaxConcurrent"], type="array", label="Node List")
                n_dataframe.value = node_array
                
            with gr.Column():
                gr.Label("SD-WEBUI-DISCORD LOG")
                # 一个长文本框，显示日至，只读的
                log = gr.Textbox(lines=20, readonly=True)
                # 一个启动按钮
                start = gr.Button("Start")
                # 一个停止按钮
                stop = gr.Button("Stop")
                



    return [(ui,"Discord","Discord")]

script_callbacks.on_ui_tabs(discord_tab)