# PORTRAIT MASTER
# Created by AI Wiz Art (Stefano Flore)
# Version: 3.2.1
# https://stefanoflore.it
# https://ai-wiz.art

# modified by Tiger (https://github.com/DropFan)
# 汉化原版，并添加了一个保存 prompt 和 workflow 到图片 exif 信息中的 node

import os
import random
# from .legacy import PortraitMaster
print("=======================================================================")
print("[Portrait Master] Loading...")

from .common import *

from .PortraitMasterBaseCharacter import PortraitMasterBaseCharacter
from .PortraitMasterSkinDetails import PortraitMasterSkinDetails
from .PortraitMasterStylePose import PortraitMasterStylePose
from .PortraitMasterMakeup import PortraitMasterMakeup

from .PortraitMasterlegacy import PortraitMasterLegacy
from .ImageSaver import CImageSaveWithExtraMetadata as SaveImageWithMetadata

NODE_CLASS_MAPPINGS = {
    "PortraitMasterBaseCharacterCN": PortraitMasterBaseCharacter,
    "PortraitMasterSkinDetailsCN": PortraitMasterSkinDetails,
    "PortraitMasterStylePoseCN": PortraitMasterStylePose,
    "PortraitMasterMakeupCN": PortraitMasterMakeup,
    # "PortraitMasterCN": PortraitMaster,
    "PortraitMasterImageSaver":SaveImageWithMetadata,
    "PortraitMasterLegacyCN":PortraitMasterLegacy
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PortraitMasterBaseCharacterCN": "肖像大师：基础角色设定",
    "PortraitMasterSkinDetailsCN": "肖像大师：皮肤细节",
    "PortraitMasterStylePoseCN": "肖像大师：风格 & 姿势",
    "PortraitMasterMakeupCN": "肖像大师：化妆",
    "PortraitMasterImageSaver":"Save Image With Prompt/Metadata",
    "PortraitMasterLegacyCN": "Portrait Master 2.9.2 经典单节点版"
}

print("[Portrait Master] Loaded.")
print("=======================================================================")
