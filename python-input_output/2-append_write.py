def append_write(filename="", text=""):
    """UTF-8 faylına mətn əlavə edir və əlavə olunan simvolların
    sayını qaytarır.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
