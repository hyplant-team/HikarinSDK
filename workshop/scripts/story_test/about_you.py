from _core.modules import VisualNovelModule
vn = VisualNovelModule()

from characters.story_test import character_2

def story():
    vn.label("about_you")
    vn.show(character_2, "shy")
    vn.say(character_2, "关于我…  嗯…")
    vn.say(character_2, "我之前一直在协助开发者完成这个模组。")
    vn.say(character_2, "我想因此你先前没有见过我。")
    vn.show(character_2, "normal")
    vn.say(character_2, "如果你看到了我，说明模组已经趋于完善。")
    vn.say(character_2, "这是新开发者对旧模组的继承。")
    vn.say(character_2, "你还有什么想知道的吗？")
    vn.jumpTo("menu_1")
    return vn.dialogueDict
