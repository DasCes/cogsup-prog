"""
Exercise 1: Superimposed objects
In Assignments/Exercises, you will find a python script called square.py. Based on the example script above (circle.py), create a script that displays a fixation cross inside a blue square of length 50 for half a second, then removes the fixation cross and displays only the blue square of length 50 until a key is pressed.

Hints:

You might want to have a look at expyriment's stimuli.Rectangle documentation: the color of the square can be set when initializing the object (note that expyriment uses UK spelling, so use colour instead of color)
Mind the arguments you pass to present
"""

# Import the main modules of expyriment
from expyriment import design, control, stimuli
control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Square")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# Create a fixation cross (color, size, and position will take on default values)
fixation = stimuli.FixCross() # At this stage the fixation cross is not yet rendered

# Create a 50px-radius circle
square = stimuli.Rectangle(size=(50,50), colour='blue')

# Start running the experiment
control.start(subject_id=1)

# Present the fixation cross with rectalgle
# square.present(clear=True, update=False)
# fixation.present(clear=False, update=True)

fixation.present(clear=True, update=False)
square.present(clear=False, update=True)


# Leave it on-screen for 500 ms
exp.clock.wait(500)


# square.present(clear=False, update=True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()