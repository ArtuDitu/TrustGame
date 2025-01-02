from psychopy.hardware import keyboard
from psychopy import visual, event, core
from parameters import  *

def wait_for_spacebar():
    """
    Waits for the user to press the space bar.
    """
    # Create a Keyboard object
    kb = keyboard.Keyboard()

    # Wait for the space bar press
    while True:
        keys = kb.getKeys(waitRelease=True)  # Wait for keys to be released
        if 'space' in [key.name for key in keys]:  # Check if space was pressed
            break


from psychopy import visual, core


def display_text(win, text, bold_indices=None, font_sizes=None, color_indices=None):
    """
    Display text on the screen with options for bold, font size, and color changes.

    Parameters:
        win (visual.Window): The PsychoPy window object.
        text (str): The full text to display.
        bold_indices (list of tuples): List of (start, end) tuples indicating bold text indices.
        font_sizes (dict): Dictionary mapping (start, end) tuples to font sizes.
        color_indices (dict): Dictionary mapping (start, end) tuples to colors.
    """
    # Default bold_indices, font_sizes, and color_indices
    if bold_indices is None:
        bold_indices = []
    if font_sizes is None:
        font_sizes = {}
    if color_indices is None:
        color_indices = {}

    # Prepare text components
    components = []
    start_idx = 0
    for start, end in sorted(
            bold_indices + list(font_sizes.keys()) + list(color_indices.keys()), key=lambda x: x[0]
    ):
        if start > start_idx:
            components.append((text[start_idx:start], False, None, "white"))
        is_bold = (start, end) in bold_indices
        font_size = font_sizes.get((start, end), None)
        color = color_indices.get((start, end), "white")
        components.append((text[start:end], is_bold, font_size, color))
        start_idx = end
    if start_idx < len(text):
        components.append((text[start_idx:], False, None, "white"))

    # Create visual.TextStim objects for each component
    text_objects = []
    for text_part, is_bold, size, color in components:
        text_objects.append(visual.TextStim(
            win,
            text=text_part,
            bold=is_bold,
            height=size if size else 0.1,  # Default font size is 0.1
            color=color,
            pos=(0, 0)
        ))

    # Display the text
    for obj in text_objects:
        obj.draw()
    win.flip()


from psychopy import visual, core, event

from psychopy import visual, event, core

from psychopy import visual, event, core

from psychopy import visual, event, core


def tg_invest(win, prompt_text, min_investment, max_investment, font_size=0.1):
    """
    Display text with a prompt box and warnings for invalid input, clearing old input when retrying.

    Parameters:
        win (visual.Window): The PsychoPy window object.
        prompt_text (str): The text displayed as a prompt for the input box.
        min_investment (int): Minimum allowed investment.
        max_investment (int): Maximum allowed investment.
        font_size (float): Font size for the text and prompt (default: 0.1).
    """
    # Clear any previous key presses
    event.clearEvents()

    # Create input prompt, editable text box, and warning text
    prompt_stim = visual.TextStim(
        win,
        text=prompt_text,
        color="white",
        height=font_size,
        pos=(0, 0.2)  # Position above input box
    )
    input_box = visual.TextBox2(
        win,
        text="",  # Start with an empty input
        color="white",
        pos=(0, -0.1),  # Position below the prompt
        size=(0.5, 0.1),  # Adjust box size
        alignment="center",
        editable=True,
        letterHeight=0.09,  # Font size for input text
        placeholder="",  # Remove default placeholder text
    )
    warning_stim = visual.TextStim(
        win,
        text="",  # Start with no warning
        color="red",
        height=font_size * 0.8,  # Slightly smaller than main text
        pos=(0, -0.3)  # Position below the input box
    )

    investment = None

    while investment is None:
        # Draw the main components
        prompt_stim.draw()
        input_box.draw()
        warning_stim.draw()
        win.flip()

        keys = event.getKeys()
        if "return" in keys:  # When Enter is pressed
            try:
                entered_value = int(input_box.text.strip())
                if entered_value < min_investment:
                    warning_stim.text = "Zła wartość: inwestycja poniżej minimum, spróbuj ponownie."
                    input_box.text = ""  # Clear the previous input
                elif entered_value > max_investment:
                    warning_stim.text = "Zła wartość: inwestycja powyżej maksimum, spróbuj ponownie."
                    input_box.text = ""  # Clear the previous input
                else:
                    investment = entered_value  # Valid input
                    break
            except ValueError:
                warning_stim.text = "Nie podałeś właściwej wartości, spróbuj jeszcze raz."
                input_box.text = ""  # Clear the previous input
        elif "escape" in keys:  # Option to exit with Escape
            core.quit()

    # Clear the screen after valid input
    win.flip()

    return investment


from psychopy import visual, core


def tg_return(win, return_text, investment, multiplier, font_size=0.1):
    """
    Display the return to the player after their investment.

    Parameters:
        win (visual.Window): The PsychoPy window object.
        return_text (str): Message to display above the return value.
        investment (float): The player's initial investment.
        multiplier (float): The multiplier used to calculate the return.
        font_size (float): Font size for the text (default: 0.1).
        duration (float): Duration in seconds to display the result (default: 5).
    """
    # Clear any previous key presses
    event.clearEvents()
    # Calculate the return
    return_value = investment * multiplier

    # Create the text stimuli
    message_stim = visual.TextStim(
        win,
        text=return_text,
        color="white",
        height=font_size,
        pos=(0, 0.2)  # Position above the return value
    )
    return_stim = visual.TextStim(
        win,
        text=f"{return_value:.2f}",  # Display the calculated return
        color="white",
        height=font_size,
        pos=(0, 0)  # Centered below the message
    )
    investment_stim = visual.TextStim(
        win,
        text= '\n\nWciśnij spacje by kontynuować',
        color="white",
        height=font_size * 0.8,
        pos=(0, -0.2)  # Below the return value
    )

    # Draw and display the text
    message_stim.draw()
    return_stim.draw()
    investment_stim.draw()
    win.flip()















