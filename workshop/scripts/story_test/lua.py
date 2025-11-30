from _core.modules import VisualNovelModule
vn = VisualNovelModule()

from characters.story_test import character_2

def story():
    vn.label("lua")
    vn.show(character_2, "normal")
    vn.say(character_2, "好问题。")
    vn.say(character_2, "Lua 是一个看似不错的选择。它轻量化，许多模组都使用它。")
    vn.say(character_2, "那为什么不使用 Lua 定义一些控制屏幕的方法？")
    vn.say(character_2, "主要问题是，Lua 是一种解释型语言。")
    vn.say(character_2, "而Java，是一种编译型语言。")
    vn.show(character_2, "tired")
    vn.say(character_2, "这将导致编译后，Java会尝试一次性运行整个脚本！")
    vn.say(character_2, "让 Java 逐行解释 Lua 是非常困难的。")
    vn.say(character_2, "这很可能就是先前开发者放弃这个项目的原因。")
    vn.show(character_2, "normal")
    vn.say(character_2, "Java 开发者都知道，让 Lua 或任何解释型语言与 Java 协作作有多难。")
    vn.say(character_2, "大多数开发者在意识到他们需要为此创建一门新的编程语言时，都不知所措。")
    vn.say(character_2, "而且，要真正重现这个模组，你还必须做出社区玩家会使用的东西。")
    vn.say(character_2, "有一种方法就是创作一种人类可读的 DSL，且可被 Java 使用。")
    vn.say(character_2, "因此，这个新的开发者创造了一种基于 Python 的 DSL。")
    vn.jumpTo("cool")
    return vn.dialogueDict
