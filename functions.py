from psychopy.hardware import keyboard
from psychopy import visual, event, core
from parameters import  *

def wait_for_spacebar():
    """
    Waits for the user to press the space bar and clears residual events.
    """
    # Clear any previous key presses
    event.clearEvents()

    while True:
        keys = event.getKeys()  # Check for keypresses
        if 'space' in keys:  # Check if space was pressed
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

def display_text_ESM(win, text, position='left'):
    """
    Display text on either the left or right part of the window.

    Parameters:
    - win: The PsychoPy window object.
    - text: The text to display.
    - position: 'left' or 'right' to specify which half of the window to display the text on.
    """
    # Determine the position based on the parameter
    if position == 'left':
        pos = (-0.5, 0)  # Left side in normalized units
    elif position == 'right':
        pos = (0.5, 0)  # Right side in normalized units
    else:
        raise ValueError("Position must be 'left' or 'right'.")

    # Create the text stimulus
    text_stim = visual.TextStim(
        win=win,
        text=text,
        color=[-1, -1, -1],  # Black text
        pos=pos,  # Position based on the side
        height=0.05  # Scalable text height
    )

    # Draw and flip the window to display the text
    text_stim.draw()

def single_selection_screen(win, words, header_text, feeling):
    """
    Displays a single selection screen with navigation and confirmation for one participant.

    Parameters:
    - win: PsychoPy window object.
    - words: List of words to display.
    - keys: Dictionary with keys for navigation ('up', 'down', 'confirm').
    - header_text: Text displayed at the top.
    - feeling: Additional text displayed with the header.
    """
    # Clear any previous key presses
    event.clearEvents()
    # Create a Keyboard object
    kb = keyboard.Keyboard()

    # Initial index for highlighted word
    index = 0
    confirmed = False

    # Function to draw words with highlighted index and a rectangle around it
    def draw_words(words, highlight_index, x_pos=0):
        # Draw header text
        header = visual.TextStim(
            win=win,
            text=header_text + " " + feeling,
            pos=(x_pos, 0.7),  # Position the header above the words
            color=[-1, -1, -1],  # Black text
            height=0.05
        )
        header.draw()

        # Draw selectable words
        for i, word in enumerate(words):
            color = [-1, -1, -1] if i != highlight_index else [1, -1, -1]  # Highlight color
            message = visual.TextStim(
                win=win,
                text=word,
                pos=(x_pos, 0.3 - 0.1 * i),  # Position words vertically
                color=color,
                height=0.05
            )
            message.draw()

            # Draw a rectangle around the highlighted word
            if i == highlight_index:
                rect = visual.Rect(
                    win=win,
                    width=0.8,  # Width of the rectangle
                    height=0.08,  # Height of the rectangle
                    pos=(x_pos, 0.3 - 0.1 * i),  # Same position as the highlighted word
                    lineColor=[1, -1, -1],  # Red border
                    lineWidth=3
                )
                rect.draw()

    # Main loop
    while not confirmed:
        # Clear the screen
        win.clearBuffer()

        # Draw words for the single side
        draw_words(words, index)

        # Flip the window to update the screen
        win.flip()

        keys_pressed = event.getKeys()
        for key in keys_pressed:
            if key == key_mappings['up']:
                index = (index - 1) % len(words)  # Move selection up
            elif key == key_mappings['down']:
                index = (index + 1) % len(words)  # Move selection down
            elif key == key_mappings['confirm']:
                confirmed = True  # Confirm selection

    # Return the selected index
    return index


def tg_invest(win, prompt_text, min_investment, max_investment, font_size=0.1):
    """
    Simulated input box using TextStim to display input and handle key presses manually.

    Parameters:
        win (visual.Window): The PsychoPy window object.
        prompt_text (str): The text displayed as a prompt for the input box.
        min_investment (int): Minimum allowed investment.
        max_investment (int): Maximum allowed investment.
        font_size (float): Font size for the text and prompt (default: 0.1).
    """
    # Create input prompt and warning text
    prompt_stim = visual.TextStim(
        win,
        text=prompt_text,
        color="white",
        height=font_size,
        pos=(0, 0.2)  # Position above input box
    )
    input_display = visual.TextStim(
        win,
        text="",  # Start with empty input
        color="white",
        height=font_size,
        pos=(0, -0.1)  # Position below the prompt
    )
    warning_stim = visual.TextStim(
        win,
        text="",  # Start with no warning
        color="red",
        height=font_size * 0.8,
        pos=(0, -0.3)  # Position below the input display
    )

    investment = None
    input_text = ""

    while investment is None:
        # Draw the components
        prompt_stim.draw()
        input_display.text = input_text  # Update displayed text
        input_display.draw()
        warning_stim.draw()
        win.flip()

        # Get key presses
        keys = event.getKeys()
        for key in keys:
            if key == "return":  # When Enter is pressed
                if input_text == "":
                    warning_stim.text = "Pole nie może być puste. Spróbuj ponownie."
                else:
                    try:
                        entered_value = int(input_text)
                        if entered_value < min_investment:
                            warning_stim.text = "Zła wartość: inwestycja poniżej minimum, spróbuj ponownie."
                        elif entered_value > max_investment:
                            warning_stim.text = "Zła wartość: inwestycja powyżej maksimum, spróbuj ponownie."
                        else:
                            investment = entered_value  # Valid input
                            break
                    except ValueError:
                        warning_stim.text = "Nie podałeś właściwej wartości, spróbuj jeszcze raz."
                input_text = ""  # Clear input after pressing Enter
            elif key == "backspace":  # Handle backspace
                input_text = input_text[:-1]  # Remove last character
            elif key == "escape":  # Exit option
                core.quit()
            elif len(key) == 1:  # Append other keys (ignore special keys)
                input_text += key

    # Clear the screen after valid input
    win.flip()

    return investment


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

    return return_value















