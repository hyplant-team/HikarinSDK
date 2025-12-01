from _core.modules import VisualNovelModule
vn = VisualNovelModule()

from characters.story_test import character_2

def story():
    vn.label("avoid")
    vn.show(character_2, "tired.png")
    vn.say(character_2, "事实上，开发者考虑到这个模组会出现 NSWF 内容。")
    vn.say(character_2, "开发者也无意制作适合大众观看的可分版本的剧情脚本。")
    vn.say(character_2, "所以，开发者因为法律、伦理、道德问题，不打算制作官方剧情脚本。")
    vn.say(character_2, "让我们换个话题再聊吧。")
    vn.jumpTo("menu_1")
    return vn.dialogueDict
