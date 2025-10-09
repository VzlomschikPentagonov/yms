from classes import *
from os import mkdir, chdir

def create_project(name: str,
                   tracks: int) -> None:
    chdir("../projects")
    for prj_dir in DIRS:
        mkdir(name + prj_dir)
    chdir("./%s/main" % name)
    for track in range(tracks):
        open("track_%d.trk" % track, "w+b")
    open("../patterns/pattern.pat", "w+b")
