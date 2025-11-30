from dataclasses import dataclass, field
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from enum import Enum



# ==========================================
# ENUMS (For Script Logic / Constants)
# ==========================================

class Status(str, Enum):
    """
    Represents dynamic game states used in the FSM conditions.
    """
    IS_DAY = "<is_day>"
    IS_NIGHT = "<is_night>"
    HOSTILES = "<hostiles>"
    BELOW_SKY = "<below_sky>"
    NEAR_HOME = "<near_home>"
    P_UID = "<p_uid>"
    P_HEALTH = "<p_health>"
    GAMEMODE = "<gamemode>"
    DIMENSION = "<dimension>"
    X_COOR = "<x_coor>"
    Y_COOR = "<y_coor>"
    Z_COOR = "<z_coor>"
    HELD_ITEM = "<held_item>"

# ==========================================
# CHARACTER MODEL (Library)
# ==========================================
class Character:
    def __init__(self, id, name, description, thoughts=None, outfit="default", additional_tags={}):
        self.id = id
        self.name = name
        self.description = description
        self.thoughts = thoughts
        self.outfit = outfit
        self.dyn_outfit = f"<{id}_outfit>"
        self.tags: List[str] = ["id", "name", "description"]
        self.custom_data: Dict[str, Any] = {"id": id, "name": name, "description": description}
        if thoughts != None:
            self.tags += ["thoughts"]
            self.custom_data |= {"thoughts": thoughts}
        self.tags += ["outfit"]
        self.custom_data |= {"outfit": outfit}
        self.tags += additional_tags.keys()
        self.custom_data |= additional_tags

# ==========================================
# PROJECT MODEL (The Orchestrator)
# ==========================================

@dataclass
class ScriptGroup:
    """
    Represents ONE Output JSON (e.g., 'main_story.json').
    It is composed of MULTIPLE Python source files.
    """
    slug: str                  # The output filename (without .json)
    name: str                  # Display name in UI (e.g. "Main Story Chapter")
    source_files: List[str]    # The inputs: ["intro.py", "ch1.py", "ch2.py"]

@dataclass
class ProjectManifest:
    """
    The Project Configuration.
    Saved as 'projects/{slug}/manifest.json'.
    """
    slug: str
    name: str
    description: str = ""
    version: str = "0.0.1"
    authors: List[str] = field(default_factory=list)
    
    script_groups: List[ScriptGroup] = field(default_factory=lambda: [
        ScriptGroup(slug="behavior", name="Main Behavior", source_files=["main.py"])
    ])

# ==========================================
# ASSET MODEL (For API Responses)
# ==========================================

@dataclass
class AssetFile:
    """
    Used by the API to list files (images/audio) 
    found in the library or project assets.
    """
    filename: str
    path: str         # System path (for backend)
    url_path: str     # Web path (for frontend/Blockly to preview)
    size: int = 0