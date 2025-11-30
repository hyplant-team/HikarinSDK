from _core.modules import VisualNovelModule
vn = VisualNovelModule()

from characters.story_test import character_2

def story():
    vn.label("mod_sdk")
    vn.say(character_2, "制作剧情脚本很简单。")
    vn.say(character_2, "你只需要 Mob Talker SDK。")
    vn.say(character_2, "https://github.com/Iteranya/MobTalkerSDK")
    vn.say(character_2, "也许你无法直接点击链接…")
    vn.say(character_2, "但肯定的是，使用 SDK，你可以把可读的 Python 脚本转换为 JSON。")
    vn.say(character_2, "有关如何使用 SDK 的更多信息，请参阅 GitHub 页面。")
    vn.say(character_2, "还有问题吗？")
    vn.jumpTo("menu_1")
    return vn.dialogueDict
