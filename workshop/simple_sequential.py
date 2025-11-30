from _core.compiler import compile
from _core.modules import VisualNovelModule
vn = VisualNovelModule()

storyName = "simple_sequential"

from scripts.simple_sequential import step_1
from scripts.simple_sequential import step_2
from scripts.simple_sequential import step_3
from scripts.simple_sequential import step_4
from scripts.simple_sequential import step_5
from scripts.simple_sequential import step_6

scripts = [
    step_1,
    step_2,
    step_3,
    step_4,
    step_5,
    step_6
]

vn.start()

def compileMultiStory():
    for script in scripts:
        script.story()
    return vn.dialogueDict

def main():
    compile(storyname=storyName, script=compileMultiStory())

if __name__ == "__main__":
    main()
