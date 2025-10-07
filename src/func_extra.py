from classes import *

def generate_tones() -> list[float]:
    base: float = 13.75
    power: list[float] = [2 ** (i / 12) for i in range(12)]
    tones: list[float] = [base * (1 << j) * i for j in range(11) for i in power]
    return tones[3:123]

def linear_interpolation(start: float, end: float, dist: float) -> float:
    return start * (1 - dist) + end * dist
