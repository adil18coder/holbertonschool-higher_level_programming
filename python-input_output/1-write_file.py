#!/usr/bin/python3
"""UTF-8 faylına mətn yazan modul."""


def write_file(filename="", text=""):
    """UTF-8 faylına mətn yazır və yazılan simvolların sayını qaytarır."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
