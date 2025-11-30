from _core.modules import VisualNovelModule
vn = VisualNovelModule()

from _characters import character_1

def story():
    vn.label("step_3")
    vn.say(character_1, "这是选项 1 和 2 共有的片段")
    vn.say(character_1, "选择选项 3 则不会看到这些")
    vn.finish()
    return vn.dialogueDict
