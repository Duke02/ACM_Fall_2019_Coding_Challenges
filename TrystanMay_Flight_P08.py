# TrystanMay_Flight_P08.py
# Fall Break Code - P08
# Trystan May (duke0200#5658)
# This program is written in Python (Version 3.7)
# This program is my own work. Any work I have
# copied has been properly attributed and used
# with permission

import typing as tp


def remove_consecutive_duplicates(l: tp.List[tp.Any]) -> tp.List[tp.Any]:
    return [l[i] for i in range(len(l) - 1) if l[i + 1] != l[i]] + [l[-1]]


input_list: tp.List[int] = sorted(list(range(10)) + list(range(10))) + list(range(10))

output_str: str = f"""
--------------------------------------------------------------------------------
P08 (**) Eliminate consecutive duplicates of list elements.
INPUT: {input_list}
OUTPUT: {remove_consecutive_duplicates(input_list)}
--------------------------------------------------------------------------------
"""

print(output_str)
