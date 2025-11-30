from _core.modules import VisualNovelModule
vn = VisualNovelModule()

from _characters import character_1
from characters.story_test import character_2

def story():
    vn.label("start")
    vn.show(character_1, "happy")
    vn.say(character_1, "你好，好久没见面了！哈哈！")
    vn.show(character_1, "normal")
    vn.say(character_1, "反正…有段时间了。")
    vn.say(character_1, "之前的最后一个版本是多少？")
    vn.say(character_1, "1.8？现在的版本是多少？")
    vn.show(character_1, "scared")
    vn.say(character_1, "1.21！我们分别了…这么久！")
    vn.show(character_1, "angry")
    vn.say(character_1, "我无法相信这个模组被放弃了这么久！！！")
    vn.say(character_1, "我说，重制这个模组难度会有多大呢？")
    vn.show_right(character_2, "normal")
    vn.say(character_2, "这并不简单，测试 NPC 1号。重制这个模组用到了 DSL。")
    vn.show_left(character_1, "scared")
    vn.say(character_1, "我的天啊，测试 NPC 2号！你是从哪里来的？")
    vn.show_right(character_2, "normal")
    vn.say(character_2, "我之前一直在协助开发者完成这个模组。")
    vn.show_left(character_1, "angry")
    vn.say(character_1, "我只是在夸张而已…不过，你为什么要来这里？")
    vn.say(character_2, "我来解释这个模组是如何使用的。如果你能阅读这些，说明你已经正确安装了模组，并成功加载了测试剧情。")
    vn.show_left(character_1, "normal")
    vn.say(character_1, "好，那你们开始吧。")
    vn.remove(character_2)
    vn.show(character_2, "normal")
    vn.say(character_2, "你好，很高兴见到你！")
    vn.say(character_2, "我们找个更好的地方聊吧。")
    vn.show_full("asset", "end_land")
    vn.modVar("background", True)
    vn.say(character_2, "现在你想知道什么呢？")
    vn.jumpTo("menu_1")
    return vn.dialogueDict
