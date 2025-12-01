from _core.modules import VisualNovelModule
vn = VisualNovelModule()

from characters.story_test import character_2

def story():
    vn.label("bugs")
    vn.say(character_2, "Since this is a framework, some bugs can be not from this mod itself...")
    vn.say(character_2, "Soo, let me list off some known bugs as of right now, ahem...")
    vn.say(character_2, "1. We don't support multiple character sprite yet")
    vn.say(character_2, "The dev is working on that currently, most likely this bug is already fixed")
    vn.say(character_2, "This is the mod's fault, not the SDK's fault, so, report the issue correctly")
    vn.say(character_2, "2. The images are not displayed correctly")
    vn.say(character_2, "As of right now, the size of the image are hardcoded to 530 by 900 pixels")
    vn.say(character_2, "3. There is no way to programatically remove a sprite  that's already appeared, only replace")
    vn.say(character_2, "All of these sprite and image showing issue is being reworked as of writing this")
    vn.say(character_2, "The dev is looking to solve problem 1 and 2 at the same time right now")
    vn.show(character_2, "tired.png")
    vn.say(character_2, "See minecraft just updated how they handle Screens and it kinda throw them off...")
    vn.show(character_2, "normal.png")
    vn.say(character_2, "So yeah, send some love his way alright???")
    vn.jumpTo("menu_1")
    return vn.dialogueDict
