from _core.modules import VisualNovelModule
vn = VisualNovelModule()

from _characters import character_1

def story():
    vn.label("step_6")
    vn.say(character_1, "这是第六个片段")
    vn.say(character_1, "我们要学习一下代码风格")
    vn.say(character_1, "良好的代码风格可以显著增加代码可读性")
    vn.say(character_1, "这可以减少后续维护的成本")
    vn.say(character_1, "在我的项目结构中")
    vn.say(character_1, "全部使用多文件的剧情脚本")
    vn.say(character_1, "每个片段由一个标签开始，由跳转到另一片段或完成对话结束")
    vn.say(character_1, "主文件中只完成变量定义的引擎开始，按顺序导入各个片段的子文件")
    vn.say(character_1, "这样可以使剧情脚本便于维护，且适配多人协作编写")
    vn.finish()
    return vn.dialogueDict
