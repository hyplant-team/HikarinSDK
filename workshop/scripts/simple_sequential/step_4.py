from _core.modules import VisualNovelModule
vn = VisualNovelModule()

from _characters import character_1

def story():
    vn.label("step_4")
    vn.say(character_1, "这是第四个片段")
    vn.say(character_1, "我们还可以执行 Minecraft 命令")
    vn.say(character_1, "当然，世界必而允许作弊，你也需要特定的权限")
    vn.say(character_1, "对了，如果你在使用单人游戏，为让命令正常工作，请开放到局域网。")
    vn.say(character_1, "因为单人游戏下，打开对话框会暂停游戏，导致一些命令无法正常工作")
    vn.say(character_1, "就像这样，点击屏幕飞天")
    vn.customCommand("execute as @p at @s run tp @s ~ ~10 ~")
    vn.say(character_1, "这可不是改变背景，而是真的进行了传送")
    vn.say(character_1, "再点击屏幕返回")
    vn.customCommand("execute as @p at @s run tp @s ~ ~-10 ~")
    vn.say(character_1, "现在我们回来了")
    vn.jumpTo("step_5")
    return vn.dialogueDict
