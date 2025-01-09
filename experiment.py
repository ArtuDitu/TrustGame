from functions import  *
from functions import single_selection_screen
from parameters import  *
import csv
import random
import time


### START
# Display welcome text
display_text(win, welcome_text)
wait_for_spacebar()

while not understood:
    # display instructions
    display_text(win, instructions1)
    wait_for_spacebar()
    display_text(win, instructions2)
    wait_for_spacebar()
    investment_text = f'Masz w tej chwili {max_investment_p:.2f}\n\n\nIlę chciałabyś/byś zainwestować?\n\n\nWciśnij ENTER by potwierdzić'
    investment_p, rt = tg_invest(win, prompt_text=investment_text, min_investment=min_investment_p, max_investment=max_investment_p)
    investment_return = 3 * investment_p
    display_text(win, instructions3)
    wait_for_spacebar()
    display_text(win,f'Inwestycja została pomnożona trzykrotnie i wynosi {investment_return:.2f}.\n\n\nWciśnij SPACE, aby się dowiedzieć ile powiernik zdecydował się Ci zwrócić.')
    wait_for_spacebar()
    display_text(win,f'Inwestycja została pomnożona trzykrotnie i wynosi {investment_return:.2f}.\n\n\nWciśnij SPACE, aby się dowiedzieć ile powiernik zdecydował się Ci zwrócić.\n\n Poczekaj na decyzje swojego powiernika')
    # Generate a random float between 3 and 8 seconds
    delay = random.uniform(5, 10)
    # Wait for the random delay
    core.wait(delay)
    display_text(win, instructions4)
    wait_for_spacebar()
    return_p = tg_return(win, return_text=return_text_p, investment=investment_p, multiplier=1.5)
    wait_for_spacebar()
    display_text(win, instructions5)
    instructions_input = wait_for_input()
    if instructions_input == "Space bar pressed":
        understood = True
    elif instructions_input == "Enter key pressed":
        understood = False


