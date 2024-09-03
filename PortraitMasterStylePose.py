
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
                "model_pose": (['-'] + [rand_opt] + lists['model_pose'], {
                    "default": '-',
                }),
                "clothes": (['-'] + [rand_opt] + lists['clothes'], {
                    "default": '-',
                }),
                "female_lingerie": (['-'] + [rand_opt] + lists['female_lingerie'], {
                    "default": '-',
                }),
                "makeup": (['-'] + [rand_opt] + lists['makeup'], {
                    "default": '-',
                }),
                "light_type": (['-'] + [rand_opt] + lists['light_type'], {
                    "default": '-',
                }),
                "light_direction": (['-'] + [rand_opt] + lists['light_direction'], {
                    "default": '-',
                }),
                "light_weight": ("FLOAT", {
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
                "photorealism_improvement": ("BOOLEAN", {"default": True}),
                "active": ("BOOLEAN", {"default": True}),
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
            model_pose='-',
            clothes='-',
            female_lingerie='-',
            makeup='-',
            light_type='-',
            light_direction='-',
            light_weight=1,
            style_1='-',
            style_1_weight=1,
            style_2='-',
            style_2_weight=1,
            photorealism_improvement=False,
            active=True
    ):

        prompt = []

        if text_in != '':
            prompt.append(text_in)

        if active:

            if makeup == rand_opt:
                prompt.append('(' + random.choice(lists['makeup']) + ':1.05)')
            elif makeup != '-':
                prompt.append(f"({makeup}:1.05)")

            if model_pose == rand_opt:
                prompt.append('(' + random.choice(lists['model_pose']) + ':1.25)')
            elif model_pose != '-':
                prompt.append(f"({model_pose}:1.25)")

            if clothes == rand_opt:
                prompt.append('(' + random.choice(lists['clothes']) + ':1.25)')
            elif clothes != '-':
                prompt.append(f"({clothes}:1.25)")

            if female_lingerie == rand_opt:
                prompt.append('(' + random.choice(lists['female_lingerie']) + ':1.25)')
            elif female_lingerie != '-':
                prompt.append(f"({female_lingerie}:1.25)")

            if light_type == rand_opt:
                prompt.append(applyWeight(random.choice(lists['light_type']),light_weight))
            elif light_type != '-':
                prompt.append(applyWeight(light_type,light_weight))

            if light_direction == rand_opt:
                prompt.append(applyWeight(random.choice(lists['light_direction']),light_weight))
            elif light_direction != '-':
                prompt.append(applyWeight(light_direction,light_weight))

            if style_1 == rand_opt:
                prompt.append(applyWeight(random.choice(lists['style']),style_1_weight))
            elif style_1 != '-':
                prompt.append(applyWeight(style_1,style_1_weight))

            if style_2 == rand_opt:
                prompt.append(applyWeight(random.choice(lists['style']),style_2_weight))
            elif style_2 != '-':
                prompt.append(applyWeight(style_2,style_2_weight))

            if photorealism_improvement:
                prompt.append('(professional photo, balanced photo, balanced exposure:1.2)')

        if len(prompt) > 0:
            prompt = ', '.join(prompt)
            prompt = prompt.lower()
            return(prompt,)
        else:
            return('',)
