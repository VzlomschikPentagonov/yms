from classes import *
from typing import TextIO
from os import mkdir, chdir

def create_project(name: str) -> list:
    chdir("../projects")
    for prj_dir in DIRS:
        mkdir(name + prj_dir)
    return []