
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
                "shot": (['-'] + [rand_opt] + lists['shot'], {
                    "default": '-',
                }),
                "shot_weight": ("FLOAT", {
                    "default": 1,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "gender": (['-'] + [rand_opt] + lists['gender'], {
                    "default": '-',
                }),
                "androgynous": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "ugly": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "ordinary_face": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                # "age": (['-'] + [rand_opt] + lists['age'], {
                #     "default": '-',
                # }),
                "age": ("INT", {
                    "default": 0,
                    "min": 1,
                    "max": 120,
                    "step": 1,
                    "display": "slider",
                }),
                "nationality_1": (['-'] + [rand_opt] + lists['nationality'], {
                    "default": '-',
                }),
                "nationality_2": (['-'] + [rand_opt] + lists['nationality'], {
                    "default": '-',
                }),
                "nationality_mix": ("FLOAT", {
                    "default": 0.5,
                    "min": 0,
                    "max": 1,
                    "step": 0.05,
                    "display": "slider",
                }),
                "body_type": (['-'] + [rand_opt] + lists['body_type'], {
                    "default": '-',
                }),
                "body_type_weight": ("FLOAT", {
                    "default": 1,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "eyes_color": (['-'] + [rand_opt] + lists['eyes_color'], {
                    "default": '-',
                }),
                "eyes_shape": (['-'] + [rand_opt] + lists['eyes_shape'], {
                    "default": '-',
                }),
                "lips_color": (['-'] + [rand_opt] + lists['lips_color'], {
                    "default": '-',
                }),
                "lips_shape": (['-'] + [rand_opt] + lists['lips_shape'], {
                    "default": '-',
                }),
                "facial_expression": (['-'] + [rand_opt] + lists['face_expression'], {
                    "default": '-',
                }),
                "facial_expression_weight": ("FLOAT", {
                    "default": 1,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "face_shape": (['-'] + [rand_opt] + lists['face_shape'], {
                    "default": '-',
                }),
                "face_shape_weight": ("FLOAT", {
                    "default": 1,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "facial_asymmetry": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "hair_style": (['-'] + [rand_opt] + lists['hair_style'], {
                    "default": '-',
                }),
                "hair_color": (['-'] + [rand_opt] + lists['hair_color'], {
                    "default": '-',
                }),
                "hair_length": (['-'] + [rand_opt] + lists['hair_length'], {
                    "default": '-',
                }),
                "disheveled": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "beard": (['-'] + [rand_opt] + lists['beard'], {
                    "default": '-',
                }),
                "beard_color": (['-'] + [rand_opt] + lists['beard_color'], {
                    "default": '-',
                }),
                "active": ("BOOLEAN", {"default": True}),
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
            shot='-',
            shot_weight=1,
            gender='-',
            androgynous=0,
            ugly=0,
            ordinary_face=0,
            age=30,
            nationality_1='-',
            nationality_2='-',
            nationality_mix=0.5,
            body_type='-',
            body_type_weight=1,
            eyes_color='-',
            eyes_shape='-',
            lips_color='-',
            lips_shape='-',
            facial_expression='-',
            facial_expression_weight=1,
            face_shape='-',
            face_shape_weight=1,
            facial_asymmetry=0,
            hair_style='-',
            hair_color='-',
            hair_length='-',
            disheveled=0,
            beard='-',
            beard_color='-',
            active=True
        ):

        prompt = []

        if text_in != '':
            prompt.append(text_in)

        if active:

            if shot_weight > 0:
                if shot == rand_opt:
                    prompt.append(applyWeight(random.choice(lists['shot']),shot_weight))
                elif shot != '-':
                    prompt.append(applyWeight(shot,shot_weight))

            if gender == rand_opt:
                gender_opt = random.choice(lists['gender']) + ' '
            elif gender != '-':
                gender_opt = gender + ' '
            else:
                gender_opt = ''

            if age == rand_opt:
                age_opt = random.choice(lists['age']) + '-years-old '
            elif age != '-':
                age_opt = f'{age}-years-old '
            else:
                age_opt = ''

            if androgynous > 0:
                androgynous_opt = applyWeight('androgynous',androgynous) + ' '
            else:
                androgynous_opt = ''

            if ugly > 0:
                ugly_opt = applyWeight('ugly',ugly) + ' '
            else:
                ugly_opt = ''

            nationality = ''
            if nationality_1 != '-' or nationality_2 != '-':
                nationality_1_opt = random.choice(lists['nationality']) if nationality_1 == rand_opt else nationality_1
                nationality_2_opt = random.choice(lists['nationality']) if nationality_2 == rand_opt else nationality_2
                if nationality_1_opt and nationality_2_opt and nationality_1_opt != '-' and nationality_2_opt != '-':
                    nationality = f'[{nationality_1_opt}:{nationality_2_opt}:{str(round(nationality_mix, 2))}] '
                else:
                    nationality = nationality_1_opt + ' ' if nationality_1_opt != '-' else nationality_2_opt + ' '

            if androgynous_opt + ugly_opt + nationality + gender_opt + age_opt != '':
                t = f'({androgynous_opt}{ugly_opt}{nationality}{gender_opt}{age_opt}:1.15)'
                t = t.strip()
                prompt.append(t)

            if ordinary_face > 0:
                prompt.append(applyWeight('ordinary face',ordinary_face))

            if body_type_weight > 0:
                if body_type == rand_opt:
                    prompt.append(applyWeight(random.choice(lists['body_type']),body_type_weight))
                elif body_type != '-':
                    prompt.append(applyWeight(body_type,body_type_weight))

            if eyes_color == rand_opt:
                prompt.append('(' + random.choice(lists['eyes_color']) + ' eyes:1.05)')
            elif eyes_color != '-':
                prompt.append('(' + eyes_color + ' eyes:1.05)')

            if eyes_shape == rand_opt:
                prompt.append('(' + random.choice(lists['eyes_shape']) + ':1.05)')
            elif eyes_shape != '-':
                prompt.append('(' + eyes_shape + ':1.05)')

            if lips_color == rand_opt:
                prompt.append('(' + random.choice(lists['lips_color']) + ':1.05)')
            elif lips_color != '-':
                prompt.append('(' + lips_color + ':1.05)')

            if lips_shape == rand_opt:
                prompt.append('(' + random.choice(lists['lips_shape']) + ':1.05)')
            elif lips_shape != '-':
                prompt.append('(' + lips_shape + ':1.05)')

            if facial_expression_weight > 0:
                if facial_expression == rand_opt:
                    prompt.append(applyWeight(random.choice(lists['face_expression']),facial_expression_weight))
                elif facial_expression != '-':
                    prompt.append(applyWeight(facial_expression,facial_expression_weight))

            if face_shape_weight > 0:
                if face_shape == rand_opt:
                    prompt.append(applyWeight(random.choice(lists['face_shape']) + ' face-shape',face_shape_weight))
                elif face_shape != '-':
                    prompt.append(applyWeight(face_shape + ' face-shape',face_shape_weight))

            if facial_asymmetry > 0:
                prompt.append(applyWeight('facial asymmetry, face asymmetry',facial_asymmetry))

            if hair_style == rand_opt:
                prompt.append('(' + random.choice(lists['hair_style']) + ' hair style:1.05)')
            elif hair_style != '-':
                prompt.append('(' + hair_style + ' hair style:1.05)')

            if hair_color == rand_opt:
                prompt.append('(' + random.choice(lists['hair_color']) + ' hair color:1.05)')
            elif hair_color != '-':
                prompt.append('(' + hair_color + ' hair color:1.05)')

            if hair_length == rand_opt:
                prompt.append('(' + random.choice(lists['hair_length']) + ' hair length:1.05)')
            elif hair_length != '-':
                prompt.append('(' + hair_length + ' hair length:1.05)')

            if disheveled > 0:
                prompt.append(applyWeight('disheveled',disheveled))

            if beard == rand_opt:
                prompt.append('(' + random.choice(lists['beard']) + ':1.05)"')
            elif beard != '-':
                prompt.append('(' + beard + ':1.05)"')

            if beard_color == rand_opt:
                prompt.append('(' + random.choice(lists['beard_color']) + ' beard color:1.05)"')
            elif beard_color != '-':
                prompt.append('(' + beard_color + ' beard color:1.05)"')

        if len(prompt) > 0:
            prompt = ', '.join(prompt)
            prompt = prompt.lower()
            return(prompt,)
        else:
            return('',)