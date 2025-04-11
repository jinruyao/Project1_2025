# Author: Jinru Yao
# Date: 9/4/2025

from gpiozero import LED, Button
from time import sleep, time
from random import uniform
import os

# Initialize a flag to control the main loop
game_over = False

try:
    # Initialize the LED conntection
    led = LED(4)
    right_button = Button(15)
    left_button = Button(14)

    # Get the name of the players
    left_name = input('Left player name is: ')
    right_name = input('Right player name is: ')

    # Control the LED
    led.on()
    sleep_duration = uniform(5, 10)
    sleep(sleep_duration)
    led.off()

    # Record the time when the LED turned off
    start_time = time()

    # Define a function to be called when a button pressed
    def pressed(button):
        global game_over
        print(f"Button pressed: {button.pin.number}")  # 添加调试信息
        # Record the time when the button was pressed
        end_time = time()
        # Calculate the time taken to press the button after the LED turned off
        reaction_time = end_time - start_time
        if button.pin.number == 14:
            print(left_name + " won the game in "+ str(reaction_time))
        else:
            print(right_name + " won the game in " + str(reaction_time))
        # Set the flag to exit the main loop
        game_over = True

    right_button.when_pressed = pressed
    left_button.when_pressed = pressed

    # Keep the program running, untill the button pressed.
    while not game_over:
        sleep(0.1)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if 'led' in locals():
        led.close()
    if 'right_button' in locals():
        right_button.close()
    if 'left_button' in locals():
        left_button.close()
    # Optionally, you can use os._exit(0) here for immediate termination
    # os._exit(0)
