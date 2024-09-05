
import random

from .common import *


# Portrait Master Style & Pose

class PortraitMasterStylePose:

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
                "模特姿势": (['-'] + [rand_opt] + lists['model_pose'], {
                    "default": '-',
                }),
                "服装": (['-'] + [rand_opt] + lists['clothes'], {
                    "default": '-',
                }),
                "女士内衣": (['-'] + [rand_opt] + lists['female_lingerie'], {
                    "default": '-',
                }),
                "妆容": (['-'] + [rand_opt] + lists['makeup'], {
                    "default": '-',
                }),
                "光照类型": (['-'] + [rand_opt] + lists['light_type'], {
                    "default": '-',
                }),
                "光照方向": (['-'] + [rand_opt] + lists['light_direction'], {
                    "default": '-',
                }),
                "光照权重": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "style_1": (['-'] + [rand_opt] + lists['style'], {
                    "default": '-',
                }),
                "style_1_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "style_2": (['-'] + [rand_opt] + lists['style'], {
                    "default": '-',
                }),
                "style_2_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "照片写实增强": ("BOOLEAN", {"default": True}),
                "启用": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)

    FUNCTION = "pmsp"

    CATEGORY = CATEGORY

    def pmsp(
            self,
            text_in='',
            seed=0,
            模特姿势='-',
            服装='-',
            女士内衣='-',
            妆容='-',
            光照类型='-',
            光照方向='-',
            光照权重=1,
            style_1='-',
            style_1_weight=1,
            style_2='-',
            style_2_weight=1,
            照片写实增强=False,
            启用=True
    ):

        prompt = []

        if text_in != '':
            prompt.append(text_in)

        if 启用:

            if 妆容 == rand_opt:
                prompt.append('(' + random.choice(lists['makeup']) + ':1.05)')
            elif 妆容 != '-':
                prompt.append(f"({dicts['makeup'][妆容]}:1.05)")

            if 模特姿势 == rand_opt:
                prompt.append('(' + random.choice(lists['model_pose']) + ':1.25)')
            elif 模特姿势 != '-':
                prompt.append(f"({dicts['model_pose'][模特姿势]}:1.25)")

            if 服装 == rand_opt:
                prompt.append('(' + random.choice(lists['clothes']) + ':1.25)')
            elif 服装 != '-':
                prompt.append(f"({dicts['clothes'][服装]}:1.25)")

            if 女士内衣 == rand_opt:
                prompt.append('(' + random.choice(lists['female_lingerie']) + ':1.25)')
            elif 女士内衣 != '-':
                prompt.append(f"({dicts['female_lingerie'][女士内衣]}:1.25)")

            if 光照类型 == rand_opt:
                prompt.append(applyWeight(random.choice(lists['light_type']),光照权重))
            elif 光照类型 != '-':
                prompt.append(applyWeight(dicts['light_type'][光照类型],光照权重))

            if 光照方向 == rand_opt:
                prompt.append(applyWeight(random.choice(lists['light_direction']),光照权重))
            elif 光照方向 != '-':
                prompt.append(applyWeight(dicts['light_direction'][光照方向],光照权重))

            if style_1 == rand_opt:
                prompt.append(applyWeight(random.choice(lists['style']),style_1_weight))
            elif style_1 != '-':
                prompt.append(applyWeight(dicts['style'][style_1],style_1_weight))

            if style_2 == rand_opt:
                prompt.append(applyWeight(random.choice(lists['style']),style_2_weight))
            elif style_2 != '-':
                prompt.append(applyWeight(dicts['style'][style_2],style_2_weight))

            if 照片写实增强:
                prompt.append('(professional photo, balanced photo, balanced exposure:1.2)')

        if len(prompt) > 0:
            prompt = ', '.join(prompt)
            prompt = prompt.lower()
            return(prompt,)
        else:
            return('',)
