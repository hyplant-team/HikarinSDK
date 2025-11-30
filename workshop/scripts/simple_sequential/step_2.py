from _core.modules import VisualNovelModule
vn = VisualNovelModule()

from _characters import character_1

def story():
    vn.label("step_2")
    vn.say(character_1, "这是第二个片段")
    vn.say(character_1, "接下来我们尝试显示一个立绘")
    vn.show(character_1, "happy")
    vn.say(character_1, "就像这样")
    vn.show(character_1, "sad")
    vn.say(character_1, "也可以改变表情")
    vn.show_left(character_1, "normal")
    vn.say(character_1, "放到左边")
    vn.show_right(character_1, "normal")
    vn.say(character_1, "放到右边")
    vn.remove(character_1, "normal")
    vn.say(character_1, "移除立绘")
    vn.jumpTo("step_3")
    return vn.dialogueDict
