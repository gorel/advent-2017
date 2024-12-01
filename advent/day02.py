# /usr/bin/env python3

from __future__ import annotations

from advent.base import BaseSolver, Solution


class Solver(BaseSolver):
    def solve(self) -> Solution:
        part1 = 0
        for line in self.lines:
            ints = [int(x) for x in line.split()]
            part1 += max(ints) - min(ints)

        yield part1

        part2 = 0
        for line in self.lines:
            ints = [int(x) for x in line.split()]
            for i in range(len(ints)):
                for j in range(i + 1, len(ints)):
                    a = ints[i]
                    b = ints[j]
                    if a % b == 0 or b % a == 0:
                        part2 += max(a, b) // min(a, b)
                        break

        yield part2


Solver.run()
