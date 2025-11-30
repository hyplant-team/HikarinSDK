from _core.compiler import compile
from _core.modules import VisualNovelModule
vn = VisualNovelModule()

storyName = "simple_branching"

from scripts.simple_branching import step_1
from scripts.simple_branching import step_2
from scripts.simple_branching.step_2_1 import step_2_1_step_1
from scripts.simple_branching.step_2_2 import step_2_2_step_1
from scripts.simple_branching.step_2_3 import step_2_3_step_1
from scripts.simple_branching.step_2_3 import step_2_3_step_2
from scripts.simple_branching import step_3

scripts = [
    step_1,
    step_2,
    step_2_1_step_1,
    step_2_2_step_1,
    step_2_3_step_1,
    step_2_3_step_2,
    step_3
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
