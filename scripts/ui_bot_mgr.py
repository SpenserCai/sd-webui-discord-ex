'''
Author: SpenserCai
Date: 2023-08-23 23:07:15
version: 
LastEditors: SpenserCai
LastEditTime: 2023-08-24 14:32:54
Description: file content
'''
from modules import script_callbacks, paths_internal
import gradio as gr
import tempfile
import os
import shutil
import json
from scripts import base
from scripts import process_ctrl

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
        return token[:5] + "*" * 10 + token[-5:]
    return token

def start(startButton:gr.Button,stopButton:gr.Button,log:gr.Textbox):
    startButton.visible = False
    stopButton.visible = True
    log.value += "Starting...\n"
    process_ctrl.ProcessCtrl.start()
    log.value += "Started\n"

def stop(startButton:gr.Button,stopButton:gr.Button,log:gr.Textbox):
    startButton.visible = True
    stopButton.visible = False
    log.value += "Stopping...\n"
    process_ctrl.ProcessCtrl.stop()
    log.value += "Stopped\n"


def discord_tab():
    with gr.Blocks(analytics_enabled=False) as ui:
        with gr.Row():
            with gr.Column():
                j_data = {
                    "token": get_desensitization_token(load_config("token")),
                    "server_id": load_config("server_id")
                }
                gr.JSON(j_data, label="Discord Config")
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
                stop = gr.Button("Stop",visible=False)
                start.click(inputs=[start,stop,log],outputs=[],fn=start)
                



    return [(ui,"Discord","Discord")]

script_callbacks.on_ui_tabs(discord_tab)