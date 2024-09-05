
import random

from .common import *

# Portrait Master Base Character

class PortraitMasterBaseCharacter:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        max_float_value = 2
        return {
            "optional": {
                "text_in": ("STRING", {"forceInput": True}),
                "seed": ("INT", {"forceInput": True}),
            },
            "required": {
                "镜头": (['-'] + [rand_opt] + lists['shot'], {
                    "default": '-',
                }),
                "镜头权重": ("FLOAT", {
                    "default": 1,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "性别": (['-'] + [rand_opt] + lists['gender'], {
                    "default": '-',
                }),
                "跨性别程度": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "丑陋程度": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "大众脸": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # "age": (['-'] + [rand_opt] + lists['age'], {
                #     "default": '-',
                # }),
                "年龄": ("INT", {
                    "default": 22,
                    "min": 1,
                    "max": 120,
                    "step": 1,
                }),
                "国籍_1": (['-'] + [rand_opt] + lists['nationality'], {
                    "default": '-',
                }),
                "国籍_2": (['-'] + [rand_opt] + lists['nationality'], {
                    "default": '-',
                }),
                "国籍混血": ("FLOAT", {
                    "default": 0.5,
                    "min": 0,
                    "max": 1,
                    "step": 0.05,
                    "display": "slider",
                }),
                "体型": (['-'] + [rand_opt] + lists['body_type'], {
                    "default": '-',
                }),
                "体型权重": ("FLOAT", {
                    "default": 1,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "眼睛颜色": (['-'] + [rand_opt] + lists['eyes_color'], {
                    "default": '-',
                }),
                "眼睛形状": (['-'] + [rand_opt] + lists['eyes_shape'], {
                    "default": '-',
                }),
                "唇色": (['-'] + [rand_opt] + lists['lips_color'], {
                    "default": '-',
                }),
                "唇形": (['-'] + [rand_opt] + lists['lips_shape'], {
                    "default": '-',
                }),
                "面部表情": (['-'] + [rand_opt] + lists['face_expression'], {
                    "default": '-',
                }),
                "面部表情权重": ("FLOAT", {
                    "default": 1,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "脸型": (['-'] + [rand_opt] + lists['face_shape'], {
                    "default": '-',
                }),
                "脸型权重": ("FLOAT", {
                    "default": 1,
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
                "发型": (['-'] + [rand_opt] + lists['hair_style'], {
                    "default": '-',
                }),
                "发色": (['-'] + [rand_opt] + lists['hair_color'], {
                    "default": '-',
                }),
                "头发长度": (['-'] + [rand_opt] + lists['hair_length'], {
                    "default": '-',
                }),
                "凌乱程度": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "胡子": (['-'] + [rand_opt] + lists['beard'], {
                    "default": '-',
                }),
                "胡子颜色": (['-'] + [rand_opt] + lists['beard_color'], {
                    "default": '-',
                }),
                "启用": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)

    FUNCTION = "pmbc"

    CATEGORY = CATEGORY

    def pmbc(
            self,
            text_in='',
            seed=0,
            镜头='-',
            镜头权重=1,
            性别='-',
            跨性别程度=0,
            丑陋程度=0,
            大众脸=0,
            年龄=30,
            国籍_1='-',
            国籍_2='-',
            国籍混血=0.5,
            体型='-',
            体型权重=1,
            眼睛颜色='-',
            眼睛形状='-',
            唇色='-',
            唇形='-',
            面部表情='-',
            面部表情权重=1,
            脸型='-',
            脸型权重=1,
            面部不对称=0,
            发型='-',
            发色='-',
            头发长度='-',
            凌乱程度=0,
            胡子='-',
            胡子颜色='-',
            启用=True
        ):

        prompt = []

        if text_in != '':
            prompt.append(text_in)

        if 启用:

            if 镜头权重 > 0:
                if 镜头 == rand_opt:
                    镜头 = random.choice(lists['shot'])
                if 镜头 != '-':
                    prompt.append(applyWeight(dicts['shot'][镜头],镜头权重))

            if 性别 == rand_opt:
                gender_opt = random.choice(lists['gender']) + ' '
            elif 性别 != '-':
                gender_opt = dicts['gender'][性别] + ' '
            else:
                gender_opt = ''

            if 年龄 == rand_opt:
                age_opt = str(random.randint(18, 100)) + '-years-old '
            elif 年龄 != '-':
                age_opt = f'{年龄}-years-old '
            else:
                age_opt = ''

            if 跨性别程度 > 0:
                androgynous_opt = applyWeight('androgynous',跨性别程度) + ' '
            else:
                androgynous_opt = ''

            if 丑陋程度 > 0:
                ugly_opt = applyWeight('ugly',丑陋程度) + ' '
            else:
                ugly_opt = ''

            nationality = ''
            nationality_1_opt = ''
            nationality_2_opt = ''
            if 国籍_1 != '-':
                nationality_1_opt = random.choice(lists['nationality']) if 国籍_1 == rand_opt else dicts['nationality'][国籍_1]
            if 国籍_2 != '-':
                nationality_2_opt = random.choice(lists['nationality']) if 国籍_2 == rand_opt else dicts['nationality'][国籍_2]

            if nationality_1_opt and nationality_2_opt and nationality_1_opt != '-' and nationality_2_opt != '-':
                nationality = f'[{nationality_1_opt}:{nationality_2_opt}:{str(round(国籍混血, 2))}] '
            elif nationality_1_opt and nationality_1_opt != '-':
                nationality = nationality_1_opt + ' '
            elif nationality_2_opt and nationality_2_opt != '-':
                nationality = nationality_2_opt+ ' '

            if androgynous_opt + ugly_opt + nationality + gender_opt + age_opt != '':
                t = f'({androgynous_opt}{ugly_opt}{nationality}{gender_opt}{age_opt}:1.15)'
                t = t.strip()
                prompt.append(t)

            if 大众脸 > 0:
                prompt.append(applyWeight('ordinary face',大众脸))

            if 体型权重 > 0:
                if 体型 == rand_opt:
                    体型 = random.choice(lists['body_type'])
                if 体型 != '-':
                    prompt.append(applyWeight(dicts['body_type'][体型],体型权重))

            if 眼睛颜色 == rand_opt:
                眼睛颜色 = random.choice(lists['eyes_color'])
            if 眼睛颜色 != '-':
                prompt.append('(' + dicts['eyes_color'][眼睛颜色] + ' eyes:1.05)')

            if 眼睛形状 == rand_opt:
                眼睛形状 = random.choice(lists['eyes_shape'])
            if 眼睛形状 != '-':
                prompt.append('(' + dicts['eyes_shape'][眼睛形状] + ':1.05)')

            if 唇色 == rand_opt:
                唇色 = random.choice(lists['lips_color'])
            if 唇色 != '-':
                prompt.append('(' + dicts['lips_color'][唇色] + ':1.05)')

            if 唇形 == rand_opt:
                唇形 = random.choice(lists['lips_shape'])
            if 唇形 != '-':
                prompt.append('(' + dicts['lips_shape'][唇形] + ':1.05)')

            if 面部表情权重 > 0:
                if 面部表情 == rand_opt:
                    面部表情 = random.choice(lists['face_expression'])
                if 面部表情 != '-':
                    prompt.append(applyWeight(dicts['face_expression'][面部表情],面部表情权重))

            if 脸型权重 > 0:
                if 脸型 == rand_opt:
                    脸型 = random.choice(lists['face_shape'])
                if 脸型 != '-':
                    prompt.append(applyWeight(dicts['face_shape'][脸型] + ' face-shape',脸型权重))

            if 面部不对称 > 0:
                prompt.append(applyWeight('facial asymmetry, face asymmetry',面部不对称))

            if 发型 == rand_opt:
                发型 = random.choice(lists['hair_style'])
            if 发型 != '-':
                prompt.append('(' + dicts['hair_style'][发型] + ' hair style:1.05)')

            if 发色 == rand_opt:
                发色 = random.choice(lists['hair_color'])
            if 发色 != '-':
                prompt.append('(' + dicts['hair_color'][发色] + ' hair color:1.05)')

            if 头发长度 == rand_opt:
                头发长度 = random.choice(lists['hair_length'])
            if 头发长度 != '-':
                prompt.append('(' + dicts['hair_length'][头发长度] + ' hair length:1.05)')

            if 凌乱程度 > 0:
                prompt.append(applyWeight('disheveled',凌乱程度))

            if 胡子 == rand_opt:
                胡子 = random.choice(lists['beard'])
            if 胡子 != '-':
                prompt.append('(' + dicts['beard'][胡子] + ':1.05)"')

            if 胡子颜色 == rand_opt:
                胡子颜色 = random.choice(lists['beard_color'])
            if 胡子颜色 != '-':
                prompt.append('(' + dicts['beard_color'][胡子颜色] + ' beard color:1.05)"')

        if len(prompt) > 0:
            prompt = ', '.join(prompt)
            prompt = prompt.lower()
            return(prompt,)
        else:
            return('',)