from functions import  *
from parameters import  *
import csv
import random
import time


### START
# Display welcome text
display_text(win, welcome_text)
wait_for_spacebar()

# display instructions
display_text(win, instructions1)
wait_for_spacebar()

# tg
# Loop through the specified number of iterations
for i in range(TG_trials):
    # Display the investment prompt
    investment_text = f'Masz w tej chwili {max_investment_p:.2f}\n\n\nIlę chciałabyś/byś zainwestować?'
    investment_p = tg_invest(win, prompt_text=investment_text, min_investment=min_investment_p, max_investment=max_investment_p)

    # Calculate the return, clamping it to the specified range
    investment_return = 3*investment_p
    display_text(win, f'Inwestycja została pomnożona trzykrotnie i wynosi {investment_return:.2f}.\n\n\nWciśnij spację, aby się dowiedzieć ile powiernik zdecydował się Ci zwrócić.')
    wait_for_spacebar()

    # Adjust the multiplier based on the investment compared to the previous one
    if previous_investment is not None:
        if investment_p < previous_investment:
            multiplier += 0.1  # Increase multiplier
        elif investment_p > previous_investment:
            multiplier -= 0.1  # Decrease multiplier

    # Display the return breakdown
    return_p = tg_return(win, return_text=return_text_p, investment=investment_p, multiplier=multiplier)
    wait_for_spacebar()

    # Update the budget (max_investment_p) based on the initial budget
    max_investment_p -= investment_p
    max_investment_p += return_p



    # Store the current investment for comparison in the next iteration
    previous_investment = investment_p
    print(previous_investment)
    print(multiplier)