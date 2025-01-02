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
# Run a Trust Game trial
investment_p = tg_invest(win, prompt_text = investment_text, min_investment= min_investment_p, max_investment= max_investment_p)
display_text(win, 'Poczekaj na decyzje powiernika')
random_time = random.uniform(3, 6)
core.wait(random_time)
tg_return(win, return_text= return_text_p, investment= investment_p, multiplier= 1.3)
wait_for_spacebar()