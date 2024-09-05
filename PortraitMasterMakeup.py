
# global vars
import random

from .common import *

class PortraitMasterMakeup:

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
                "化妆风格": (['-'] + [rand_opt] + lists['makeup'], {
                    "default": '-',
                }),
                "化妆颜色": (['-'] + [rand_opt] + lists['makeup_color'], {
                    "default": '-',
                }),
                "眼影": ("BOOLEAN", {"default": False}),
                "眼线": ("BOOLEAN", {"default": False}),
                "睫毛膏": ("BOOLEAN", {"default": False}),
                "腮红": ("BOOLEAN", {"default": False}),
                "口红": ("BOOLEAN", {"default": False}),
                "唇彩": ("BOOLEAN", {"default": False}),
                "启用": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)

    FUNCTION = "pmmk"

    CATEGORY = CATEGORY

    def pmmk(
            self,
            text_in='',
            seed=0,
            化妆风格='-',
            化妆颜色='-',
            眼影=False,
            眼线=False,
            睫毛膏=False,
            腮红=False,
            口红=False,
            唇彩=False,
            启用=True,
    ):

        prompt = []

        if text_in != '':
            prompt.append(text_in)

        if 启用:
            if 化妆风格 == rand_opt:
                化妆风格 = random.choice(lists['makeup'])
            if 化妆风格 != '-':
                prompt.append(f"({dicts['makeup'][化妆风格]}:1.05)")

            if 化妆颜色 == rand_opt:
                化妆颜色 = random.choice(lists['makeup_color'])
            if 化妆颜色 != '-':
                prompt.append(f"({dicts['makeup_color'][化妆颜色]} make-up color:1.05)")

            if 眼影: prompt.append("(eyeshadow make-up:1.05)")
            if 眼线: prompt.append("(eyeliner make-up:1.05)")
            if 睫毛膏: prompt.append("(mascara make-up:1.05)")
            if 腮红: prompt.append("(blush make-up:1.05)")
            if 口红: prompt.append("(lipstick make-up:1.05)")
            if 唇彩: prompt.append("(lip gloss make-up:1.05)")

        if len(prompt) > 0:
            prompt = ', '.join(prompt)
            prompt = prompt.lower()
            return(prompt,)
        else:
            return('',)
