# Portrait Master 汉化版
# 1.主要汉化了原版，将数据文件改为中英两行，代码结构做了拆分，功能未做大的改动。
# 2.仅汉化了 2.9.2 的经典版本 node，v3 版本只是拆分为几个细分 node, 暂时觉得没必要，先不汉化了。
# 3.另外添加了一个 ImageSaver (修改自 ComfyUI-Crystools)，用于保存 prompt 等元信息到 exif
# By Tiger (https://github.com/DropFan)

import os

CATEGORY = "肖像大师中文版 Portrait Master CN"

script_dir = os.path.dirname(__file__)

from .logger import logger

def load_data(file_path) -> tuple[list[str],dict[str,str]]:
    file_path = os.path.join(script_dir, "lists/"+file_path)
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            lst = [line.strip() for line in lines]

        if len(lst) == 0 or len(lst) % 2 != 0:
            logger.error('Error: Invalid data list format in "%s"'%file_path)
            return ([], {})
    except Exception as e:
        logger.error('Error: Failed to load data list "%s"'%file_path)
        return ([], {})

    keys = []
    result = {}
    for i in range(len(lst)):
        if i % 2 == 0:
            result[lst[i]] = lst[i + 1]
            keys.append(lst[i])

    return (keys, result)

# convert list to dict
def parseDataList(lst:list[str]) -> tuple[list[str],dict[str,str]]:
    if len(lst) == 0 or len(lst) % 2 != 0:
        logger.error("Error: Invalid data list format")
        return ([], {})

    keys = []
    result = {}
    for i in range(len(lst)):
        if i % 2 == 0:
            result[lst[i]] = lst[i + 1]
            keys.append(lst[i])

    return (keys, result)

# apply weight
def applyWeight(text, weight):
    if weight == 1:
        return text
    else:
        return f"({text}:{round(weight,2)})"

# global vars

rand_opt = 'random 🎲'

# Load lists

def load_data_lists():
    lists = {}
    dicts = {}
    list_names = [
        "shot", "gender", "face_shape", "face_expression", "nationality", "hair_style", "light_type", "light_direction", "eyes_color", "eyes_shape", "beard_color", "hair_color", "hair_length", "body_type", "beard", "model_pose", "style", "lips_shape", "lips_color", "makeup", "clothes", "makeup_color", "female_lingerie"
    ]
    for name in list_names:
        # filepath = os.path.join(script_dir, f"lists/{name}.txt")
        # lists[name] = pmReadTxt(list_path)
        # lists[name].sort()
        lists[name], dicts[name] = load_data(name+".txt")
    return lists, dicts

lists, dicts = load_data_lists()