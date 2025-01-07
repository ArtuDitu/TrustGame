# import libraries
from psychopy import visual, core
from psychopy.hardware import keyboard
import os

#import pyxid2 as pyxid2
#######


#Cedrus
# get a list of all attached XID devices
#devices = pyxid2.get_xid_devices()
#dev = devices[0] # get the first device to use
#dev.reset_base_timer()
#dev.reset_rt_timer()

# example use:     dev.activate_line(bitmask=99)


# Participant number stored in a variable
dyad_number = 666
# resting state duration
rs_duration = 1 # 180
# number of trials
TG_trials = 5


###TG parameters
min_investment_p = 1
max_investment_p = 10 # this is also initial budget
previous_investment = None  # To track investment from the previous iteration



directory = 'data'
# Create a file with the participant number in its name
tg_file_name = f"TG_{dyad_number}.csv"
tg_file_path = os.path.join(directory, tg_file_name)

# Define window dimensions (update this for your setup or leave None for full-screen mode)
window_width = 1960
window_height = 1080


# Create a PsychoPy window
win = visual.Window(
    size=(window_width, window_height),  # Adjust to match your monitors' combined resolution
    color=[0.5, 0.5, 0.5],  # Gray background
    units="norm",  # Normalized units for scalability (-1 to 1 range)
    pos = (0,0),
    allowGUI=False
)
win.mouseVisible = False




### texts

welcome_text = 'Witamy\n\n Wciśnij spacje by kontynuować'
instructions1 = 'Instrukcje'
return_text_p = 'Twój powiernik zwrócił dla Ciebie:'

