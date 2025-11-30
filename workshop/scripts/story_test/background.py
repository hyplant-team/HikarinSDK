from _core.modules import VisualNovelModule
vn = VisualNovelModule()

from characters.story_test import character_2

def story():
    vn.label("background")
    vn.say(character_2, "哦，别担心，我们并非真的在末地。")
    vn.say(character_2, "只是展示模组更换背景的功能！")
    vn.remove("asset", "end_land")
    vn.modVar("background", False)
    vn.say(character_2, "现在我们回来了。")
    vn.jumpTo("menu_1")
    return vn.dialogueDict
