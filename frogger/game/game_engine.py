"""
GameEngine for Frogger.

Completed tasks:
1. Vehicle collision detection
2. Three lives and respawn
3. Goal detection and score
4. Thirty-second countdown timer
"""

import random
import pygame

from game.frog import Frog
from game.vehicle import Vehicle
from game.collisions import check_collision

from game.renderer import (
    GRID_COLS,
    GRID_ROWS,
    GOAL_ROW,
    ROAD_ROWS,
    START_ROW,
    CELL_SIZE,
    WIDTH,
    HEIGHT,
)


# Vehicle speeds for each road lane
LANE_SPEEDS = [1.5, -2, 2, -2.5, 1.5, -2]

# Task 4: 30-second timer
TIME_LIMIT = 30


class GameEngine:

    def __init__(self):

        # -----------------------------
        # Game state
        # -----------------------------

        self.lives = 3

        self.score = 0

        self.game_over = False

        self.won = False

        # Start timer
        self.time_left = TIME_LIMIT

        self.last_time = pygame.time.get_ticks()

        # Create frog and vehicles
        self._build_entities()

    # =========================================================
    # BUILD GAME ENTITIES
    # =========================================================

    def _build_entities(self):

        start_col = GRID_COLS // 2

        # -----------------------------
        # Create frog
        # -----------------------------

        self.frog = Frog(
            col=start_col,
            row=START_ROW,
            start_col=start_col,
            start_row=START_ROW,
            cols=GRID_COLS,
            start_row_limit=START_ROW,
        )

        frog_x_range = (
            start_col * CELL_SIZE,
            start_col * CELL_SIZE + CELL_SIZE,
        )

        # -----------------------------
        # Create vehicles
        # -----------------------------

        self.vehicles = []

        for i, row in enumerate(ROAD_ROWS):

            speed = LANE_SPEEDS[i % len(LANE_SPEEDS)]

            # Alternate between cars and trucks
            vehicle_width = 40 if i % 2 == 0 else 70

            spacing = 300

            count = 2

            # Try several random starting positions
            # so vehicles don't begin on the frog.
            for _attempt in range(20):

                phase = random.randint(
                    0,
                    spacing - 1
                )

                positions = []

                safe = True

                for n in range(count):

                    offset = phase + n * spacing

                    if speed > 0:

                        x = offset

                    else:

                        x = (
                            WIDTH
                            - offset
                            - vehicle_width
                        )

                    positions.append(x)

                    # Check starting overlap
                    if not (
                        x + vehicle_width <= frog_x_range[0]
                        or x >= frog_x_range[1]
                    ):
                        safe = False

                if safe:
                    break

            # Create vehicles
            for x in positions:

                self.vehicles.append(
                    Vehicle(
                        x=x,
                        row=row,
                        width=vehicle_width,
                        height=CELL_SIZE - 8,
                        speed=speed,
                    )
                )

    # =========================================================
    # RESET ATTEMPT TIMER
    # =========================================================

    def reset_timer(self):

        self.time_left = TIME_LIMIT

        self.last_time = pygame.time.get_ticks()

    # =========================================================
    # HANDLE KEYBOARD
    # =========================================================

    def handle_keydown(self, key):

        # -----------------------------------------
        # If game is over or won
        # only R should work.
        # -----------------------------------------

        if self.game_over or self.won:

            if key == pygame.K_r:

                self.lives = 3

                self.score = 0

                self.game_over = False

                self.won = False

                self.reset_timer()

                self._build_entities()

            return

        # -----------------------------------------
        # Frog movement
        # -----------------------------------------

        if key == pygame.K_UP:

            self.frog.move(0, -1)

        elif key == pygame.K_DOWN:

            self.frog.move(0, 1)

        elif key == pygame.K_LEFT:

            self.frog.move(-1, 0)

        elif key == pygame.K_RIGHT:

            self.frog.move(1, 0)

        # -----------------------------------------
        # Manual restart
        # -----------------------------------------

        elif key == pygame.K_r:

            self.lives = 3

            self.score = 0

            self.game_over = False

            self.won = False

            self.reset_timer()

            self._build_entities()

    # =========================================================
    # HANDLE COLLISION
    # =========================================================

    def handle_life_loss(self):

        # Lose one life
        self.lives -= 1

        # Respawn frog
        self.frog.reset()

        # Give the player another 30 seconds
        self.reset_timer()

        # Check Game Over
        if self.lives <= 0:

            self.lives = 0

            self.game_over = True

    # =========================================================
    # HANDLE TIMER EXPIRY
    # =========================================================

    def handle_timeout(self):

        # Timeout costs one life
        self.lives -= 1

        # Respawn frog
        self.frog.reset()

        # Start a fresh 30-second attempt
        self.reset_timer()

        # Check Game Over
        if self.lives <= 0:

            self.lives = 0

            self.game_over = True

    # =========================================================
    # UPDATE GAME
    # =========================================================

    def update(self):

        # Don't update after Game Over or Win
        if self.game_over or self.won:

            return

        # -----------------------------------------
        # TIMER
        # -----------------------------------------

        current_time = pygame.time.get_ticks()

        elapsed_seconds = (
            current_time - self.last_time
        ) / 1000.0

        if elapsed_seconds >= 1:

            seconds_passed = int(
                elapsed_seconds
            )

            self.time_left -= seconds_passed

            self.last_time = current_time

        # Timer expired
        if self.time_left <= 0:

            self.time_left = 0

            self.handle_timeout()

            return

        # -----------------------------------------
        # Move vehicles
        # -----------------------------------------

        for vehicle in self.vehicles:

            vehicle.update(
                road_width_px=WIDTH
            )

        # -----------------------------------------
        # Collision detection
        # -----------------------------------------

        if check_collision(
            self.frog,
            self.vehicles
        ):

            self.handle_life_loss()

            return

        # -----------------------------------------
        # Goal detection
        # -----------------------------------------

        if self.frog.row == GOAL_ROW:

            # Award points
            self.score += 100

            # Set winning state
            self.won = True

            return

    # =========================================================
    # DRAW GAME
    # =========================================================

    def draw(self, surface, font):

        from game import renderer

        # Draw frog, vehicles and board
        renderer.draw_scene(
            surface,
            self.frog,
            self.vehicles,
        )

        # Draw lives, score, timer and state
        renderer.draw_game_status(
            surface,
            font,
            self.lives,
            self.score,
            self.time_left,
            self.game_over,
            self.won,
        )

        # Instructions
        renderer.draw_text(
            surface,
            font,
            "Arrow keys to move. R to restart.",
            (10, HEIGHT - 24),
        )