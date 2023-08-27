<!--
 * @Author: SpenserCai
 * @Date: 2023-08-24 00:06:52
 * @version: 
 * @LastEditors: SpenserCai
 * @LastEditTime: 2023-08-27 15:19:10
 * @Description: file content
-->
# SD-WEBUI-DISCORD-EX
This is an extension of [SD-WEBUI-DISCORD](https://github.com/SpenserCai/sd-webui-discord) on the Stable Diffusion WebUI, which supports distributed deployment of SD node's Stable Diffusion WebUi Discord robots. The command usage on Discord can refer to the [SD-WEBUI-DISCORD](https://github.com/SpenserCai/sd-webui-discord) project.

<img src="./.github/image/controlnet_2.jpeg" />

## Usage
You need to install the following extensions on the SD webui:

[sd-webui-segment-anythin](https://github.com/continue-revolution/sd-webui-segment-anything)

[sd-weubi-deoldify](https://github.com/SpenserCai/sd-webui-deoldify)

[stable-diffusion-webui-rembg](https://github.com/AUTOMATIC1111/stable-diffusion-webui-rembg)

[sd-webui-roop](https://github.com/s0md3v/sd-webui-roop)

[sd-webui-controlnet](https://github.com/Mikubill/sd-webui-controlnet)

***

1. Install this extensions from the 'Extensions' tab page of the Stable Diffusion WebUI.

2. Create a Discord bot and get the bot token. The tutorial can be found [here](https://discord.com/developers/docs/getting-started).

3. Set the bot token in `stable-diffusion-webui/extensions/sd-webui-discord-ex/bin/config.json`.Only need set host and token and server_id(if you don't know set it empty like `"server_id": ""`).
```json
{
    "sd_webui":{
        "servers":[
            {
                "name":"webui-1",
                "host":"127.0.0.1:7860",
                "max_concurrent":5,
                "max_queue":100,
                "max_vram":"20G"
            }
        ]
    },
    "discord":{
        "token":"<your token here>",
        "server_id":"<your servers id here if empty all servers>"
    }
}
```

If you want set default value with sd-webui
```json
{
    "sd_webui":{
        "servers":[...],
        "default_setting": {
            "cfg_scale": 8,
            "negative_prompt": "bad,text,watermask",
            "height":1024,
            "width":1024,
            "steps":32
        }
    }
    ...
}
```

4. Restart the Stable Diffusion WebUI.
   
5. Find `Discord` tab and click `Start` button to start the Discord bot.

## Tips
1. The installation script retrieves the binary file from the Release of SD-WEBUI-DISCORD, which is automatically compiled by Github Action. Alternatively, you can compile SD-WEBUI-DISCORD yourself and place it in the 'bin' directory of the plugin directory.
