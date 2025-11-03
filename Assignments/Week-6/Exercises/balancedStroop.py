"""
Exercise 2: Balanced Stroop
Create a new script, stroop_balanced.py, that modifies stroop.py as follows:

have participants decide the color the onscreen word is written in
using the method you think is best, balance the design

    things i have to balance:
    1. trial match and mismatch has to be equals in number
    2. colors also has to be in same number
    3. words same numebrs
    4. combination of colors and words equally also here

    so
    4 words x 4 color ill have 16 possibilities
    ill shuffle to repeat till the trials number required 128

extend the Stroop to 128 trials in total, divided into 8 equally-sized blocks
"""

from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, C_RED, C_BLUE, C_GREEN
import random
import itertools

""" Global settings """
exp = design.Experiment(name="Balanced Stroop Effect", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.initialize(exp)
control.set_develop_mode()

""" Color mappings """
COLORS = {
    'red': C_RED,
    'blue': C_BLUE,
    'green': C_GREEN,
    'orange': (255, 165, 0),
}

COLOR_NAMES = list(COLORS.keys())

# now the kesy for colors
RESPONSE_KEYS = {
    ord('r'): 'red',
    ord('b'): 'blue',
    ord('g'): 'green',
    ord('o'): 'orange'
}


N_BLOCKS = 8
N_TRIALS_IN_BLOCK = 16
TOTAL_TRIALS = 128


def create_balanced_trials(n_trials):
    """Create balanced congruent and incongruent trials"""

    # Congruent trials: word matches color (4 possibilities)
    # these are red-RED, blue-BLUE, green-GREEN, orange-ORANGE
    congruent_trials = [(color, color) for color in COLOR_NAMES]

    # Incongruent trials: word doesn't match color (12 possibilities)
    # eg. red-BLUE, red-GREEN, red-ORANGE, blue-RED, blue-GREEN, etc.
    incongruent_trials = [(word, color) for word in COLOR_NAMES
                          for color in COLOR_NAMES if word != color]

    # Calculate how many of each type we need for 50/50 split
    # so basicly 64 will be congruents and 64 incongruent
    n_per_type = n_trials // 2

    trials = []

    # Add congruent trials (repeat to get n_per_type trials)
    repeats_congruent = n_per_type // len(congruent_trials)
    for _ in range(repeats_congruent):
        for word, color in congruent_trials:
            trials.append({
                'trial_type': 'congruent',
                'word': word,
                'color': color,
                'correct_key': ord(color[0])
            })

    # Add incongruent trials (repeat to get n_per_type trials)
    repeats_incongruent = n_per_type // len(incongruent_trials)
    remainder = n_per_type % len(incongruent_trials)

    for _ in range(repeats_incongruent):
        for word, color in incongruent_trials:
            trials.append({
                'trial_type': 'incongruent',
                'word': word,
                'color': color,
                'correct_key': ord(color[0])
            })

    # Add remainder incongruent trials if needed
    if remainder > 0:
        remaining = random.sample(incongruent_trials, remainder)
        for word, color in remaining:
            trials.append({
                'trial_type': 'incongruent',
                'word': word,
                'color': color,
                'correct_key': ord(color[0])
            })

    random.shuffle(trials)
    return trials


def show_instructions(block_num):
    """Show instructions before each block"""
    instruction_text = stimuli.TextScreen(
        heading=f"Balanced Stroop Effect - Block {block_num}",
        text="Instructions:\n\n"
             "You will see color words displayed on the screen.\n"
             "Your task is to correctly defined the TEXT COLOR.\n\n"
             "Press 'R' if red\n"
             "Press 'B' if red\n"
             "Press 'G' if red\n"
             "Press 'O' if red\n"
             "Respond as quickly and accurately as possible.\n\n"
             "Press SPACE to start"
    )
    instruction_text.present()
    exp.keyboard.wait(keys=[32])  # Wait for spacebar


def show_feedback(is_correct):
    """Show positive or negative feedback"""
    if is_correct:
        feedback = stimuli.TextLine("CORRECT!", text_size=50, text_colour=C_BLACK)
    else:
        feedback = stimuli.TextLine("WRONG!", text_size=50, text_colour=C_BLACK)

    feedback.present()
    exp.clock.wait(1000)


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
    key, rt = exp.keyboard.wait(keys=list(RESPONSE_KEYS.keys()))

    response_color = RESPONSE_KEYS[key]
    is_correct = (response_color == trial['color'])
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

    all_trials = create_balanced_trials(TOTAL_TRIALS)
    blocks = [all_trials[i:i+N_TRIALS_IN_BLOCK] for i in range(0, TOTAL_TRIALS, N_TRIALS_IN_BLOCK)]


    # Run each block
    for block_num, block_trials in enumerate(blocks, start=1):
        # Show instructions before block
        show_instructions(block_num)

        # Run trials in the block
        for trial_num, trial in enumerate(block_trials, start=1):
            run_trial(trial, block_num, trial_num)

        # Show break message between blocks (except after last block)
        if block_num < N_BLOCKS:
            break_text = stimuli.TextScreen(
                heading="Break",
                text=f"You have completed block {block_num} of {N_BLOCKS}.\n\n"
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

# works correctly