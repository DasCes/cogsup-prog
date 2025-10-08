"""
Exercise 4: Ternus illusion
Write a ternus.py program that generates a Ternus display similar to the program embedded here.
The run_trial function should have parameters for circle radius, inter-stimulus interval (ISI),
and for whether to add color tags to the circles.
"""

from expyriment import design, control, stimuli
from expyriment.misc.constants import K_SPACE
from drawing_functions import load, present_for


def present_frames(exp, stims, frames_number):
    """Present stimuli for N frames by converting to milliseconds"""
    time_ms = frames_number * (1000/60)
    present_for(exp, stims, time_ms)


def make_circles(radius, with_tags=False):
    """Create two frames of circles for Ternus display"""
    spacing = radius * 2 + radius / 4

    frame1_pos = [(-2*spacing, 0), (-spacing, 0), (0, 0)]
    frame2_pos = [(0, 0), (spacing, 0), (2*spacing, 0)]

    circles_frame1 = [stimuli.Circle(radius, position=pos) for pos in frame1_pos]
    circles_frame2 = [stimuli.Circle(radius, position=pos) for pos in frame2_pos]

    if with_tags:
        add_tags(circles_frame1)
        add_tags(circles_frame2)

    load(circles_frame1 + circles_frame2)

    return circles_frame1, circles_frame2


def add_tags(circles):
    """Add colored tags to circles"""
    colors = [(255, 14, 0), (27, 232, 4), (54, 30, 3)]
    for circle, color in zip(circles, colors):
        tag = stimuli.Circle(5, position=(0, 0), colour=color)
        tag.plot(circle)


def run_trial(exp, radius, isi, with_tags=False):
    """Run one Ternus trial"""
    circles_frame1, circles_frame2 = make_circles(radius, with_tags)
    display_frames = 6

    while True:
        present_frames(exp, circles_frame1, display_frames)
        if isi > 0:
            present_frames(exp, [], isi)
        present_frames(exp, circles_frame2, display_frames)
        if isi > 0:
            present_frames(exp, [], isi)
        if exp.keyboard.check(K_SPACE):
            break


if __name__ == "__main__":
    exp = design.Experiment(name="ternus")
    control.set_develop_mode()
    control.initialize(exp)

    radius = 50

    # 1. Element motion (low ISI)
    run_trial(exp, radius, isi=1, with_tags=False)

    # 2. Group motion (high ISI)
    run_trial(exp, radius, isi=6, with_tags=False)

    # 3. Element motion with tags (high ISI)
    run_trial(exp, radius, isi=6, with_tags=True)

    control.end()