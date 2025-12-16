# This sample tests that a complete union of enum literal members
# is treated as equivalent to the enum type itself, per the typing spec.

from enum import Enum, Flag
from typing import Literal


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


def expansion(x: Color) -> Literal[Color.RED, Color.GREEN, Color.BLUE]:
    return x

def expansion_extra(x: Color) -> Literal[Color.RED, Color.GREEN, Color.BLUE] | str:
    return x

def contraction(x: Literal[Color.RED, Color.GREEN, Color.BLUE]) -> Color:
    return x

def incomplete_union(x: Color) -> Literal[Color.RED, Color.GREEN]:
    # This should generate an error because BLUE is missing
    return x

def literal_to_union(x: Literal[Color.RED]) -> Literal[Color.RED, Color.GREEN, Color.BLUE]:
    return x

class SingleMember(Enum):
    ONLY = 1

def single_member_expansion(x: SingleMember) -> Literal[SingleMember.ONLY]:
    return x

def single_member_contraction(x: Literal[SingleMember.ONLY]) -> SingleMember:
    return x 

class Permission(Flag):
    READ = 1
    WRITE = 2
    EXECUTE = 4

def flag_no_expansion(x: Permission) -> Literal[Permission.READ, Permission.WRITE, Permission.EXECUTE]:
    # This should generate an error because Flag enums don't support literal expansion
    return x