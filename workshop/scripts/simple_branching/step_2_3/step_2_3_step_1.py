from _core.modules import VisualNovelModule
vn = VisualNovelModule()

from _characters import character_1

def story():
    vn.label("step_2_3_step_1")
    vn.say(character_1, "你选择了选项 3")
    vn.say(character_1, "这里是选项 3 专有的剧情脚本")
    vn.say(character_1, "选择选项 1 和 2 则不会看到这些")
    vn.jumpTo("step_2_3_step_2")
    return vn.dialogueDict
