# PORTRAIT MASTER
# Created by AI Wiz Art (Stefano Flore)
# Version: 2.9.2 (legacy)
# https://stefnoflore.it
# https://ai-wiz.art

# modified by Tiger (https://github.com/DropFan)
# 主要汉化了原版，将数据文件改为中英两行，未做大的改动

import os
import random

from .common import *
from .logger import logger

logger.info("Load data list ")

shotList, shotDict = load_data("shot.txt")
genderList, genderDict = load_data("gender.txt")
faceShapeList, faceShapeDict = load_data("face_shape.txt")
facialExpressionsList, facialExpressionsDict = load_data("face_expression.txt")
nationalityList, nationalityDict = load_data("nationality.txt")
hairStyleList, hairStyleDict = load_data("hair_style.txt")

lightTypeList, lightTypeDict = load_data("light_type.txt")
lightDirectionList, lightDirectionDict = load_data("light_direction.txt")

eyeColorList, eyeColorDict = load_data("eyes_color.txt")
eyeShapeList, eyeShapeDict = load_data("eyes_shape.txt")

beardColorList, beardColorDict = load_data("beard_color.txt")

hairColorList, hairColorDict = load_data("hair_color.txt")
hairLengthList, hairLengthDict = load_data("hair_length.txt")

bodyTypeList, bodyTypeDict = load_data("body_type.txt")

beardList, beardDict = load_data("beard.txt")

modelPoseList, modelPoseDict = load_data("model_pose.txt")

style1List, style1Dict = load_data("style.txt")
style2List, style2Dict = load_data("style.txt")

lipsShapeList, lipsShapeDict = load_data("lips_shape.txt")
lipsColorList, lipsColorDict = load_data("lips_color.txt")

makeupList, makeupDict = load_data("makeup.txt")

clothesList, clothesDict = load_data("clothes.txt")

logger.info("Load data list done")

# Portrait Master version (Legacy)

