"""
Exercise 4: Ternus illusion
Write a ternus.py program that generates a Ternus display similar to the program embedded here.
The run_trial function should have parameters for circle radius, inter-stimulus interval (ISI),
and for whether to add color tags to the circles.

Requirements requested by professor

1. The run_trial function should have parameters for
    1.1 circle radius
    1.2 inter-stimulus interval (ISI)
    1.3 add color tags to the circles


2.  When run, the program should present three Ternus displays in succession
    2.1 Element motion without color tags (low ISI)
    2.2 Group motion without color tags (high ISI)
    2.3 Element motion with color tags (high ISI)

3.  Don't forget to preserve the structure of expyriment scripts:
    prof said to make this works (changing from one to other) using space bar
    3.1 Global settings
    3.2 Stimuli generation
    3.3 Trial run

4.  Aim for compact code (80–90 lines)

5.  In the loop for the display (e.g., while True, add a command
    that checks for user input and exits the loop if SPACE was pressed)


Pay attention to how you implement ISI = 0
Since a frame is 16.67 ms, it's best to use frames instead of times. Have the present_for function take as input the number of frames and convert to time in milliseconds internally. This will help you avoid rounding errors or passing in meaningless commands (such as present for 12 milliseconds).
As we’ve seen with canvases, expyriment lets you plot stimuli onto the surface of other stimuli. You can add tags by plotting small circles on the surface of the big ones, but be mindful of two aspects:
The big circles must be preloaded after the plotting of the tags
The positions of the tags must be set relative to the circles on top of which they’re plotted (easier than it sounds)

!!!!!
i do not implement errorExeption controls... expecte number given in input are goods
for example testing with big radius number the code does not work... i mean it works but we cant
see the illusion
if isi is negative it will produce an isi=0 scenario
"""

from expyriment import design, control, stimuli
from expyriment.misc.constants import K_SPACE


def present_for(stims, frames_number):
    """Mostra stimoli per N frames"""
    time_ms = frames_number * (1000/60)  # Più preciso di 16.67


    time_before = exp.clock.time

    exp.screen.clear()
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()

    drawing_time = exp.clock.time - time_before
    remaining = time_ms - drawing_time

    if remaining > 0:
        exp.clock.wait(remaining)


def make_circles(radius, with_tags=False):

    """
    If i understand correctly i need 3 circle for frame.
    I need to finde the position of the cirlce which are based on the radius and
    the distance between the circle (ill do 1/4 of a circle)
    """

    spacing = radius * 2 + radius / 4  # Spaziatura tra cerchi

    # Posizioni: [-2*spacing, -spacing, 0]
    frame1_circles_pos = [(-2*spacing, 0),(-spacing, 0),(0, 0)]

    # Posizioni: [0, spacing, 2*spacing]
    frame2_circles_pos = [(0, 0),(spacing, 0),(2 * spacing, 0)]

    circles_frame1 = [stimuli.Circle(radius, position=pos) for pos in frame1_circles_pos]
    circles_frame2 = [stimuli.Circle(radius, position=pos) for pos in frame2_circles_pos]

    if with_tags:
        add_tags(circles_frame1)
        add_tags(circles_frame2)

    # Preload dopo i tag
    for circle in circles_frame1 + circles_frame2:
        circle.preload()

    return circles_frame1, circles_frame2


def add_tags(circles):
    # add here the small circle inside big circle
    colors = [(255, 14, 0), (27, 232, 4), (54, 30, 3)] #random number

    for circle, color in zip(circles, colors):
        tag = stimuli.Circle(5, position=(0, 0), colour=color)
        tag.plot(circle)


def run_trial(radius, isi, with_tags=False):
    circles_frame1, circles_frame2 = make_circles(radius, with_tags)

    display_frames = 6 #just for have an idea if this is set to 6 means that the
                       # circles will be presented for (frames_number * (1000/60))
                       # which is approsimativamente 100ms (0.1s)

    # here the same code shared in slides basically
    while True:
        # Mostra frame 1
        present_for(circles_frame1, display_frames)

        # ISI
        if isi > 0:
            present_for([], isi) #when pass an empty list mean it will plot nothing

        # Mostra frame 2
        present_for(circles_frame2, display_frames)

        # ISI
        if isi > 0:
            present_for([], isi)

        # Check SPACE
        if exp.keyboard.check(K_SPACE):
            break


if __name__ == "__main__":
    exp = design.Experiment(name="ternus")
    control.set_develop_mode()
    control.initialize(exp)

    # as requested here in the main we can set 3 parmeters:
    #   circle radius --> radius
    #   inter-stimuls interval (ISI) --> isi
    #   color tags variable --> with_tags

    radius = 50

    # 1. Element motion (ISI basso)
    run_trial(radius, isi=1, with_tags=False)

    # 2. Group motion (ISI alto)
    run_trial(radius, isi=6, with_tags=False)

    # 3. Element motion con tags (ISI alto)
    run_trial(radius, isi=6, with_tags=True)

    control.end()