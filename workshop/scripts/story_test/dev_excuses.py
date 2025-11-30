from _core.modules import VisualNovelModule
vn = VisualNovelModule()

from characters.story_test import character_2

def story():
    vn.label("dev_excuses")
    vn.say(character_2, "我有义务告诉你…")
    vn.say(character_2, "那个…")
    vn.say(character_2, "这个模组的开发者 Iteranya，不为任何剧情脚本的内容负责。")
    vn.say(character_2, "如果有人声称这是“默认”或“官方”脚本…")
    vn.say(character_2, "他们是乱说。")
    vn.say(character_2, "关于“默认”剧情脚本…")
    vn.say(character_2, "开发者正在处理此事，但他们很可能不会声称这是“官方”的，而会使用化名。")
    vn.say(character_2, "以上是关于默认剧情脚本的全部。")
    vn.say(character_2, "其他的话…")
    vn.choice({
        "avoid": "你为什么听起来提防心那么强？",
        "menu_1":"知道了，谢谢。"
    })
    return vn.dialogueDict
