from typing import Protocol


class BaseLogger(Protocol):
    def info(self, message: str) -> None: ...

    def error(self, message: str) -> None: ...

    def debug(self, message: str) -> None: ...

    def warning(self, message: str) -> None: ...

    def critical(self, message: str) -> None: ...

    def exception(self, message: str) -> None: ...
