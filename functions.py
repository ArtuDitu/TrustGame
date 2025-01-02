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


def display_text(win, text, bold_indices=None, font_sizes=None, color_indices=None, duration=5):
    """
    Display text on the screen with options for bold, font size, and color changes.

    Parameters:
        win (visual.Window): The PsychoPy window object.
        text (str): The full text to display.
        bold_indices (list of tuples): List of (start, end) tuples indicating bold text indices.
        font_sizes (dict): Dictionary mapping (start, end) tuples to font sizes.
        color_indices (dict): Dictionary mapping (start, end) tuples to colors.
        duration (float): How long to display the text (in seconds).
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
    core.wait(duration)
    win.flip()


# Example usage
if __name__ == "__main__":
    # Create a PsychoPy window
    win = visual.Window(size=(800, 600), color="black", fullscr=False)

    # Display text with bold, font size, and color changes
    display_text(
        win,
        "This is an example of bold, varied font size, and colored text.",
        bold_indices=[(11, 15)],  # Make "bold" bold
        font_sizes={(23, 30): 0.15},  # Make "varied" larger
        color_indices={(37, 47): "red"},  # Make "colored" red
        duration=5
    )
    win.close()
    core.quit()
