from pathlib import Path

import hobbybot_dagster.defs
from dagster_components import load_defs

defs = load_defs(defs_root=hobbybot_dagster.defs)
