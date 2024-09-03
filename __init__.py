# PORTRAIT MASTER
# Created by AI Wiz Art (Stefano Flore)
# Version: 3.2.1
# https://stefanoflore.it
# https://ai-wiz.art

# modified by Tiger (https://github.com/DropFan)

import os
import random
# from .legacy import PortraitMaster
print("=======================================================================")
print("[Portrait Master] Loading...")

from .common import *
# from . import PortraitMasterBaseCharacter, PortraitMasterSkinDetails, PortraitMasterStylePose, PortraitMasterMakeup,PortraitMasterLegacy
from .legacy import PortraitMasterLegacy
from .ImageSaver import CImageSaveWithExtraMetadata as SaveImageWithMetadata

NODE_CLASS_MAPPINGS = {
    # "PortraitMasterBaseCharacterCN": PortraitMasterBaseCharacter,
    # "PortraitMasterSkinDetailsCN": PortraitMasterSkinDetails,
    # "PortraitMasterStylePoseCN": PortraitMasterStylePose,
    # "PortraitMasterMakeupCN": PortraitMasterMakeup,
    # "PortraitMasterCN": PortraitMaster,
    "PortraitMasterImageSaver":SaveImageWithMetadata,
    "PortraitMasterLegacyCN":PortraitMasterLegacy
}

NODE_DISPLAY_NAME_MAPPINGS = {
    # "PortraitMasterBaseCharacterCN": "肖像大师: 基础角色",
    # "PortraitMasterSkinDetailsCN": "肖像大师: 皮肤细节",
    # "PortraitMasterStylePoseCN": "肖像大师: 风格 & Pose",
    # "PortraitMasterMakeupCN": "肖像大师: 化妆",
    # "PortraitMasterLegacyCN": "肖像大师 2.9.2 (经典)",
    "PortraitMasterImageSaver":"SaveImageWithMetadata",
    "PortraitMasterLegacyCN": "Portrait Master 经典汉化"
}

print("[Portrait Master] Loaded.")
print("=======================================================================")
