from _core.modules import VisualNovelModule
vn = VisualNovelModule()

from characters.story_test import character_2

def story():
    vn.label("mod_compatibility")
    vn.say(character_2, "这个模组重视兼容性且易于维护。")
    vn.say(character_2, "由于依赖 Java 互操作性和关注点分离，唯一“修改”的部分是 GUI。")
    vn.say(character_2, "读取 Json FSM 的游戏引擎是用纯 Java 编写的。")
    vn.say(character_2, "你甚至不需要担心跨版本时脚本的兼容性。")
    vn.show(character_2, "happy")
    vn.say(character_2, "我个人很喜欢这种方法，Mob Talker 模组可能因此再次成为经典！")
    vn.say(character_2, "CMM 团队也仍然活跃。")
    vn.say(character_2, "所以这是有可能的。")
    vn.show(character_2, "normal")
    vn.say(character_2, "但是，如果要使用这个框架，需要自己添加剧情脚本。")
    vn.say(character_2, "你还有其他问题吗？")
    vn.jumpTo("menu_1")
    return vn.dialogueDict
