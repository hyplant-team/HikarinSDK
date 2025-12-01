from _core.modules import VisualNovelModule
vn = VisualNovelModule()

from characters.story_test import character_2

def story():
    vn.label("dev_history")
    vn.say(character_2, "嗯…  关于这个…")
    vn.say(character_2, "请不要到抱怨先前开发者的放弃。")
    vn.say(character_2, "Mob Talker 模组功能简单，但开发十分复杂。")
    vn.show_left(character_2, "normal.png")
    vn.show_custom("ui","old-dsl.png",16,9,10,6,6,1)
    vn.say(character_2, "开发者必须创建一种 DSL（领域特定语言）。")
    vn.say(character_2, "例如先前的 Mob Talker 模组剧情脚本。")
    vn.say(character_2, "想象一下，你必须把这些脚本转换成模组可加载的型式。")
    vn.say(character_2, "你几乎是在创建一个全新的编程语言和游戏引擎。")
    vn.show(character_2, "tired.png")
    vn.say(character_2, "而且你还得让编程语言与 Java 兼容，并在 Minecraft 内运行游戏引擎。")
    vn.choice({
        "lua": "为什么不使用 Lua？",
        "cool": "这么高级，开发者是怎么做到的？"
    })
    return vn.dialogueDict
