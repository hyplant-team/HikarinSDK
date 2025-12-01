from _core.modules import VisualNovelModule
vn = VisualNovelModule()

from characters.story_test import character_2

def story():
    vn.label("end")
    vn.show(character_2, "happy.png")
    vn.say(character_2, "很高兴为您服务，再见！")
    vn.finish()
    return vn.dialogueDict
