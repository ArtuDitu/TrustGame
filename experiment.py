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

# display instructions
display_text(win, instructions1)
wait_for_spacebar()



### appraisal start
# Display text on the left side
display_text(win, esm_start_text)
# Keep the window open for a few seconds
wait_for_spacebar()
# open  a file to store esm data
with open(esm_file_path, mode='w', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["participant", "esm", 'question', 'answer_left', 'answer_right' ])  # Write the header row

# Append rows to the file during the loop
with open(esm_file_path, mode='a', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)
    # loop over different feelings
    random.shuffle(feelings)
    for feeling in feelings:
        choice= single_selection_screen(win, words_7, feeling_text, feeling)
        writer.writerow([participant_number, 'before', feeling, choice])  # Write the iteration number and data
    random.shuffle(feelings2)
    for feeling in feelings2:
        choice = single_selection_screen(win, words_7, feeling_text, feeling)
        writer.writerow([participant_number, 'before', feeling, choice])  # Write the iteration number and data

# Display text on the left side
display_text(win, esm_end_text)
# Keep the window open till spacebar pressed by the experimentator
wait_for_spacebar()

# open  a file to store esm data
with open(tg_file_path, mode='w', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["participant", "condition", 'investment', 'investment_return','multiplier','return'])  # Write the header row


# tg block 1
# Loop through the specified number of iterations

with open(tg_file_path, mode='a', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)
    for i in range(TG_trials):
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
        writer.writerow([participant_number, start_condition , investment_p, investment_return, multiplier,return_p])  # Write the header row


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
        writer.writerow([participant_number, 'first', feeling, choice])  # Write the iteration number and data
    random.shuffle(feelings2)
    choice = single_selection_screen(win, words_7, feeling_text, feeling)
    writer.writerow([participant_number, 'first', feeling, choice])  # Write the iteration number and data
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
        writer.writerow([participant_number, 'first', opinion, choice])  # Write the iteration number and data
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
        writer.writerow([participant_number, 'first', interaction, choice])  # Write the iteration number and data
    choice = single_selection_screen(win, words_person, '', interaction_opinions_person[0])
    writer.writerow([participant_number, 'first', interaction_opinions_person[0], choice])  # Write the iteration number and data
    choice = single_selection_screen(win, words_person, '', interaction_opinions_person[1])
    writer.writerow([participant_number, 'first', interaction_opinions_person[1], choice])  # Write the iteration number and data
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
        writer.writerow([participant_number, 'first', activity, choice])  # Write the iteration number and data
# Display text on the left side
display_text(win, esm_end_text)
# Keep the window open till spacebar pressed by the experimentator
wait_for_spacebar()

# tg block 2
with open(tg_file_path, mode='a', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)
    for i in range(TG_trials):
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
        writer.writerow([participant_number, condition , investment_p, investment_return, multiplier,return_p])  # Write the header row


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
        writer.writerow([participant_number, 'second', feeling, choice])  # Write the iteration number and data
    random.shuffle(feelings2)
    choice = single_selection_screen(win, words_7, feeling_text, feeling)
    writer.writerow([participant_number, 'second', feeling, choice])  # Write the iteration number and data
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
        writer.writerow([participant_number, 'second', opinion, choice])  # Write the iteration number and data
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
        writer.writerow([participant_number, 'second', interaction, choice])  # Write the iteration number and data
    choice = single_selection_screen(win, words_person, '', interaction_opinions_person[0])
    writer.writerow([participant_number, 'second', interaction_opinions_person[0], choice])  # Write the iteration number and data
    choice = single_selection_screen(win, words_person, '', interaction_opinions_person[1])
    writer.writerow([participant_number, 'second', interaction_opinions_person[1], choice])  # Write the iteration number and data
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
        writer.writerow([participant_number, 'second', activity, choice])  # Write the iteration number and data
# Display text on the left side
display_text(win, esm_end_text)
# Keep the window open till spacebar pressed by the experimentator
wait_for_spacebar()


# tg block 3
with open(tg_file_path, mode='a', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)
    for i in range(TG_trials):
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
        writer.writerow([participant_number, start_condition , investment_p, investment_return, multiplier,return_p])  # Write the header row

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
        writer.writerow([participant_number, 'third', feeling, choice])  # Write the iteration number and data
    random.shuffle(feelings2)
    choice = single_selection_screen(win, words_7, feeling_text, feeling)
    writer.writerow([participant_number, 'third', feeling, choice])  # Write the iteration number and data
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
        writer.writerow([participant_number, 'third', opinion, choice])  # Write the iteration number and data
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
        writer.writerow([participant_number, 'third', interaction, choice])  # Write the iteration number and data
    choice = single_selection_screen(win, words_person, '', interaction_opinions_person[0])
    writer.writerow([participant_number, 'third', interaction_opinions_person[0], choice])  # Write the iteration number and data
    choice = single_selection_screen(win, words_person, '', interaction_opinions_person[1])
    writer.writerow([participant_number, 'third', interaction_opinions_person[1], choice])  # Write the iteration number and data
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
        writer.writerow([participant_number, 'third', activity, choice])  # Write the iteration number and data
# Display text on the left side
display_text(win, esm_end_text)
# Keep the window open till spacebar pressed by the experimentator
wait_for_spacebar()

# tg block 4
with open(tg_file_path, mode='a', newline='', encoding = 'utf-8') as file:
    writer = csv.writer(file)
    for i in range(TG_trials):
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
        writer.writerow([participant_number, condition , investment_p, investment_return, multiplier,return_p])  # Write the header row


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
        writer.writerow([participant_number, 'fourt', feeling, choice])  # Write the iteration number and data
    random.shuffle(feelings2)
    choice = single_selection_screen(win, words_7, feeling_text, feeling)
    writer.writerow([participant_number, 'third', feeling, choice])  # Write the iteration number and data
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
        writer.writerow([participant_number, 'third', opinion, choice])  # Write the iteration number and data
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
        writer.writerow([participant_number, 'third', interaction, choice])  # Write the iteration number and data
    choice = single_selection_screen(win, words_person, '', interaction_opinions_person[0])
    writer.writerow([participant_number, 'third', interaction_opinions_person[0], choice])  # Write the iteration number and data
    choice = single_selection_screen(win, words_person, '', interaction_opinions_person[1])
    writer.writerow([participant_number, 'third', interaction_opinions_person[1], choice])  # Write the iteration number and data
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
        writer.writerow([participant_number, 'third', activity, choice])  # Write the iteration number and data
# Display text on the left side
display_text(win, esm_end_text)
# Keep the window open till spacebar pressed by the experimentator
wait_for_spacebar()