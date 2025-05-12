import os
import time

# Constants for console dimensions and character to display
WIDTH = 80
HEIGHT = 24
CHARACTER = '#'
RADIUS = ord("X")  # Radius based on the ASCII value of 'X'

# Create a "console" as a 2D list to represent the display
console = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Function to set a pixel at the specified coordinates
def set_pixel(x, y):
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        console[y][x] = CHARACTER

# Calculate the center of the console
center_x = WIDTH // 2
center_y = HEIGHT // 2

# Main loop to update the console display
while True:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            # Draw a circle based on the radius
            if (x - center_x) ** 2 + (y - center_y) ** 2 <= RADIUS:
                set_pixel(x, y)
            else:
                console[y][x] = ' '  # Clear other pixels

            # Print the console display, updating in place
            print('\n'.join([''.join(row) for row in console]), end='\r')
            time.sleep(0.01)  # Delay to control the update speed

    # Clear the screen for the next frame
    os.system('cls' if os.name == 'nt' else 'clear')
