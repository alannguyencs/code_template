from pathlib import Path
import os
from alutils import alos

CWF = Path(__file__)

PROJECT_PATH = str(CWF.parent.parent) + '/'
DATA_PATH = f"{PROJECT_PATH}data/"
RESULT_PATH = alos.gen_dir(f"{PROJECT_PATH}result/")
CKPT_PATH = alos.gen_dir(f"{PROJECT_PATH}ckpt/")
LOG_PATH = alos.gen_dir(f"{PROJECT_PATH}log/")

