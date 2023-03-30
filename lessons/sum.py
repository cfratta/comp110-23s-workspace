"""Example function for unit tests"""


def sum_while(xs: list[float]) -> float:
    """Return sum of all elements in xs"""
    sum_total: float = 0.0
    idx: int = 0
    while idx < len(xs):
        sum_total += xs[idx]
        idx += 1
    return sum_total


def sum_for(xs: list[float]) -> float:
    """Return sum of all elements in xs"""
    sum_total: float = 0.0
    for elem in xs:
        sum_total += elem
    return sum_total


def sum_range(xs: list[float]) -> float:
  """"Return sum of all elements in xs"""
  sum_total: float = 0.0
  
  for idx in range(0, len(xs)):
    sum_total += xs[idx]
  return sum_total