class PortraitMasterLegacy:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        max_float_value = 1.95
        return {
            "optional": {
                "seed": ("INT", {"forceInput": False}),
            },
            "required": {
                "镜头类型": (['-'] + shotList, {
                    "default": shotList[0],
                }),
                "镜头权重": ("FLOAT", {
                    "default": 0,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "性别": (['-'] + genderList, {
                    "default": "女",
                }),
                "跨性别程度": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "年龄": ("INT", {
                    "default": 22,
                    "min":0,
                    "max":100,
                }),
                "国籍_1": (['-'] + nationalityList, {
                    "default": "中国人",
                }),
                "国籍_2": (['-'] + nationalityList, {
                    "default": "-",
                }),
                "国籍混血": ("FLOAT", {
                    "default": 0.5,
                    "min": 0,
                    "max": 1,
                    "step": 0.05,
                    "display": "slider",
                }),
                "体型": (['-'] + bodyTypeList, {
                    "default": "-",
                }),
                "体型权重": ("FLOAT", {
                    "default": 0,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "模特姿势": (['-'] + modelPoseList, {
                    "default": "-",
                }),
                "服装": (['-'] + clothesList, {
                    "default": "-",
                }),
                "眼睛颜色": (['-'] + eyeColorList, {
                    "default": "-",
                }),
                "眼睛形状": (['-'] + eyeShapeList, {
                    "default": '-',
                }),
                "唇色": (['-'] + lipsColorList, {
                    "default": '-',
                }),
                "唇形": (['-'] + lipsShapeList, {
                    "default": '-',
                }),
                "表情": (['-'] + facialExpressionsList, {
                    "default": '-',
                }),
                "表情权重": ("FLOAT", {
                    "default": 0,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "脸型": (['-'] + faceShapeList, {
                    "default": '-',
                }),
                "脸型权重": ("FLOAT", {
                    "default": 0,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "面部不对称": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "发型": (['-'] + hairStyleList, {
                    "default": '-',
                }),
                "发型颜色": (['-'] + hairColorList, {
                    "default": '-',
                }),
                "头发长度": (['-'] + hairLengthList, {
                    "default": '-',
                }),
                "凌乱程度": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "妆容": (['-'] + makeupList, {
                    "default": '-',
                }),
                "胡子": (['-'] + beardList, {
                    "default": '-',
                }),
                "自然皮肤": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "素颜": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "洗脸程度": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "干脸程度": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "皮肤细节": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "皮肤毛孔": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "酒窝": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "皱纹": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "雀斑": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "痣": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "皮肤瑕疵": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "皮肤痤疮": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "晒黑_小麦色皮肤": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "眼睛细节": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "虹膜细节": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "环形虹膜": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "圆形瞳孔": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "光照类型": (['-'] + lightTypeList, {
                    "default": '-',
                }),
                "光照方向": (['-'] + lightDirectionList, {
                    "default": '-',
                }),
                "光照权重": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "照片写实增强": (["enable", "disable"],),
                "prompt_start": ("STRING", {
                    "multiline": True,
                    "default": "raw photo, (realistic:1.5)"
                }),
                "prompt_additional": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "prompt_end": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "negative_prompt": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "style_1": (['-'] + style1List, {
                    "default": '-',
                }),
                "style_1_weight": ("FLOAT", {
                    "default": 1.5,
                    "min": 1,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "style_2": (['-'] + style2List, {
                    "default": '-',
                }),
                "style_2_weight": ("FLOAT", {
                    "default": 1.5,
                    "min": 1,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "随机镜头": ("BOOLEAN", {"default": False}),
                "随机性别": ("BOOLEAN", {"default": False}),
                "随机年龄": ("BOOLEAN", {"default": False}),
                "随机跨性别": ("BOOLEAN", {"default": False}),
                "随机种族": ("BOOLEAN", {"default": False}),
                "随机体型": ("BOOLEAN", {"default": False}),
                "随机模特姿势": ("BOOLEAN", {"default": False}),
                "随机服装": ("BOOLEAN", {"default": False}),
                "随机眼睛颜色": ("BOOLEAN", {"default": False}),
                "随机眼睛形状": ("BOOLEAN", {"default": False}),
                "随机唇色": ("BOOLEAN", {"default": False}),
                "随机唇形": ("BOOLEAN", {"default": False}),
                "随机面部表情": ("BOOLEAN", {"default": False}),
                "随机脸型": ("BOOLEAN", {"default": False}),
                "随机发型": ("BOOLEAN", {"default": False}),
                "随机发色": ("BOOLEAN", {"default": False}),
                "随机头发长度": ("BOOLEAN", {"default": False}),
                "随机凌乱": ("BOOLEAN", {"default": False}),
                "随机妆容": ("BOOLEAN", {"default": False}),
                "随机雀斑": ("BOOLEAN", {"default": False}),
                "随机痣": ("BOOLEAN", {"default": False}),
                "随机皮肤瑕疵": ("BOOLEAN", {"default": False}),
                "随机胡子": ("BOOLEAN", {"default": False}),
                "random_style_1": ("BOOLEAN", {"default": False}),
                "random_style_2": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("STRING","STRING",)
    RETURN_NAMES = ("positive", "negative",)

    FUNCTION = "pm"

    CATEGORY = CATEGORY

    def pm(self, 镜头类型="-", 镜头权重=1, 性别="-", 体型="-", 体型权重=0, 眼睛颜色="-", 表情="-", 表情权重=0, 脸型="-", 脸型权重=0, 国籍_1="-", 国籍_2="-", 国籍混血=0.5, 年龄=30, 发型="-", 发型颜色="-", 凌乱程度=0, 酒窝=0, 雀斑=0, 皮肤毛孔=0, 皮肤细节=0, 痣=0, 皮肤瑕疵=0, 皱纹=0, 晒黑_小麦色皮肤=0, 眼睛细节=1, 虹膜细节=1, 环形虹膜=1, 圆形瞳孔=1, 面部不对称=0, prompt_additional="", prompt_start="", prompt_end="", 光照类型="-", 光照方向="-", 光照权重=0, negative_prompt="", 照片写实增强="disable", 胡子="-", 模特姿势="-", 皮肤痤疮=0, style_1="-", style_1_weight=0, style_2="-", style_2_weight=0, 跨性别程度=0, 自然皮肤=0, 素颜=0, 洗脸程度=0, 干脸程度=0, 随机性别=False, 随机年龄=False, 随机种族=False, 随机体型=False,随机发型=False, 随机眼睛颜色=False, 随机发色=False, 随机凌乱=False, 随机雀斑=False, 随机痣=False, 随机胡子=False, 随机镜头=False, 随机跨性别=False, 随机面部表情=False, 随机皮肤瑕疵=False, random_style_1=False, random_style_2=False, random_body_type=False, 随机模特姿势=False, 头发长度="-", 随机头发长度=False, 眼睛形状="-", 随机眼睛形状=False, 唇色="-", 随机唇色=False, 唇形="-", 随机唇形=False, 妆容="-", 随机妆容=False, 服装="-", 随机服装=False, 随机脸型=False, seed=0):

        prompt = []

        # RANDOMIZER SWITCHES

        if 随机镜头:
            镜头类型 = random.choice(shotList)
            镜头权重 = random.uniform(0.5,1.25)

        if 随机性别:
            性别 = random.choice(genderList)

        if 随机年龄:
            年龄 = random.randint(18,75)

        if 随机种族:
            国籍_1 = random.choice(nationalityList)
            国籍_2 = "-"

        if 随机发型:
            发型 = random.choice(hairStyleList)
            发型颜色 = random.choice(hairColorList)

        if 随机模特姿势:
            模特姿势 = random.choice(modelPoseList)

        if 随机眼睛颜色:
            眼睛颜色 = random.choice(eyeColorList)

        if 随机眼睛形状:
            眼睛形状 = random.choice(eyeShapeList)

        if 随机唇色:
            唇色 = random.choice(lipsColorList)

        if 随机唇形:
            唇形 = random.choice(lipsShapeList)

        if 随机发色:
            发型颜色 = random.choice(hairColorList)

        if 随机头发长度:
            头发长度 = random.choice(hairLengthList)

        if 随机面部表情:
            表情 = random.choice(facialExpressionsList)
            表情权重 = random.uniform(0.5,1.25)

        if 随机脸型:
            脸型 = random.choice(faceShapeList)
            脸型权重 = random.uniform(0.5,1.25)

        if 随机体型:
            体型 = random.choice(bodyTypeList)
            体型权重 = random.uniform(0.25,1.25)

        if 随机胡子:
            胡子 = random.choice(beardList)

        if 随机跨性别:
            跨性别程度 = random.uniform(0,1)

        if 随机凌乱:
            凌乱程度 = random.uniform(0,1.35)

        if 随机服装:
            服装 = random.choice(clothesList)

        if 随机妆容:
            妆容 = random.choice(makeupList)

        if 随机雀斑:
            雀斑 = random.uniform(0,1.35)

        if 随机痣:
            痣 = random.uniform(0,1.35)

        if random_style_1:
            style_1 = random.choice(style1List)
            style_1_weight = random.uniform(0.5,1.5)

        if random_style_2:
            style_2 = random.choice(style2List)
            style_2_weight = random.uniform(0.5,1.5)

        if 随机皮肤瑕疵:
            皮肤瑕疵 = random.uniform(0.15,1)

        # OPTIONS

        if 性别 == "-":
            性别 = ""
        else:
            性别 = genderDict[性别] + " "

        if 国籍_1 != '-' and 国籍_2 != '-':
            nationality = f"[{nationalityDict[国籍_1]}:{nationalityDict[国籍_2]}:{round(国籍混血, 2)}] "
        elif 国籍_1 != '-':
            nationality = nationalityDict[国籍_1] + " "
        elif 国籍_2 != '-':
            nationality = nationalityDict[国籍_2] + " "
        else:
            nationality = ""

        if prompt_start != "":
            prompt.append(f"{prompt_start}")

        if 镜头类型 != "-" and 镜头权重 > 0:
            prompt.append(applyWeight(shotDict[镜头类型],镜头权重))

        prompt.append(f"({nationality}{性别}{年龄}-years-old:1.5)")

        if 跨性别程度 > 0:
            prompt.append(applyWeight('androgynous',跨性别程度))

        if 体型 != "-" and 体型权重 > 0:
            prompt.append(applyWeight(f"{bodyTypeDict[体型]}, {bodyTypeDict[体型]} body",体型权重))

        if 模特姿势 != "-":
            prompt.append(f"({modelPoseDict[模特姿势]}:1.25)")

        if 服装 != "-":
            prompt.append(f"({clothesDict[服装]}:1.05)")

        if 眼睛颜色 != "-":
            prompt.append(f"({eyeColorDict[眼睛颜色]} eyes:1.05)")

        if 眼睛形状 != "-":
            prompt.append(f"({eyeShapeDict[眼睛形状]}:1.05)")

        if 唇色 != "-":
            prompt.append(f"({lipsColorDict[唇色]}:1.05)")

        if 唇形 != "-":
            prompt.append(f"({lipsShapeDict[唇形]}:1.05)")

        if 妆容 != "-":
            prompt.append(f"({makeupDict[妆容]}:1.05)")

        if 表情 != "-" and 表情权重 > 0:
            prompt.append(applyWeight(f"{facialExpressionsDict[表情]}, {facialExpressionsDict[表情]} expression",表情权重))

        if 脸型 != "-" and 脸型权重 > 0:
            prompt.append(applyWeight(f"{faceShapeDict[脸型]} shape face",脸型权重))

        if 发型 != "-":
            prompt.append(f"({hairStyleDict[发型]} cut hairstyle:1.05)")

        if 发型颜色 != "-":
            prompt.append(f"({hairColorDict[发型颜色]} hair:1.05)")

        if 头发长度 != "-":
            prompt.append(f"({hairLengthDict[头发长度]}:1.05)")

        if 胡子 != "-":
            prompt.append(f"({beardColorDict[胡子]}:1.15)")

        if 凌乱程度 != "-" and 凌乱程度 > 0:
            prompt.append(applyWeight('disheveled',凌乱程度))

        if prompt_additional != "":
            prompt.append(f"{prompt_additional}")

        if 自然皮肤 > 0:
            prompt.append(applyWeight('natural skin',自然皮肤))

        if 素颜 > 0:
            prompt.append(applyWeight('bare face',素颜))

        if 洗脸程度 > 0:
            prompt.append(applyWeight('washed-face',洗脸程度))

        if 干脸程度 > 0:
            prompt.append(applyWeight('dried-face',干脸程度))

        if 皮肤细节 > 0:
            prompt.append(applyWeight('skin details, skin texture',皮肤细节))

        if 皮肤毛孔 > 0:
            prompt.append(applyWeight('skin pores',皮肤毛孔))

        if 皮肤瑕疵 > 0:
            prompt.append(applyWeight('skin imperfections',皮肤瑕疵))

        if 皮肤痤疮 > 0:
            prompt.append(applyWeight('acne, skin with acne',皮肤痤疮))

        if 皱纹 > 0:
            prompt.append(applyWeight('wrinkles',皱纹))

        if 晒黑_小麦色皮肤 > 0:
            prompt.append(applyWeight('tanned skin',晒黑_小麦色皮肤))

        if 酒窝 > 0:
            prompt.append(applyWeight('dimples',酒窝))

        if 雀斑 > 0:
            prompt.append(applyWeight('freckles',雀斑))

        if 痣 > 0:
            prompt.append(applyWeight('moles',痣))

        if 眼睛细节 > 0:
            prompt.append(applyWeight('eyes details',眼睛细节))

        if 虹膜细节 > 0:
            prompt.append(applyWeight('iris details',虹膜细节))

        if 环形虹膜 > 0:
            prompt.append(applyWeight('circular details',环形虹膜))

        if 圆形瞳孔 > 0:
            prompt.append(applyWeight('circular pupil',圆形瞳孔))

        if 面部不对称 > 0:
            prompt.append(applyWeight('facial asymmetry, face asymmetry',面部不对称))

        if 光照类型 != '-' and 光照权重 > 0:
            if 光照方向 != '-':
                prompt.append(applyWeight(f"{lightTypeDict[光照类型]} {lightDirectionDict[光照方向]}",光照权重))
            else:
                prompt.append(applyWeight(f"{lightTypeDict[光照类型]}",光照权重))

        if style_1 != '-' and style_1_weight > 0:
            prompt.append(applyWeight(style_1,style_1_weight))

        if style_2 != '-' and style_2_weight > 0:
            prompt.append(applyWeight(style_2,style_2_weight))

        if prompt_end != "":
            prompt.append(f"{prompt_end}")

        prompt = ", ".join(prompt)
        prompt = prompt.lower()

        if 照片写实增强 == "enable":
            prompt = prompt + ", (professional photo, balanced photo, balanced exposure:1.2)"
            # prompt = prompt + ", (detailed, professional photo, perfect exposition:1.25), (film grain:1.5)"

        if 照片写实增强 == "enable":
            negative_prompt = negative_prompt + ", (shinny skin, shiny skin, reflections on the skin, skin reflections:1.35)"

        print("=============================================================")
        logger.info("Portrait Master positive prompt:")
        print(prompt)
        print("")
        logger.info("Portrait Master negative prompt:")
        print(negative_prompt)
        print("=============================================================")

        return (prompt,negative_prompt,)
