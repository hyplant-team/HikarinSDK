from _core.modules import VisualNovelModule
vn = VisualNovelModule()

from _characters import character_1

def story():
    vn.label("step_2")
    vn.say(character_1, "请做出选择")
    vn.choice({
        "step_2_1_step_1": "选项 1",
        "step_2_2_step_1": "选项 2",
        "step_2_3_step_1": "选项 3"
    })
    return vn.dialogueDict
