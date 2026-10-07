"""
Collision detection for Frogger.

Task 1:
Detect actual rectangle overlap between the frog and vehicles.
"""

import pygame

CELL_SIZE = 50


def check_collision(frog, vehicles):
    """
    Returns True if the frog overlaps any vehicle.
    """

    frog_rect = frog.get_rect(CELL_SIZE)

    for vehicle in vehicles:

        vehicle_rect = vehicle.get_rect(CELL_SIZE)

        if frog_rect.colliderect(vehicle_rect):
            return True

    return False