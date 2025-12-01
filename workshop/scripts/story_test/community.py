from _core.modules import VisualNovelModule
vn = VisualNovelModule()

from characters.story_test import character_2

def story():
    vn.label("community")
    vn.say(character_2, "模组的下载页面上有一个 Discord 链接。")
    vn.show(character_2, "happy.png")
    vn.say(character_2, "随意创作你自己的剧本吧！打造你自己的角色，主世界及更远的地方都是你的探索天地。")
    vn.say(character_2, "开发者的愿望是重现，复兴在 Minecraft 中加入2D CG图像的美感，并让这个模组永生！")
    vn.show(character_2, "shy.png")
    vn.say(character_2, "并让我们相遇。")
    vn.show(character_2, "normal.png")
    vn.say(character_2, "但说到底，开发者只是提供工具而已。")
    vn.say(character_2, "所以请不要反馈漏洞说缺乏互动。")
    vn.say(character_2, "还有什么其他想问的吗？")
    vn.jumpTo("menu_1")
    return vn.dialogueDict
