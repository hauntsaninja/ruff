# See https://peps.python.org/pep-0484/#positional-only-arguments
# for the full details on which arguments using the older syntax should/shouldn't
# be considered positional-only arguments by type checkers.
from typing import Self

def bad(__x: int) -> None: ...  # PYI063
def also_bad(__x: int, __y: str) -> None: ...  # PYI063
def still_bad(__x_: int) -> None: ...  # PYI063

def no_args() -> None: ...
def okay(__x__: int) -> None: ...
# The first argument isn't positional-only, so logically the second can't be either:
def also_okay(x: int, __y: str) -> None: ...
def fine(x: bytes, /) -> None: ...
def no_idea_why_youd_do_this(__x: int, /, __y: str) -> None: ...
def cool(_x__: int) -> None: ...
def also_cool(x__: int) -> None: ...
def unclear_from_pep_484_if_this_is_positional_or_not(__: str) -> None: ...
def _(_: int) -> None: ...

class Foo:
    def bad(__self) -> None: ...  # PYI063
    @staticmethod
    def bad2(__self) -> None: ...  # PYI063
    def bad3(__self, __x: int) -> None: ...  # PYI063
    def still_bad(self, __x_: int) -> None: ...  # PYI063  # TODO: doesn't get raised here
    @staticmethod
    def this_is_bad_too(__x: int) -> None: ...  # PYI063
    @classmethod
    def not_good(cls, __foo: int) -> None: ...  # PYI063

    # The first non-self argument isn't positional-only, so logically the second can't be either:
    def okay1(self, x: int, __y: int) -> None: ...
    # Same here:
    @staticmethod
    def okay2(x: int, __y_: int) -> None: ...
    @staticmethod
    def no_args() -> int: ...
    def okay3(__self__, __x__: int, __y: str) -> None: ...
    def okay4(self, /) -> None: ...
    def okay5(self, x: int, /) -> None: ...
    def okay6(__self, /) -> None: ...
    def cool(_self__: int) -> None: ...
    def also_cool(self__: int) -> None: ...
    def unclear_from_pep_484_if_this_is_positional_or_not(__: str) -> None: ...
    def _(_: int) -> None: ...
    @classmethod
    def fine(cls, foo: int, /) -> None: ...

class Metaclass(type):
    @classmethod
    def __new__(mcls, __name: str, __bases: tuple[type, ...], __namespace: dict, **kwds) -> Self: ...  # PYI063

class Metaclass2(type):
    @classmethod
    def __new__(metacls, __name: str, __bases: tuple[type, ...], __namespace: dict, **kwds) -> Self: ...  # PYI063

class GoodMetaclass(type):
    @classmethod
    def __new__(mcls, name: str, bases: tuple[type, ...], namespace: dict, /, **kwds) -> Self: ...

class GoodMetaclass2(type):
    @classmethod
    def __new__(metacls, name: str, bases: tuple[type, ...], namespace: dict, /, **kwds) -> Self: ...
