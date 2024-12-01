# /usr/bin/env python3

from __future__ import annotations

from advent.base import BaseSolver, Solution
from advent.graph import Direction, Point

# Spiral pattern
# 1 exists at (0,0) -> square1 -> call x value "idx"
# 4 exists at (0, 1)
# 9 exists at (1, -1) -> square3 -> idx = 1
# 16 exists at (-1, 2)
# 25 exists at (2, -2) -> square5 -> idx = 2
# 36 exists at (-2, 3)
# odd squares exists at (idx, idx) where idx advances every 2 squares
# even squares exist at (-idx, idx+1)


def find(target: int) -> Point:
    # Travel right, up, left, down until you hit target
    side_length = 0
    n = 1
    p = Point(0, 0)
    d = Direction.RIGHT

    while n < target:
        side_length += 1
        for _ in range(2):
            # Travel forward in the current direction
            for _ in range(side_length):
                n += 1
                p += d
                if n == target:
                    return p
            d = d.counter_clockwise
    return p


def sum_neighbors(g: dict[Point, int], p: Point) -> int:
    return sum(g.get(adj, 0) for adj in p.adjacent8())


def find_larger(target: int) -> int:
    g = {}
    # Travel right, up, left, down until you hit target
    side_length = 0
    n = 1
    p = Point(0, 0)
    g[p] = 1
    d = Direction.RIGHT
    while n < target:
        side_length += 1
        for _ in range(2):
            # Travel forward in the current direction
            for _ in range(side_length):
                n += 1
                p += d
                g[p] = sum_neighbors(g, p)
                print(f"{p}: {g[p]}")
                if g[p] >= target:
                    return g[p]
            d = d.counter_clockwise
    return n


class Solver(BaseSolver):
    def solve(self) -> Solution:
        target = int(self.data)
        p = find(target)
        yield p.manhattan_dist(Point(0, 0))
        yield find_larger(target)


Solver.run()
