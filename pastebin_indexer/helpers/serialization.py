from typing import Callable, Any

from arrow import arrow, get as arget


def encoder(o: arrow.Arrow) -> float:
    return o.float_timestamp


def decoder(s: str, _w: Callable[..., Any] = ...) -> arrow.Arrow:  # noqa
    return arget(s)
