"""
Fixer that changes xrange(...) into range(...).
"""

from _typeshed import Incomplete, StrPath
from typing import ClassVar, Literal

from .. import fixer_base
from ..pytree import Node

class FixXrange(fixer_base.BaseFix):
    BM_compatible: ClassVar[Literal[True]]
    PATTERN: ClassVar[str]
    transformed_xranges: set[Incomplete] | None
    def start_tree(self, tree: Node, filename: StrPath) -> None: ...
    def finish_tree(self, tree: Node, filename: StrPath) -> None: ...
    def transform(self, node, results): ...
    def transform_xrange(self, node, results) -> None: ...
    def transform_range(self, node, results): ...
    P1: ClassVar[str]
    p1: ClassVar[Incomplete]
    P2: ClassVar[str]
    p2: ClassVar[Incomplete]
    def in_special_context(self, node): ...
