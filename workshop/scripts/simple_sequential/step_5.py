from _core.modules import VisualNovelModule
vn = VisualNovelModule()

from _characters import character_1

def story():
    vn.label("step_5")
    vn.say(character_1, "这是第五个片段")
    vn.say(character_1, "现在我们加上角色语音")
    vn.say(character_1, "记得适当调低音量")
    vn.say(character_1, "自定义音频可以通过资源包加载")
    vn.say(character_1, "就像这样，点击屏幕播放语音")
    # vn.customCommand("execute as @p at @s run playsound mobtalkerredux:voice.simple_sequential.example1 voice @s")
    vn.voice_effect("simple_sequential.example1")
    vn.say(character_1, "这样就可以实现角色语音了")
    vn.voice_effect("")
    # vn.customCommand("execute as @p at @s run stopsound @s voice mobtalkerredux:voice.simple_sequential.example1")
    vn.say(character_1, "（该剧情脚本中之后的对话没有语音）")
    vn.jumpTo("step_6")
    return vn.dialogueDict
