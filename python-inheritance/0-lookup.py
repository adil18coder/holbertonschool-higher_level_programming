#!/usr/bin/python3
"""
Bu modul lookup funksiyasını ehtiva edir.
lookup(obj) funksiyası obyektin atribut və metodlarını
siyahı şəklində qaytarır.
"""


def lookup(obj):
    """
    Obyektin mövcud atributlarını və metodlarını siyahı şəklində qaytarır.
    """
    return dir(obj)
