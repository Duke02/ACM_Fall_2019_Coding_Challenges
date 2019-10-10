#!/usr/bin/env python3

# TrystanMay_Flight_P07.py
# Fall Break Code - P07
# Trystan May (duke0200#5658)
# This program is written in Python (Version 3.7)
# This program is my own work. Any work I have
# copied has been properly attributed and used
# with permission

import typing as tp
from functools import reduce


def flatten(in_list: tp.List[tp.List[tp.Any]]) -> tp.List[tp.Any]:
    return reduce(lambda l, x: l + x, in_list)


ll: tp.List[tp.List[int]] = [list(range(i)) for i in range(10, 15)]

output_str: str = f"""
--------------------------------------------------------------------------------
P07 (**) Flatten a nested list structure.
INPUT: {ll}
OUTPUT: {flatten(ll)}
--------------------------------------------------------------------------------
"""

print(output_str)
