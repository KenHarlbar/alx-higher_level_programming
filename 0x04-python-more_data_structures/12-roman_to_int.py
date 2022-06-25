#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_dict = {"I": 1, "V": 5, "X": 10,
                  "L": 50, "C": 100, "D": 500, "M": 1000}
    n = len(roman_string)
    total = roman_dict[roman_string[n - 1]]
    for i in range(n - 1, 0, -1):
        current = roman_dict[roman_string[i]]
        prev = roman_dict[roman_string[i - 1]]
        total += prev if prev >= current else -prev
    return total
