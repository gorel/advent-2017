# /usr/bin/env python3

from __future__ import annotations

from advent.base import BaseSolver, Solution


class Solver(BaseSolver):
    def solve(self) -> Solution:
        inc = len(self.data) // 2
        part1 = 0
        part2 = 0
        for i, c in enumerate(self.data):
            if c == self.data[(i + 1) % len(self.data)]:
                part1 += int(c)
            if c == self.data[(i + inc) % len(self.data)]:
                part2 += int(c)

        yield part1
        yield part2


Solver.run()
