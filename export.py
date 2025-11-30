# =======================================

# This is where you define the resource pack name, description, and  trigger words
# No need to scroll down
# Just press play, top right corner of the screen
# And it will create the resource pack zip for you

# Have fun then!

ASSETS_DIR = "mediafile"
OUTPUT_NAME = "HikarinSdkDemo"

# =======================================

# Oh you want to know how it works???
# ...
# Yeah, good luck with that


import os
import shutil

def create_resource_pack():
    # Create the zip file
    if os.path.exists(OUTPUT_NAME+".zip"):
        os.remove(OUTPUT_NAME+".zip")
    shutil.make_archive(OUTPUT_NAME, 'zip', ASSETS_DIR)
    return 0

def main():
    create_resource_pack()

if __name__ == "__main__":
    main()
