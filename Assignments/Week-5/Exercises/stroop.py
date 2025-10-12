"""
Stroop Effect Experiment
20 trials divided into 2 blocks (10 trials each)
Participants decide if word meaning and text color match
"""

from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, C_RED, C_BLUE, C_GREEN
import random

""" Global settings """
exp = design.Experiment(name="Stroop Effect", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.initialize(exp)

""" Color mappings """
COLORS = {
    'red': C_RED,
    'blue': C_BLUE,
    'green': C_GREEN,
}

COLOR_NAMES = list(COLORS.keys())

# Response keys: m for match, n for mismatch
MATCH_KEY = ord('m')
MISMATCH_KEY = ord('n')


def create_trials(n_trials):
    """Create a list of trials with random word/color combinations"""
    trials = []

    for i in range(n_trials):
        # Randomly decide if trial is match or mismatch
        trial_type = random.choice(['match', 'mismatch'])

        # Choose word
        word = random.choice(COLOR_NAMES)

        # Choose color based on trial type
        if trial_type == 'match':
            color = word  # Color matches word
        else:
            # Color doesn't match word
            possible_colors = [c for c in COLOR_NAMES if c != word]
            color = random.choice(possible_colors)

        trials.append({
            'trial_type': trial_type,
            'word': word,
            'color': color
        })

    return trials


def show_instructions(block_num):
    """Show instructions before each block"""
    instruction_text = stimuli.TextScreen(
        heading=f"Stroop Effect - Block {block_num}",
        text="Instructions:\n\n"
             "You will see color words displayed on the screen.\n"
             "Your task is to decide if the WORD MEANING matches the TEXT COLOR.\n\n"
             "Press 'M' if they MATCH\n"
             "Press 'N' if they DO NOT match\n\n"
             "Respond as quickly and accurately as possible.\n\n"
             "Press SPACE to start"
    )
    instruction_text.present()
    exp.keyboard.wait(keys=[32])  # Wait for spacebar


def show_feedback(is_correct):
    """Show positive or negative feedback"""
    if is_correct:
        feedback = stimuli.TextLine("CORRECT!", text_size=50, text_colour=C_GREEN)
    else:
        feedback = stimuli.TextLine("WRONG!", text_size=50, text_colour=C_RED)

    feedback.present()
    exp.clock.wait(1000)  # Show for 1 second


def run_trial(trial, block_num, trial_num):
    """Run a single trial"""

    # Fixation cross (500 ms)
    fixation = stimuli.FixCross(size=(50, 50), line_width=4)
    fixation.present()
    exp.clock.wait(500)

    # Present word with colored text
    word_stimulus = stimuli.TextLine(
        trial['word'].upper(),
        text_size=80,
        text_colour=COLORS[trial['color']]
    )
    word_stimulus.present()

    # Wait for response (self-paced)
    key, rt = exp.keyboard.wait(keys=[MATCH_KEY, MISMATCH_KEY])

    # Determine if response was correct
    if trial['trial_type'] == 'match':
        correct_key = MATCH_KEY
    else:
        correct_key = MISMATCH_KEY

    is_correct = (key == correct_key)
    accuracy = 1 if is_correct else 0

    # Show feedback
    show_feedback(is_correct)

    # Save data
    exp.data.add([
        block_num,
        trial_num,
        trial['trial_type'],
        trial['word'],
        trial['color'],
        rt,
        accuracy
    ])

    return accuracy


def run_experiment():
    """Run the complete experiment"""

    # Set up data variable names
    exp.data.add_variable_names([
        "block",
        "trial_number",
        "trial_type",
        "word_meaning",
        "text_color",
        "RT",
        "accuracy"
    ])

    # Create all trials (20 total)
    all_trials = create_trials(20)

    # Divide into 2 blocks of 10 trials each
    blocks = [all_trials[:10], all_trials[10:]]

    # Run each block
    for block_num, block_trials in enumerate(blocks, start=1):
        # Show instructions before block
        show_instructions(block_num)

        # Run trials in the block
        for trial_num, trial in enumerate(block_trials, start=1):
            run_trial(trial, block_num, trial_num)

        # Show break message between blocks (except after last block)
        if block_num < 2:
            break_text = stimuli.TextScreen(
                heading="Break",
                text=f"You have completed block {block_num} of 2.\n\n"
                     "Take a short break.\n\n"
                     "Press SPACE when ready to continue."
            )
            break_text.present()
            exp.keyboard.wait(keys=[32])

    # End experiment
    end_text = stimuli.TextScreen(
        heading="Thank You!",
        text="The experiment is complete.\n\n"
             "Thank you for your participation!\n\n"
             "Press SPACE to exit."
    )
    end_text.present()
    exp.keyboard.wait(keys=[32])


# Start experiment
control.start(subject_id=1)

run_experiment()

control.end()