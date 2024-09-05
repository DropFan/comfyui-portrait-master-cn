
import random

from .common import *

# Portrait Master Skin Details

class PortraitMasterSkinDetails:

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
                "干燥脸": ("FLOAT", {
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
                "皮肤痤疮_痘痘": ("FLOAT", {
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
                "启用": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)

    FUNCTION = "pmsd"

    CATEGORY = CATEGORY

    def pmsd(
            self,
            text_in='',
            seed=0,
            自然皮肤=0,
            素颜=0,
            洗脸程度=0,
            干燥脸=0,
            皮肤细节=0,
            皮肤毛孔=0,
            酒窝=0,
            皱纹=0,
            雀斑=0,
            痣=0,
            皮肤瑕疵=0,
            皮肤痤疮_痘痘=0,
            晒黑_小麦色皮肤=0,
            眼睛细节=0,
            虹膜细节=0,
            环形虹膜=0,
            圆形瞳孔=0,
            启用=True
    ):

        prompt = []

        if text_in != '':
            prompt.append(text_in)

        if 启用:

            if 自然皮肤 > 0:
                prompt.append(applyWeight('natural skin',自然皮肤))

            if 素颜 > 0:
                prompt.append(applyWeight('bare face',素颜))

            if 洗脸程度 > 0:
                prompt.append(applyWeight('washed-face',洗脸程度))

            if 干燥脸 > 0:
                prompt.append(applyWeight('dried-face',干燥脸))

            if 皮肤细节 > 0:
                prompt.append(applyWeight('detailed skin',皮肤细节))

            if 皮肤毛孔 > 0:
                prompt.append(applyWeight('skin pores',皮肤毛孔))

            if 皮肤瑕疵 > 0:
                prompt.append(applyWeight('skin imperfections',皮肤瑕疵))

            if 皮肤痤疮_痘痘 > 0:
                prompt.append(applyWeight('acne, skin with acne',皮肤痤疮_痘痘))

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

        if len(prompt) > 0:
            prompt = ', '.join(prompt)
            prompt = prompt.lower()
            return(prompt,)
        else:
            return('',)
