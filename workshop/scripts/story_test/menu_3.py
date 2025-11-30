from _core.modules import VisualNovelModule
vn = VisualNovelModule()

def story():
    vn.label("menu_3")
    vn.condSame("background", True, [
        vn.choice({
            "mod_compatibility": "这个模组与 Insert Mod Here 兼容吗",
            "community":"从哪里获得社区剧情脚本？",
            "background": "我们怎么在末地？",
            "menu_2":"< 上一页  ",
            "end": "再见"
        },True)
    ])
    vn.choice({
        "mod_compatibility": "这个模组与 Insert Mod Here 兼容吗",
        "community":"从哪里获得社区剧情脚本？",
        "end_land": "我们回到末地吧。",
        "menu_2":"< 上一页  ",
        "end": "再见"
    })
    return vn.dialogueDict
