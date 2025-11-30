from _core.modules import VisualNovelModule
vn = VisualNovelModule()

from characters.story_test import character_2

def story():
    vn.label("cool")
    vn.remove("asset", "old-dsl")
    vn.show_left(character_2, "normal")
    vn.show_custom("asset", "python-dsl",16,9,10,6,6,1)
    vn.say(character_2, "这是 DSL 使用 Python 编写。")
    vn.say(character_2, "开发者放弃了 Lua，从而完全绕过了解释型语言与 Java 协作问题。")
    vn.say(character_2, "开发者创建了一个 Python SDK 框架，可以将 python-dsl 转换为可在 Java 中使用的脚本。")
    vn.say(character_2, "从 Python 转化为 Json FSM（有限状态机）")
    vn.say(character_2, "这个 Json FSM 可以轻松被 Java 读取并解释。")
    vn.say(character_2, "开发者唯一要做的，只是创建一个简单的 Java 类，可以读取 Json FSM。")
    vn.say(character_2, "整合包作者和玩家只需将这个 Json FSM 放入资源包中。")
    vn.say(character_2, "这便是开发者实现 DSL 的方法。")
    vn.remove("asset", "python-dsl")
    vn.show(character_2, "normal")
    vn.say(character_2, "你还有什么要问的吗？")
    vn.jumpTo("menu_1")
    return vn.dialogueDict
