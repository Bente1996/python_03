#!/usr/bin/env python3

def get_player_pos() -> tuple[float, float, float]:
    try:
        coordinates = input("Enter new coordinates as floats in format 'x,y,z'"
                            ": ").split(",")
        x, y, z = coordinates
        print(float(x))
        print(float(y))
        print(float(z))
        return (tuple(coordinates))
    except ValueError as e:
        print(f"ValueError: {e} ")
        get_player_pos()

if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get first set of coordinates")
    coordinates = get_player_pos()
    print(coordinates)
