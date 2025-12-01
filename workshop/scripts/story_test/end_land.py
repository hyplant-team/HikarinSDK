from _core.modules import VisualNovelModule
vn = VisualNovelModule()

from characters.story_test import character_2

def story():
    vn.label("end_land")
    vn.show(character_2, "happy.png")
    vn.say(character_2, "好啊！")
    vn.show_full("ui", "end_land.png")
    vn.modVar("background", True)
    vn.say(character_2, "回到末地！")
    vn.jumpTo("menu_1")
    return vn.dialogueDict
