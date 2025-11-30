from _core.modules import VisualNovelModule
vn = VisualNovelModule()

from _characters import character_1

def story():
    vn.label("step_2_3_step_2")
    vn.say(character_1, "这是选项 3 专有的结局")
    vn.say(character_1, "选择选项 1 和 2 则不会看到这些")
    vn.finish()
    return vn.dialogueDict
