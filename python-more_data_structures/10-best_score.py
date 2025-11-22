#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best = None
    max_score = None
    for k, v in a_dictionary.items():
        if max_score is None or v > max_score:
            max_score = v
            best = k
    return best
