from _core.modules import VisualNovelModule
vn = VisualNovelModule()

def story():
    vn.label("menu_2")
    vn.choice({
        "mod_feature": "这个模组提供什么功能？",
        "mod_sdk":"如何创建我自己的剧情脚本？",
        "bugs":"已知的 bugs…（未翻译）",
        "menu_1":"< 上一页  ",
        "menu_3":"  下一页 >"
    })
    return vn.dialogueDict
