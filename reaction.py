# Author: Yao Yao
# Date: 11/4/25

from gpiozero import LED, Button
from time import sleep
from random import uniform

# Initialize hardware components
led = LED(4)
right_button = Button(15)
left_button = Button(14)

# Get player names
left_name = input('Left player name is ')
right_name = input('Right player name is ')

# Use a dictionary to store scores, avoiding the use of nonlocal
scores = {'left': 0, 'right': 0}
rounds = 5  # Set number of game rounds
accept_input = False  # Flag to control when button presses should be accepted

def pressed(button):
    global accept_input, scores
    if accept_input:  # Only process button press if in accept state
        if button.pin.number == 14:  # If left button is pressed
            scores['left'] += 1
            print(left_name + ' won this round!')
        else:  # If right button is pressed
            scores['right'] += 1
            print(right_name + ' won this round!')
        accept_input = False  # Stop accepting inputs after first press

for i in range(rounds):
    print(f"\nRound {i + 1} begins!")
    led.on()
    sleep(uniform(5,10))  # Light stays on for a random period before turning off
    led.off()
    
    accept_input = True  # Allow button presses now that the light is off
    right_button.when_pressed = pressed
    left_button.when_pressed = pressed
    
    # Wait for a short duration to ensure the button press event is captured
    sleep(2)
    
    print(f"Scores: {left_name} {scores['left']}, {right_name} {scores['right']}")

# Determine the winner based on the final scores
print("\nGame Over!")
if scores['left'] > scores['right']:
    print(f"{left_name} wins with {scores['left']} points!")
elif scores['right'] > scores['left']:
    print(f"{right_name} wins with {scores['right']} points!")
else:
    print("It's a tie!")

