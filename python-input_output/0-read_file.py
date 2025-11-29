#!/usr/bin/python3
"""UTF-8 faylını oxuyub ekrana çap edən modul."""


def read_file(filename=""):
    """UTF-8 faylını oxuyur və məzmununu ekrana çap edir."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
