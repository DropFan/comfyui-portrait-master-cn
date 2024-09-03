
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
                "makeup_style": (['-'] + [rand_opt] + lists['makeup'], {
                    "default": '-',
                }),
                "makeup_color": (['-'] + [rand_opt] + lists['makeup_color'], {
                    "default": '-',
                }),
                "eyeshadow": ("BOOLEAN", {"default": False}),
                "eyeliner": ("BOOLEAN", {"default": False}),
                "mascara": ("BOOLEAN", {"default": False}),
                "blush": ("BOOLEAN", {"default": False}),
                "lipstick": ("BOOLEAN", {"default": False}),
                "lip_gloss": ("BOOLEAN", {"default": False}),
                "active": ("BOOLEAN", {"default": True}),
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
            makeup_style='-',
            makeup_color='-',
            eyeshadow=False,
            eyeliner=False,
            mascara=False,
            blush=False,
            lipstick=False,
            lip_gloss=False,
            active=True,
    ):

        prompt = []

        if text_in != '':
            prompt.append(text_in)

        if active:

            if makeup_style == rand_opt:
                prompt.append('(' + random.choice(lists['makeup']) + ':1.05)')
            elif makeup_style != '-':
                prompt.append(f"({makeup_style}:1.05)")

            if makeup_color == rand_opt:
                prompt.append('(' + random.choice(lists['makeup_color']) + ' make-up color:1.05)')
            elif makeup_color != '-':
                prompt.append(f"({makeup_color} make-up color:1.05)")

            if eyeshadow: prompt.append("(eyeshadow make-up:1.05)")
            if eyeliner: prompt.append("(eyeliner make-up:1.05)")
            if mascara: prompt.append("(mascara make-up:1.05)")
            if blush: prompt.append("(blush make-up:1.05)")
            if lipstick: prompt.append("(lipstick make-up:1.05)")
            if lip_gloss: prompt.append("(lip gloss make-up:1.05)")

        if len(prompt) > 0:
            prompt = ', '.join(prompt)
            prompt = prompt.lower()
            return(prompt,)
        else:
            return('',)
