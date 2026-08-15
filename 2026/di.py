from collections.abc import Callable
from typing import Any, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


_injections: dict[Callable[..., Any], dict[str, dict[str, Any]]] = {}


def _inject(input_type: str, **kwargs: Any) -> Callable[[F], F]:
    def deco(fn: F) -> F:
        _injections.setdefault(fn, {})[input_type] = kwargs
        return fn

    return deco


def sample(**kwargs: Any) -> Callable[[F], F]:
    return _inject("sample", **kwargs)


def real(**kwargs: Any) -> Callable[[F], F]:
    return _inject("real", **kwargs)


def kwargs_for(fn: Callable[..., Any], input_type: str) -> dict[str, Any]:
    return _injections.get(fn, {}).get(input_type, {})
