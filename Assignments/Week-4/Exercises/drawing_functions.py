"""
Exercise 3: Drawing functions
Open drawing_functions.py and implement the following functions:

 - load: preload the stimuli passed as input
 - timed_draw: draw a list of (preloaded) stimuli on-screen, return the time it took to execute the drawing
 - present_for: draw and keep stimuli on-screen for time t in ms (be mindful of edge cases!)

Once you've implemented all three functions, run drawing_functions.py. If you implemented the functions
correctly, the program will print "Well done!". Otherwise, it will show you the measured durations.
"""

from expyriment import design, control, stimuli
import random


def load(stims):
    for stimulus in stims:
        stimulus.preload()


def timed_draw(exp, stims):
    # Draw to canvas
    time_before_draw = exp.clock.time

    exp.screen.clear()  # Clear the screen first!
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    time_after_draw = exp.clock.time

    return time_after_draw - time_before_draw


def present_for(exp, stims, t=1000):
    dur = timed_draw(exp, stims)

    remaining_time = t - dur
    if remaining_time > 0:
        exp.clock.wait(remaining_time)


""" Test functions """
if __name__ == "__main__":
    exp = design.Experiment()

    control.set_develop_mode()
    control.initialize(exp)

    # defined the fixationCross stimulus and load it
    fixation = stimuli.FixCross()
    load([fixation])

    # define the squares stimuli and load them
    n = 20
    positions = [(random.randint(-300, 300), random.randint(-300, 300)) for _ in range(n)]
    squares = [stimuli.Rectangle(size=(50, 50), position=pos) for pos in positions]
    load(squares)

    durations = []
    t0 = exp.clock.time
    for square in squares:
        if not square.is_preloaded:
            print("Preloading function not implemented correctly.")
        stims = [fixation, square]
        present_for(exp, stims, 500)  # Pass exp here!
        t1 = exp.clock.time
        durations.append(t1 - t0)
        t0 = t1

    print(f"The presentation process at screen takes: {durations} seconds")

    control.end()