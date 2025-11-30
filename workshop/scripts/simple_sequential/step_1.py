from _core.modules import VisualNovelModule
vn = VisualNovelModule()

from _characters import character_1
from characters.simple_sequential import simple_sequential_player

def story():
    vn.label("step_1")
    vn.say(character_1, "这是简单的顺序结构示例")
    vn.say(character_1, "现在是第一个片段")
    vn.say(character_1, "为你展示最简单的对话")
    vn.say(character_1, "现在是 NPC 对你说话")
    vn.say(character_1, "当然，可以改变说话者")
    vn.say(character_1, "只需创建对应的角色")
    vn.say(simple_sequential_player, "例如，这是你对 NPC 说的话")
    vn.jumpTo("step_2")
    return vn.dialogueDict
