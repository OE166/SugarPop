import pygame as pg

class HUD:
    def __init__(self, screen, font_size=24, position=(10, 10)):

        self.screen = screen
        self.font = pg.font.SysFont(None, font_size)
        self.position = position

    def draw(self, total_grains, grains_in_buckets, grains_in_spout, level_count):
        # Prepare the HUD text lines
        hud_lines = [
            f"Level: {level_count}",
            f"Total Grains: {total_grains}",
            f"Grains in Spout: {grains_in_spout}",
        ]
                # Start counting from 1
        bucket_number = 1
        for count in grains_in_buckets:
            message = f"Bucket {bucket_number}: {count} grains"
            hud_lines.append(message)
            bucket_number += 1


        # Render and display each line
        y_offset = self.position[1]
        for line in hud_lines:
            text_surface = self.font.render(line, True, (255, 255, 255))
            self.screen.blit(text_surface, (self.position[0], y_offset))
            y_offset += text_surface.get_height() + 5
