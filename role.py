from enum import Enum, auto


class Role(Enum):
    # this ordering will be reflected at render time
    SOLO = 1
    COMP = 2
    HEAD = 3
    #TACIT = 4
