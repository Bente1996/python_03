#!/usr/bin/env python3

import sys

class NoArgumentsError(Exception):
    pass

class NonNumericError(Exception):
    pass

def non_numeric(scores: list) -> bool:
    args = len(scores)
    i = 1
    for _ in range(args - 1):
        j = 0
        print(f"Index {i}: {scores[i]}")
        i += 1
        str(scores[i])
        while scores[i][j]:
            if scores[i][j] < '0' or scores [i][j] > '9':
                print(scores[i])
    return True
    #args = len(scores)
    #i = 1
    #while i < args:
    #    j = 0
    #    while scores[i][j]:
    #        if scores[i][j] < 0 or scores[i][j] > 9:
    #            return True
    #    i += 1
    #return False

def check_errors(scores: list) -> None:
    if len(scores) < 2:
        raise NoArgumentsError("No arguments provided")
    if non_numeric(scores) is True:
        raise NonNumericError("Non numeric found")


def scores_processed(scores: list) -> None:
    i = 1
    print("[ ", end="")
    while i < len(scores):
        print(f"{scores[i]}, ", end="")
        i += 1

def test_score_analytics(scores: list) -> None:
    try:
        check_errors(scores)
    except NoArgumentsError as e:
        print(f"Caught NoArgumentsError: {e}")
    finally:
        print("pluh")

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    #test_score_analytics(sys.argv)
    non_numeric(sys.argv)
