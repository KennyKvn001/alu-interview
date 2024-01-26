#!/usr/bin/python3
"""Module for the rain function
"""


def rain(walls):
    """Function to find the maximum rain collected
    by a series of walls
    """
    if type(walls) is not list or not all(type(n) is int for n in walls):
        return 0

    water_units = 0
    L_wall_i = 0
    walls_len = len(walls)

    # stop at size - 2 since two adjacent walls can't hold water
    for i in range(0, walls_len - 2):
        # next wall that is non-zero height and begins new basin
        if walls[i] > 0 and i >= L_wall_i:
            # likewise, right wall must be at least 2 units from left wall
            for j in range(i + 2, walls_len):
                if walls[j] >= walls[i]:
                    # water level can only be as high as lowest wall of basin
                    water_level = walls[i]

                    for k in range(i + 1, j):
                        water_units += water_level - walls[k]

                    # right wall becomes left wall of next potential basin
                    L_wall_i = j
                    break

    return water_units
