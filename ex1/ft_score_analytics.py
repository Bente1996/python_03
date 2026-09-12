#!/usr/bin/env python3

import sys

class NoArgumentsError(Exception):
    pass

def is_number(scores: list) -> list:
    score_list = [0] * (len(scores) - 1)
    i = 1
    j = 0
    errors = 0
    while i < len(scores):
        try:
            int(scores[i])
            score_list[j] = scores[i]
            j += 1
        except ValueError as e:
            errors += 1
            print(f"Caught ValueError: {e}")
        i += 1
    final_list = [0] * (len(score_list) - errors)
    i = 0
    while i < len(final_list):
        final_list[i] = score_list[i]
        i += 1
    return final_list

def check_errors(scores: list) -> list:
    score_list = is_number(scores)
    if len(score_list) < 2:
        raise NoArgumentsError("No scores provided. Usage:"
                               "./ft_score_analytics.py <score1> <score2> ...")
    return score_list

def scores_processed(score_list: list) -> None:
    i = 0
    print("[", end="")
    while i < len(score_list) - 1:
        print(f"{score_list[i]}, ", end="")
        i += 1
    print(f"{score_list[i]}]")

def basic_stats(score_list: list) -> None:
    print(f"Total players: {len(score_list)}")
    i = 0
    total_score = 0
    while i < len(score_list):
        total_score += int(score_list[i])
        i += 1
    print(f"Total score: {sum(int(score) for score in score_list)}")
    print(f"Average score: {total_score / len(score_list)}")
    print(f"High score: {max(score_list)}") ## gaat mis
    print(f"Low score: {float(min(score_list))}")
    print(f"Score range: {int(max(score_list)) - int(min(score_list))}")

def test_score_analytics(scores: list) -> int:
    try:
        score_list = check_errors(scores)
        scores_processed(score_list)
        basic_stats(score_list)
    except NoArgumentsError as e:
        print(f"Caught NoArgumentsError: {e}")
        return (1)
    finally:
        print("Finally :}")
    return (0)

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    test_score_analytics(sys.argv)

#~/python_03/ex1 % ./ft_score_analytics.py 2 3 4 5 65785876 pluh 1234 meerpluh 8888 1  
#=== Player Score Analytics ===
#Caught ValueError: invalid literal for int() with base 10: 'pluh'
#Caught ValueError: invalid literal for int() with base 10: 'meerpluh'
#[2, 3, 4, 5, 65785876, 1234, 8888, 1]
#Total players: 8
#Total score: 65796013
#Average score: 8224501.625
#High score: 8888
#Low score: 1.0
#Score range: 8887
#Finally :}

