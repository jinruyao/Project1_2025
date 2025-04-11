# Author: Yao Yao
# Date: 11/4/25

from gpiozero import LED, Button
from time import sleep
from random import uniform

# Initialize GPIO components
led = LED(4)
right_button = Button(15)
left_button = Button(14)

# Get player names
left_name = input('Left player name is: ')
right_name = input('Right player name is: ')

# Initialize scores for both players
left_score = 0
right_score = 0

def pressed(button):
    global left_score, right_score
    # Determine which button was pressed and update the score accordingly
    if button.pin.number == 14:
        print(left_name + ' won this round!')
        left_score += 1
    else:
        print(right_name + ' won this round!')
        right_score += 1
    # Clear button press event handlers to prepare for the next round
    right_button.when_pressed = None
    left_button.when_pressed = None

# Main game loop
rounds = int(input("Enter the number of rounds you want to play: "))
for i in range(rounds):
    # Set up button press event handlers for the current round
    right_button.when_pressed = pressed
    left_button.when_pressed = pressed
    
    led.on()
    sleep_time = uniform(5, 10)
    sleep(sleep_time) # Keep the LED on for a random period between 5 to 10 seconds
    led.off()

    # Wait until one of the buttons is pressed
    while not right_button.is_pressed and not left_button.is_pressed:
        sleep(0.1) # Prevent high CPU usage by sleeping briefly

# Display the final scores after all rounds have been played
print("\nGame Over!")
print(f"{left_name}'s total score: {left_score}")
print(f"{right_name}'s total score: {right_score}")

# Determine the winner based on the total scores
if left_score > right_score:
    print(f"{left_name} wins!")
elif right_score > left_score:
    print(f"{right_name} wins!")
else:
    print("It's a tie!")
