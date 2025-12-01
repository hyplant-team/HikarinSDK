from _core.modules import VisualNovelModule
vn = VisualNovelModule()

from _characters import character_1

def story():
    vn.label("step_3")
    vn.show(character_1, "happy.png")
    vn.say(character_1, "这是第三个片段")
    vn.say(character_1, "我们可以更改背景图像")
    vn.show_full("ui", "end_land.png")
    vn.say(character_1, "就像这样")
    vn.say(character_1, "新加入的图像会显示在最上层")
    vn.show(character_1, "happy.png")
    vn.say(character_1, "所以需要重新显示立绘")
    vn.say(character_1, "当然，也可以一次性显示背景和立绘")
    vn.remove("end_land.png")
    vn.say(character_1, "先移除背景")
    vn.show_full("ui", "end_land.png")
    vn.show(character_1, "happy.png")
    vn.say(character_1, "然后一次性加入")
    vn.remove("end_land.png")
    vn.remove(character_1)
    vn.say(character_1, "也支持一次性移除移除")
    vn.jumpTo("step_4")
    return vn.dialogueDict
