
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
                "natural_skin": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "bare_face": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "washed_face": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "dried_face": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "skin_details": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "skin_pores": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "dimples": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "wrinkles": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "freckles": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "moles": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "skin_imperfections": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "skin_acne": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "tanned_skin": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "eyes_details": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "iris_details": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "circular_iris": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "circular_pupil": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "active": ("BOOLEAN", {"default": True}),
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
            natural_skin=0,
            bare_face=0,
            washed_face=0,
            dried_face=0,
            skin_details=0,
            skin_pores=0,
            dimples=0,
            wrinkles=0,
            freckles=0,
            moles=0,
            skin_imperfections=0,
            skin_acne=0,
            tanned_skin=0,
            eyes_details=0,
            iris_details=0,
            circular_iris=0,
            circular_pupil=0,
            active=True
    ):

        prompt = []

        if text_in != '':
            prompt.append(text_in)

        if active:

            if natural_skin > 0:
                prompt.append(applyWeight('natural skin',natural_skin))

            if bare_face > 0:
                prompt.append(applyWeight('bare face',bare_face))

            if washed_face > 0:
                prompt.append(applyWeight('washed-face',washed_face))

            if dried_face > 0:
                prompt.append(applyWeight('dried-face',dried_face))

            if skin_details > 0:
                prompt.append(applyWeight('detailed skin',skin_details))

            if skin_pores > 0:
                prompt.append(applyWeight('skin pores',skin_pores))

            if skin_imperfections > 0:
                prompt.append(applyWeight('skin imperfections',skin_imperfections))

            if skin_acne > 0:
                prompt.append(applyWeight('acne, skin with acne',skin_acne))

            if wrinkles > 0:
                prompt.append(applyWeight('wrinkles',wrinkles))

            if tanned_skin > 0:
                prompt.append(applyWeight('tanned skin',tanned_skin))

            if dimples > 0:
                prompt.append(applyWeight('dimples',dimples))

            if freckles > 0:
                prompt.append(applyWeight('freckles',freckles))

            if moles > 0:
                prompt.append(applyWeight('moles',moles))

            if eyes_details > 0:
                prompt.append(applyWeight('eyes details',eyes_details))

            if iris_details > 0:
                prompt.append(applyWeight('iris details',iris_details))

            if circular_iris > 0:
                prompt.append(applyWeight('circular details',circular_iris))

            if circular_pupil > 0:
                prompt.append(applyWeight('circular pupil',circular_pupil))

        if len(prompt) > 0:
            prompt = ', '.join(prompt)
            prompt = prompt.lower()
            return(prompt,)
        else:
            return('',)
