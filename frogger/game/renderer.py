"""
Renderer for Frogger.

All pygame drawing is handled here.
"""

import pygame


# =========================================================
# GAME DIMENSIONS
# =========================================================

CELL_SIZE = 50

GRID_COLS = 12

GRID_ROWS = 8

WIDTH = CELL_SIZE * GRID_COLS

HEIGHT = CELL_SIZE * GRID_ROWS

# Required by main.py
WINDOW_SIZE = (WIDTH, HEIGHT)


# =========================================================
# GAME ROWS
# =========================================================

GOAL_ROW = 0

ROAD_ROWS = list(
    range(1, GRID_ROWS - 1)
)

START_ROW = GRID_ROWS - 1


# =========================================================
# COLORS
# =========================================================

COLOR_BG = (20, 20, 25)

COLOR_GOAL = (40, 130, 60)

COLOR_ROAD = (45, 45, 50)

COLOR_START = (40, 90, 60)

COLOR_LINE = (90, 90, 90)

COLOR_FROG = (80, 220, 100)

COLOR_VEHICLE = (220, 80, 70)

COLOR_TEXT = (255, 255, 255)

COLOR_SCORE = (255, 220, 80)

COLOR_TIMER = (255, 255, 255)

COLOR_GAME_OVER = (255, 80, 80)

COLOR_WIN = (80, 255, 120)


# =========================================================
# DRAW GAME SCENE
# =========================================================

def draw_scene(surface, frog, vehicles):

    # Background
    surface.fill(COLOR_BG)

    # -----------------------------------------
    # Draw rows
    # -----------------------------------------

    for row in range(GRID_ROWS):

        rect = pygame.Rect(
            0,
            row * CELL_SIZE,
            WIDTH,
            CELL_SIZE,
        )

        # Goal row
        if row == GOAL_ROW:

            pygame.draw.rect(
                surface,
                COLOR_GOAL,
                rect,
            )

        # Starting row
        elif row == START_ROW:

            pygame.draw.rect(
                surface,
                COLOR_START,
                rect,
            )

        # Road
        else:

            pygame.draw.rect(
                surface,
                COLOR_ROAD,
                rect,
            )

            pygame.draw.line(
                surface,
                COLOR_LINE,
                (
                    0,
                    row * CELL_SIZE,
                ),
                (
                    WIDTH,
                    row * CELL_SIZE,
                ),
                1,
            )

    # -----------------------------------------
    # Draw vehicles
    # -----------------------------------------

    for vehicle in vehicles:

        pygame.draw.rect(
            surface,
            COLOR_VEHICLE,
            vehicle.get_rect(CELL_SIZE),
            border_radius=6,
        )

    # -----------------------------------------
    # Draw frog
    # -----------------------------------------

    pygame.draw.rect(
        surface,
        COLOR_FROG,
        frog.get_rect(CELL_SIZE),
        border_radius=8,
    )


# =========================================================
# DRAW TEXT
# =========================================================

def draw_text(
    surface,
    font,
    text,
    pos,
    color=COLOR_TEXT,
):

    text_surface = font.render(
        text,
        True,
        color,
    )

    surface.blit(
        text_surface,
        pos,
    )


# =========================================================
# DRAW GAME STATUS
# =========================================================

def draw_game_status(
    surface,
    font,
    lives,
    score,
    time_left,
    game_over,
    won,
):

    # -----------------------------------------
    # WIN
    # -----------------------------------------

    if won:

        # Top status bar
        status_rect = pygame.Rect(
            0,
            0,
            WIDTH,
            CELL_SIZE,
        )

        pygame.draw.rect(
            surface,
            COLOR_GOAL,
            status_rect,
        )

        text_surface = font.render(
            "YOU WIN!  Score: {}".format(score),
            True,
            COLOR_WIN,
        )

        text_rect = text_surface.get_rect(
            center=status_rect.center
        )

        surface.blit(
            text_surface,
            text_rect,
        )

        # Center banner
        banner_surface = font.render(
            "YOU WIN! Press R to restart",
            True,
            COLOR_SCORE,
        )

        banner_rect = banner_surface.get_rect(
            center=(
                WIDTH // 2,
                HEIGHT // 2,
            )
        )

        surface.blit(
            banner_surface,
            banner_rect,
        )

        return

    # -----------------------------------------
    # GAME OVER
    # -----------------------------------------

    if game_over:

        status_rect = pygame.Rect(
            0,
            0,
            WIDTH,
            CELL_SIZE,
        )

        pygame.draw.rect(
            surface,
            COLOR_GAME_OVER,
            status_rect,
        )

        text_surface = font.render(
            "GAME OVER",
            True,
            COLOR_TEXT,
        )

        text_rect = text_surface.get_rect(
            center=status_rect.center
        )

        surface.blit(
            text_surface,
            text_rect,
        )

        # Center message
        banner_surface = font.render(
            "GAME OVER - Press R to restart",
            True,
            COLOR_SCORE,
        )

        banner_rect = banner_surface.get_rect(
            center=(
                WIDTH // 2,
                HEIGHT // 2,
            )
        )

        surface.blit(
            banner_surface,
            banner_rect,
        )

        return

    # -----------------------------------------
    # NORMAL GAME
    # -----------------------------------------

    status_rect = pygame.Rect(
        0,
        0,
        WIDTH,
        CELL_SIZE,
    )

    pygame.draw.rect(
        surface,
        COLOR_START,
        status_rect,
    )

    # Make sure timer doesn't become negative
    display_time = max(
        0,
        int(time_left)
    )

    status_text = (
        "Lives: {}    Score: {}    Time: {}s"
        .format(
            lives,
            score,
            display_time,
        )
    )

    text_surface = font.render(
        status_text,
        True,
        COLOR_TEXT,
    )

    text_rect = text_surface.get_rect(
        center=status_rect.center
    )

    surface.blit(
        text_surface,
        text_rect,
    )


# =========================================================
# DRAW CENTER BANNER
# =========================================================

def draw_banner(
    surface,
    font,
    text,
):

    text_surface = font.render(
        text,
        True,
        COLOR_SCORE,
    )

    text_rect = text_surface.get_rect(
        center=(
            surface.get_width() // 2,
            surface.get_height() // 2,
        )
    )

    surface.blit(
        text_surface,
        text_rect,
    )