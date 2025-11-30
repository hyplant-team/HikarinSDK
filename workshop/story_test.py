from _core.compiler import compile
from _core.modules import VisualNovelModule
vn = VisualNovelModule()

storyName = "story_test"

from scripts.story_test import start
from scripts.story_test import menu_1
from scripts.story_test import menu_2
from scripts.story_test import menu_3
from scripts.story_test import end_land
from scripts.story_test import background
from scripts.story_test import bugs
from scripts.story_test import about_you
from scripts.story_test import dev_history
from scripts.story_test import lua
from scripts.story_test import cool
from scripts.story_test import dev_excuses
from scripts.story_test import avoid
from scripts.story_test import mod_feature
from scripts.story_test import mod_sdk
from scripts.story_test import mod_compatibility
from scripts.story_test import community
from scripts.story_test import end

scripts = [
    start,
    menu_1,
    menu_2,
    menu_3,
    end_land,
    background,
    bugs,
    about_you,
    dev_history,
    lua,
    cool,
    dev_excuses,
    avoid,
    mod_feature,
    mod_sdk,
    mod_compatibility,
    community,
    end
]

vn.setVar("background", False)
vn.start()

def compileMultiStory():
    for script in scripts:
        script.story()
    return vn.dialogueDict

def main():
    compile(storyname=storyName, script=compileMultiStory())

if __name__ == "__main__":
    main()