# appraisal start
if appraisal:
    ### appraisal start
    # Display text on the left side
    display_text(win, esm_start_text)
    # Keep the window open for a few seconds
    wait_for_spacebar()
    # open  a file to store esm data
    with open(esm_file_path, mode='w', newline='', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["participant", "esm", 'question', 'answer', 'previous_condition'])  # Write the header row

    # Append rows to the file during the loop
    with open(esm_file_path, mode='a', newline='', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        # loop over different feelings
        random.shuffle(feelings)
        for feeling in feelings:
            choice= single_selection_screen(win, words_7, feeling_text, feeling)
            writer.writerow([participant_number, 'before', feeling, choice, 'none'])  # Write the iteration number and data
        random.shuffle(feelings2)
        for feeling in feelings2:
            choice = single_selection_screen(win, words_7, feeling_text, feeling)
            writer.writerow([participant_number, 'before', feeling, choice, 'none'])  # Write the iteration number and data

    # Display text on the left side
    display_text(win, esm_end_text)
    # Keep the window open till spacebar pressed by the experimentator
    wait_for_spacebar()

# open  a file to store esm data
with open(tg_file_path, mode='w', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["participant", "condition", 'investment', 'investment_return','multiplier','return', 'RT'])  # Write the header row

# tg block 1
# Loop through the specified number of iterations

# Display block start name
display_text(win, text_block1and3)
wait_for_spacebar()
core.wait(3)
with open(tg_file_path, mode='a', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)
    if start_condition == "fair":
        multiplier = 1.3
        min_return = 1.0
        max_return = 1.5
    elif start_condition == "unfair":
        multiplier = 0.3
        min_return = 0.0
        max_return = 0.3
    else:
        raise ValueError("Mode must be 'fair' or 'unfair'.")
    for i in range(TG_trials):
        # Display the investment prompt
        investment_text = f'Masz w tej chwili {max_investment_p:.2f}\n\n\nIlę chciałabyś/byś zainwestować?\n\n\nWciśnij ENTER by potwierdzić'
        investment_p, rt = tg_invest(win, prompt_text=investment_text, min_investment=min_investment_p, max_investment=max_investment_p)

        # Calculate the return, clamping it to the specified range
        investment_return = 3*investment_p
        display_text(win, f'Inwestycja została pomnożona trzykrotnie i wynosi {investment_return:.2f}.\n\n\nWciśnij SPACE, aby się dowiedzieć ile powiernik zdecydował się Ci zwrócić.')
        wait_for_spacebar()
        display_text(win,f'Inwestycja została pomnożona trzykrotnie i wynosi {investment_return:.2f}.\n\n\nWciśnij SPACE, aby się dowiedzieć ile powiernik zdecydował się Ci zwrócić.\n\n Poczekaj na decyzje swojego powiernika')
        # Generate a random float between 3 and 8 seconds
        delay = random.uniform(5, 10)
        # Wait for the random delay
        core.wait(delay)

        # Adjust the multiplier based on the investment compared to the previous one
        if previous_investment is not None:
            if investment_p < previous_investment:
                multiplier += 0.1  # Increase multiplier
            elif investment_p > previous_investment:
                multiplier -= 0.1  # Decrease multiplier

        # Display the return breakdown
        return_p = tg_return(win, return_text=return_text_p, investment=investment_p, multiplier=multiplier)
        wait_for_spacebar()

        # Store the current investment for comparison in the next iteration
        previous_investment = investment_p
        writer.writerow([participant_number, start_condition , investment_p, investment_return, multiplier,return_p, rt])  # Write the header row

# appraisal 1
if appraisal:
    ### appraisal
    # Display text on the left side
    display_text(win, esm_start_text)
    # Keep the window open for a few seconds
    wait_for_spacebar()
    # Append rows to the file during the loop
    with open(esm_file_path, mode='a', newline='', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        # loop over different feelings
        random.shuffle(feelings)
        for feeling in feelings:
            choice= single_selection_screen(win, words_7, feeling_text, feeling)
            writer.writerow([participant_number, 'first', feeling, choice, start_condition])  # Write the iteration number and data
        random.shuffle(feelings2)
        for feeling in feelings2:
            choice = single_selection_screen(win, words_7, feeling_text, feeling)
            writer.writerow([participant_number, 'first', feeling, choice, start_condition])  # Write the iteration number and data
    # Display text on the left side
    display_text(win, esm_others_text)
    # Keep the window open for a few seconds
    wait_for_spacebar()
    # Append rows to the file during the loop
    with open(esm_file_path, mode='a', newline='', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        # loop over different opinions
        random.shuffle(others_opinions)
        for opinion in others_opinions:
            choice= single_selection_screen(win, words_7, others_text, opinion)
            writer.writerow([participant_number, 'first', opinion, choice, start_condition])  # Write the iteration number and data
    # Display text on the left side
    display_text(win, esm_interaction_text)
    # Keep the window open for a few seconds
    wait_for_spacebar()
    # Append rows to the file during the loop
    with open(esm_file_path, mode='a', newline='', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        # loop over different opinions
        random.shuffle(interaction_opinions)
        for interaction in interaction_opinions:
            choice = single_selection_screen(win, words_5, interaction_text, interaction)
            writer.writerow([participant_number, 'first', interaction, choice, start_condition])  # Write the iteration number and data
        choice = single_selection_screen(win, words_person, '', interaction_opinions_person[0])
        writer.writerow([participant_number, 'first', interaction_opinions_person[0], choice, start_condition])  # Write the iteration number and data
        choice = single_selection_screen(win, words_person, '', interaction_opinions_person[1])
        writer.writerow([participant_number, 'first', interaction_opinions_person[1], choice, start_condition])  # Write the iteration number and data
    # Display text on the left side
    display_text(win, esm_activity_text)
    # Keep the window open for a few seconds
    wait_for_spacebar()
    # Append rows to the file during the loop
    with open(esm_file_path, mode='a', newline='', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        # loop over different opinions
        random.shuffle(activity_opinions)
        for activity in activity_opinions:
            choice = single_selection_screen(win, words_7, activity_text, activity)
            writer.writerow([participant_number, 'first', activity, choice, start_condition])  # Write the iteration number and data
    # Display text on the left side
    display_text(win, esm_end_text)
    # Keep the window open till spacebar pressed by the experimentator
    wait_for_spacebar()

# Display block start name
display_text(win, text_block2and4)
wait_for_spacebar()
core.wait(3)
# tg block 2
with open(tg_file_path, mode='a', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)
    if start_condition == "fair":
        multiplier = 0.3
        min_return = 0.0
        max_return = 0.3
        condition = 'unfair'
    elif start_condition == "unfair":
        multiplier = 1.3
        min_return = 1.0
        max_return = 1.5
        condition = 'fair'
    else:
        raise ValueError("Mode must be 'fair' or 'unfair'.")
    for i in range(TG_trials):
        # Display the investment prompt
        investment_text = f'Masz w tej chwili {max_investment_p:.2f}\n\n\nIlę chciałabyś/byś zainwestować?\n\n\nWciśnij ENTER by potwierdzić'
        investment_p, rt = tg_invest(win, prompt_text=investment_text, min_investment=min_investment_p, max_investment=max_investment_p)

        # Calculate the return, clamping it to the specified range
        investment_return = 3*investment_p
        display_text(win, f'Inwestycja została pomnożona trzykrotnie i wynosi {investment_return:.2f}.\n\n\nWciśnij SPACE, aby się dowiedzieć ile powiernik zdecydował się Ci zwrócić.')
        wait_for_spacebar()
        display_text(win,f'Inwestycja została pomnożona trzykrotnie i wynosi {investment_return:.2f}.\n\n\nWciśnij SPACE, aby się dowiedzieć ile powiernik zdecydował się Ci zwrócić.\n\n Poczekaj na decyzje swojego powiernika')
        # Generate a random float between 3 and 8 seconds
        delay = random.uniform(5, 10)
        # Wait for the random delay
        core.wait(delay)

        # Adjust the multiplier based on the investment compared to the previous one
        if previous_investment is not None:
            if investment_p < previous_investment:
                multiplier += 0.1  # Increase multiplier
            elif investment_p > previous_investment:
                multiplier -= 0.1  # Decrease multiplier

        # Display the return breakdown
        return_p = tg_return(win, return_text=return_text_p, investment=investment_p, multiplier=multiplier)
        wait_for_spacebar()

        # Store the current investment for comparison in the next iteration
        previous_investment = investment_p
        writer.writerow([participant_number, condition , investment_p, investment_return, multiplier,return_p, rt])  # Write the header row

if appraisal:
    ### appraisal 2
    # Display text on the left side
    display_text(win, esm_start_text)
    # Keep the window open for a few seconds
    wait_for_spacebar()
    # Append rows to the file during the loop
    with open(esm_file_path, mode='a', newline='', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        # loop over different feelings
        random.shuffle(feelings)
        for feeling in feelings:
            choice= single_selection_screen(win, words_7, feeling_text, feeling)
            writer.writerow([participant_number, 'second', feeling, choice, condition])  # Write the iteration number and data
        random.shuffle(feelings2)
        for feeling in feelings2:
            choice = single_selection_screen(win, words_7, feeling_text, feeling)
            writer.writerow([participant_number, 'second', feeling, choice, condition])  # Write the iteration number and data
    # Display text on the left side
    display_text(win, esm_others_text)
    # Keep the window open for a few seconds
    wait_for_spacebar()
    # Append rows to the file during the loop
    with open(esm_file_path, mode='a', newline='', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        # loop over different opinions
        random.shuffle(others_opinions)
        for opinion in others_opinions:
            choice= single_selection_screen(win, words_7, others_text, opinion)
            writer.writerow([participant_number, 'second', opinion, choice, condition])  # Write the iteration number and data
    # Display text on the left side
    display_text(win, esm_interaction_text)
    # Keep the window open for a few seconds
    wait_for_spacebar()
    # Append rows to the file during the loop
    with open(esm_file_path, mode='a', newline='', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        # loop over different opinions
        random.shuffle(interaction_opinions)
        for interaction in interaction_opinions:
            choice = single_selection_screen(win, words_5, interaction_text, interaction)
            writer.writerow([participant_number, 'second', interaction, choice, condition])  # Write the iteration number and data
        choice = single_selection_screen(win, words_person, '', interaction_opinions_person[0])
        writer.writerow([participant_number, 'second', interaction_opinions_person[0], choice, condition])  # Write the iteration number and data
        choice = single_selection_screen(win, words_person, '', interaction_opinions_person[1])
        writer.writerow([participant_number, 'second', interaction_opinions_person[1], choice, condition])  # Write the iteration number and data
    # Display text on the left side
    display_text(win, esm_activity_text)
    # Keep the window open for a few seconds
    wait_for_spacebar()
    # Append rows to the file during the loop
    with open(esm_file_path, mode='a', newline='', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        # loop over different opinions
        random.shuffle(activity_opinions)
        for activity in activity_opinions:
            choice = single_selection_screen(win, words_7, activity_text, activity)
            writer.writerow([participant_number, 'second', activity, choice, condition])  # Write the iteration number and data
    # Display text on the left side
    display_text(win, esm_end_text)
    # Keep the window open till spacebar pressed by the experimentator
    wait_for_spacebar()

# Display block start name
display_text(win, text_block1and3)
wait_for_spacebar()
core.wait(3)
# tg block 3
with open(tg_file_path, mode='a', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)
    if start_condition == "fair":
        multiplier = 1.3
        min_return = 1.0
        max_return = 1.5
    elif start_condition == "unfair":
        multiplier = 0.3
        min_return = 0.0
        max_return = 0.3
    else:
        raise ValueError("Mode must be 'fair' or 'unfair'.")
    for i in range(TG_trials):
        # Display the investment prompt
        investment_text = f'Masz w tej chwili {max_investment_p:.2f}\n\n\nIlę chciałabyś/byś zainwestować?\n\n\nWciśnij ENTER by potwierdzić'
        investment_p, rt = tg_invest(win, prompt_text=investment_text, min_investment=min_investment_p, max_investment=max_investment_p)

        # Calculate the return, clamping it to the specified range
        investment_return = 3*investment_p
        display_text(win, f'Inwestycja została pomnożona trzykrotnie i wynosi {investment_return:.2f}.\n\n\nWciśnij SPACE, aby się dowiedzieć ile powiernik zdecydował się Ci zwrócić.')
        wait_for_spacebar()
        display_text(win,f'Inwestycja została pomnożona trzykrotnie i wynosi {investment_return:.2f}.\n\n\nWciśnij SPACE, aby się dowiedzieć ile powiernik zdecydował się Ci zwrócić.\n\n Poczekaj na decyzje swojego powiernika')
        # Generate a random float between 3 and 8 seconds
        delay = random.uniform(5, 10)
        # Wait for the random delay
        core.wait(delay)

        # Adjust the multiplier based on the investment compared to the previous one
        if previous_investment is not None:
            if investment_p < previous_investment:
                multiplier += 0.1  # Increase multiplier
            elif investment_p > previous_investment:
                multiplier -= 0.1  # Decrease multiplier

        # Display the return breakdown
        return_p = tg_return(win, return_text=return_text_p, investment=investment_p, multiplier=multiplier)
        wait_for_spacebar()

        # Store the current investment for comparison in the next iteration
        previous_investment = investment_p
        writer.writerow([participant_number, start_condition , investment_p, investment_return, multiplier,return_p, rt])  # Write the header row

# appraisal 3
if appraisal:
    ### appraisal 3
    # Display text on the left side
    display_text(win, esm_start_text)
    # Keep the window open for a few seconds
    wait_for_spacebar()
    # Append rows to the file during the loop
    with open(esm_file_path, mode='a', newline='', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        # loop over different feelings
        random.shuffle(feelings)
        for feeling in feelings:
            choice= single_selection_screen(win, words_7, feeling_text, feeling)
            writer.writerow([participant_number, 'third', feeling, choice, start_condition])  # Write the iteration number and data
        random.shuffle(feelings2)
        choice = single_selection_screen(win, words_7, feeling_text, feeling)
        writer.writerow([participant_number, 'third', feeling, choice, start_condition])  # Write the iteration number and data
    # Display text on the left side
    display_text(win, esm_others_text)
    # Keep the window open for a few seconds
    wait_for_spacebar()
    # Append rows to the file during the loop
    with open(esm_file_path, mode='a', newline='', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        # loop over different opinions
        random.shuffle(others_opinions)
        for opinion in others_opinions:
            choice= single_selection_screen(win, words_7, others_text, opinion)
            writer.writerow([participant_number, 'third', opinion, choice, start_condition])  # Write the iteration number and data
    # Display text on the left side
    display_text(win, esm_interaction_text)
    # Keep the window open for a few seconds
    wait_for_spacebar()
    # Append rows to the file during the loop
    with open(esm_file_path, mode='a', newline='', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        # loop over different opinions
        random.shuffle(interaction_opinions)
        for interaction in interaction_opinions:
            choice = single_selection_screen(win, words_5, interaction_text, interaction)
            writer.writerow([participant_number, 'third', interaction, choice, start_condition])  # Write the iteration number and data
        choice = single_selection_screen(win, words_person, '', interaction_opinions_person[0])
        writer.writerow([participant_number, 'third', interaction_opinions_person[0], choice, start_condition])  # Write the iteration number and data
        choice = single_selection_screen(win, words_person, '', interaction_opinions_person[1])
        writer.writerow([participant_number, 'third', interaction_opinions_person[1], choice, start_condition])  # Write the iteration number and data
    # Display text on the left side
    display_text(win, esm_activity_text)
    # Keep the window open for a few seconds
    wait_for_spacebar()
    # Append rows to the file during the loop
    with open(esm_file_path, mode='a', newline='', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        # loop over different opinions
        random.shuffle(activity_opinions)
        for activity in activity_opinions:
            choice = single_selection_screen(win, words_7, activity_text, activity)
            writer.writerow([participant_number, 'third', activity, choice, start_condition])  # Write the iteration number and data
    # Display text on the left side
    display_text(win, esm_end_text)
    # Keep the window open till spacebar pressed by the experimentator
    wait_for_spacebar()

# Display block start name
display_text(win, text_block2and4)
wait_for_spacebar()
core.wait(3)
# tg block 4
with open(tg_file_path, mode='a', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)
    if start_condition == "fair":
        multiplier = 0.3
        min_return = 0.0
        max_return = 0.3
        condition = 'unfair'
    elif start_condition == "unfair":
        multiplier = 1.3
        min_return = 1.0
        max_return = 1.5
        condition = 'fair'
    else:
        raise ValueError("Mode must be 'fair' or 'unfair'.")
    for i in range(TG_trials):
        # Display the investment prompt
        investment_text = f'Masz w tej chwili {max_investment_p:.2f}\n\n\nIlę chciałabyś/byś zainwestować?\n\n\nWciśnij ENTER by potwierdzić'
        investment_p, rt = tg_invest(win, prompt_text=investment_text, min_investment=min_investment_p, max_investment=max_investment_p)

        # Calculate the return, clamping it to the specified range
        investment_return = 3*investment_p
        display_text(win, f'Inwestycja została pomnożona trzykrotnie i wynosi {investment_return:.2f}.\n\n\nWciśnij SPACE, aby się dowiedzieć ile powiernik zdecydował się Ci zwrócić.')
        wait_for_spacebar()
        display_text(win,f'Inwestycja została pomnożona trzykrotnie i wynosi {investment_return:.2f}.\n\n\nWciśnij SPACE, aby się dowiedzieć ile powiernik zdecydował się Ci zwrócić.\n\n Poczekaj na decyzje swojego powiernika')
        # Generate a random float between 3 and 8 seconds
        delay = random.uniform(5, 10)
        # Wait for the random delay
        core.wait(delay)

        # Adjust the multiplier based on the investment compared to the previous one
        if previous_investment is not None:
            if investment_p < previous_investment:
                multiplier += 0.1  # Increase multiplier
            elif investment_p > previous_investment:
                multiplier -= 0.1  # Decrease multiplier

        # Display the return breakdown
        return_p = tg_return(win, return_text=return_text_p, investment=investment_p, multiplier=multiplier)
        wait_for_spacebar()

        # Store the current investment for comparison in the next iteration
        previous_investment = investment_p
        writer.writerow([participant_number, condition , investment_p, investment_return, multiplier,return_p, max_investment_p, rt])  # Write the header row

# appraisal 4
if appraisal:
    ### appraisal 3
    # Display text on the left side
    display_text(win, esm_start_text)
    # Keep the window open for a few seconds
    wait_for_spacebar()
    # Append rows to the file during the loop
    with open(esm_file_path, mode='a', newline='', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        # loop over different feelings
        random.shuffle(feelings)
        for feeling in feelings:
            choice= single_selection_screen(win, words_7, feeling_text, feeling)
            writer.writerow([participant_number, 'fourth', feeling, choice, condition])  # Write the iteration number and data
        random.shuffle(feelings2)
        for feeling in feelings2:
            choice = single_selection_screen(win, words_7, feeling_text, feeling)
            writer.writerow([participant_number, 'fourth', feeling, choice, condition])  # Write the iteration number and data
    # Display text on the left side
    display_text(win, esm_others_text)
    # Keep the window open for a few seconds
    wait_for_spacebar()
    # Append rows to the file during the loop
    with open(esm_file_path, mode='a', newline='', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        # loop over different opinions
        random.shuffle(others_opinions)
        for opinion in others_opinions:
            choice= single_selection_screen(win, words_7, others_text, opinion)
            writer.writerow([participant_number, 'fourth', opinion, choice, condition])  # Write the iteration number and data
    # Display text on the left side
    display_text(win, esm_interaction_text)
    # Keep the window open for a few seconds
    wait_for_spacebar()
    # Append rows to the file during the loop
    with open(esm_file_path, mode='a', newline='', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        # loop over different opinions
        random.shuffle(interaction_opinions)
        for interaction in interaction_opinions:
            choice = single_selection_screen(win, words_5, interaction_text, interaction)
            writer.writerow([participant_number, 'fourth', interaction, choice, condition])  # Write the iteration number and data
        choice = single_selection_screen(win, words_person, '', interaction_opinions_person[0])
        writer.writerow([participant_number, 'fourth', interaction_opinions_person[0], choice, condition])  # Write the iteration number and data
        choice = single_selection_screen(win, words_person, '', interaction_opinions_person[1])
        writer.writerow([participant_number, 'fourth', interaction_opinions_person[1], choice, condition])  # Write the iteration number and data
    # Display text on the left side
    display_text(win, esm_activity_text)
    # Keep the window open for a few seconds
    wait_for_spacebar()
    # Append rows to the file during the loop
    with open(esm_file_path, mode='a', newline='', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        # loop over different opinions
        random.shuffle(activity_opinions)
        for activity in activity_opinions:
            choice = single_selection_screen(win, words_7, activity_text, activity)
            writer.writerow([participant_number, 'fourth', activity, choice, condition])  # Write the iteration number and data
    # Display text on the left side
    display_text(win, esm_end_text)
    # Keep the window open till spacebar pressed by the experimentator
    wait_for_spacebar()
