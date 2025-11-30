from _core.modules import VisualNovelModule
vn = VisualNovelModule()

from characters.story_test import character_2

def story():
    vn.label("mod_feature")
    vn.say(character_2, "这是一个“可视化小说模组”，它使整合包作者能够在他们的游戏中添加与生物交谈的“剧情动画”。")
    vn.say(character_2, "所谓“剧情动画”，就是像你现在看到的界面这样。")
    vn.say(character_2, "这个模组里的所有东西都非常基础，它是为协作地图的故事线而制作的。")
    vn.say(character_2, "在这个剧情脚本中，你看到的就是它所能提供的一切。")
    vn.say(character_2, "对话、选项、循环和分支，图像（立绘、背景等）显示。")
    vn.say(character_2, "真的没什么别的好说的。")
    vn.say(character_2, "啊，它还支持 Minecraft 命令")
    vn.customCommand("give @p minecraft:diamond 1")
    vn.say(character_2, "欲了解更多技术细节，请随时查看开发者的 GitHub 页面。")
    vn.say(character_2, "https://github.com/Iteranya/MobTalkerRedux")
    vn.jumpTo("mod_sdk")
    return vn.dialogueDict
