from _core.modules import VisualNovelModule
vn = VisualNovelModule()

from _characters import character_1

def story():
    vn.label("step_2_1_step_1")
    vn.say(character_1, "你选择了选项 1")
    vn.say(character_1, "这里是选项 1 专有的剧情脚本")
    vn.say(character_1, "选择选项 2 和 3 则不会看到这些")
    vn.jumpTo("step_3")
    return vn.dialogueDict
