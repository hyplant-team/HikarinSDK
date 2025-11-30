from _core.modules import VisualNovelModule
vn = VisualNovelModule()

from _characters import character_1

def story():
    vn.label("step_1")
    vn.say(character_1, "这是简单的分支结构示例")
    vn.say(character_1, "在这个示例中")
    vn.say(character_1, "用户将做出选择")
    vn.say(character_1, "不同的选择会触发不同的分支")
    vn.say(character_1, "选项 1 和 2 过程不同，结局相同；选项 3 结局不同")
    vn.jumpTo("step_2")
    return vn.dialogueDict
