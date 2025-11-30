from _core.modules import VisualNovelModule
vn = VisualNovelModule()

from characters.story_test import character_2

def story():
    vn.label("menu_1")
    vn.show(character_2, "normal")
    vn.choice({
        "about_you": "关于你…",
        "dev_history": "为何重制要花这么久？",
        "dev_excuses":"默认剧情脚本在哪里？",
        "menu_2":"  下一页 >"
    })
    return vn.dialogueDict
