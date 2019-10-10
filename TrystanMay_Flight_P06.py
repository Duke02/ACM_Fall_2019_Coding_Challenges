#!/usr/bin/env python3

# TrystanMay_Flight_P06.py
# Fall Break Code - P06
# Trystan May (duke0200#5658)
# This program is written in Python (Version 3.7)
# This program is my own work. Any work I have
# copied has been properly attributed and used
# with permission

import typing as tp


def is_palindrome(l: tp.List[tp.Any]) -> bool:
	return l == l[::-1]

input_data_1: tp.List[str] = list("racecar")
input_data_2: tp.List[str] = list("hello")

output_str: str = f"""
--------------------------------------------------------------------------------
P96 (*) Find out whether a list is a palindrome.
INPUT: {input_data_1}, {input_data_2}
OUTPUT: {is_palindrome(input_data_1)}, {is_palindrome(input_data_2)}
--------------------------------------------------------------------------------
"""

print(output_str)
