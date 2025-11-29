#!/usr/bin/python3
"""
Bu modul MyList sinifini ehtiva edir.
MyList list-dən miras alır və print_sorted() metodu ilə siyahını
sıralanmış şəkildə çap etməyə imkan verir.
"""


class MyList(list):
    """List-dən miras alan MyList sinifi"""

    def print_sorted(self):
        """Siyahını dəyişdirmədən, sıralanmış şəkildə çap edir"""
        print(sorted(self))
