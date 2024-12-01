# /usr/bin/env python3

from __future__ import annotations

from advent.base import BaseSolver, Solution


class Solver(BaseSolver):
    def solve(self) -> Solution:
        part1 = 0
        part2 = 0
        for line in self.lines:
            d = set()
            d2 = set()
            valid = True
            valid2 = True
            for word in line.split():
                if word in d:
                    valid = False
                d.add(word)
                word2 = "".join(sorted(word))
                if word2 in d2:
                    valid2 = False
                d2.add(word2)
            if valid:
                part1 += 1
            if valid2:
                part2 += 1

        yield part1
        yield part2


Solver.run()
