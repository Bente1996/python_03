#!/usr/bin/env python3

import math

def get_player_pos() -> tuple[str, ...]:
    try:
        coordinates = input("Enter new coordinates as floats in format 'x,y,z'"
                            ": ").split(",")
        x, y, z = coordinates
        float(x)
        float(y)
        float(z)
    except ValueError as e:
        print(f"ValueError: {e} ")
        coordinates = get_player_pos()
    return (tuple(coordinates))

if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get first set of coordinates")
    coordinates = get_player_pos()
    print(coordinates)
    print(f"Got first tuple: {coordinates}")
    x, y, z = coordinates
    print(f"It includes: X={x}, Y={y}, Z={z}")
    print(f"Distance to center: {round(math.sqrt((0-float(x))**2 + 
          (0-float(y))**2 + (0-float(z))**2), 4)}")
    print("\nGet a second set of coordinates:")
    second_coordinates = get_player_pos()
    x2, y2, z2 = second_coordinates
    print("Distance between the 2 sets of coordinates: "
          f"{round(math.sqrt((float(x2)-float(x))**2 + (float(y2)-float(y))**2
          + (float(z2)-float(z))**2), 4)}")
