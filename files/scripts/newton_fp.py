from itertools import accumulate, repeat
from math import sin, cos
from typing import Callable, Generator, NewType, TypeVar


R2R = Callable[[float], float]
T = TypeVar('T')


def circuit_breaker(stream: Generator[T, None, None], max_iter: int) -> Generator[T, None, None]:
    """
    Given a (possibly infinite) stream (s0, s1, s2, ...), return the enumerated stream
    
        (0, s0), (1, s1), (2, s2), ..., (n-1, s(n-1))
        
    where n is the maximum number of iterations.
    
    Args:
        stream: input stream
        max_iter: maximum number of iterations
    """
    return zip(range(max_iter), stream)


def iterate_v1(proc: Callable[[T], T], x: T) -> Generator[T, None, None]:
    """
    Generator for computing the sequence

        x, proc(x), proc(proc(x)), proc(proc(proc(x))), ...

    Args:
        proc: function we are using to perform the iteration
        x: initial function input
    """
    while True:
        yield x
        x = proc(x)



def iterate_v2(proc: Callable[[T], T], x: T) -> Generator[T, None, None]:
    """..."""
    return accumulate(repeat(x), lambda procx, _: proc(procx))


def newton_v1(f: R2R, df: R2R, x0: float, tol: float=1e-8) -> float:
    """
    1D Newton method implemented in a procedural style.
    Args:
        f: function we are interested in extracting a root from
        df: derivative of the function f
        x0: initial guess
        tol: numerical tolerance for the value of f at the root
    Returns:
        root: approximate location of a root of the function f
    """
    x = x0
    while True:
        x -= f(x) / df(x)

        if abs(f(x)) < tol:
            break

    return x

def newton_v2(f: R2R, df: R2R, x0: float, tol: float=1e-8, max_iter: int=1000) -> float:
    """..."""
    x = x0
    i = 0
    while abs(f(x)) > tol and i < max_iter:
        x -= f(x) / df(x)
        i += 1

    return x


def newton_v3a(f: R2R, df: R2R, x0: float, tol: float=1e-8) -> float:
    """..."""
    for x in iterate_v1(lambda x: x - f(x) / df(x), x0):
        if abs(f(x)) < tol:
            return x

def newton_v3(f: R2R, df: R2R, x0: float, tol: float=1e-8) -> float:
    """..."""
    for x in iterate_v2(lambda x: x - f(x) / df(x), x0):
        if abs(f(x)) < tol:
            return x


def newton_v4a(f: R2R, df: R2R, x0: float, tol: float=1e-8, max_iter: int=1000) -> float:
    """..."""
    newton_method = iterate_v1(lambda x: x - f(x) / df(x), x0)
    for i, x in circuit_breaker(newton_method, max_iter):
        if abs(f(x)) < tol:
            return x



def newton_v4(f: R2R, df: R2R, x0: float, tol: float=1e-8, max_iter: int=1000) -> float:
    """..."""
    newton_method = iterate_v2(lambda x: x - f(x) / df(x), x0)
    for i, x in circuit_breaker(newton_method, max_iter):
        if abs(f(x)) < tol:
            return x


if __name__ == '__main__':
    f = sin
    df = cos

    x0 = 2.


