#!/usr/bin/env python3

import sys

class NoArgumentsError(Exception):
    pass

class NonNumericError(Exception):
    pass

def is_number(scores: list) -> bool: # mee bezig
    i = 1
    while i < len(scores):
        try:
            float(scores[i])
        except ValueError:
            return False
        i += 1
    return True

def check_errors(scores: list) -> None:
    if len(scores) < 2:
        raise NoArgumentsError("No arguments provided")
    #if is_number(scores) is False:
    #    raise NonNumericError("Non numeric found")
    is_number(scores)


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
    test_score_analytics(sys.argv)
