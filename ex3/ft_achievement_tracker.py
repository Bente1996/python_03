#!/usr/bin/env python3

import random

def get_achievements() -> tuple[str, ...]:
    achievements = ("Strategist", "Speed Runner", "World Savior", 
    "Crafting Genius", "Master Explorer", "Collector Supreme", "Untouchable", 
    "Boss Slayer", "Unstoppable", "Survivor", "Treasure Hunter", "First Steps",
    "Sharp Mind", "Hidden Path Finder")
    return achievements

def gen_player_achievements() -> None:
    achievements = get_achievements()
    print(achievements)

if __name__ == "__main__":
    print("=== Achievement Tracker SYstem ===\n")
    gen_player_achievements()
