"""
## Exercise 2: Side-by-side objects
Open `two_squares.py`. Write a script that displays two squares side by side, the left one red, the right one green.
 Leave the fixation cross out. The two squares should be separated by 200 pixels but centered as a whole. Present
 them on-screen until a key is pressed.

Hints:
- By default, stimuli are presented at the center of the screen, so you need to modify this via the ```position```
attribute of shapes
- Shape size can be set when initializing the shape (e.g., ```stimuli.Rectangle(..., position = (x, y))```), or
afterward (e.g., ```square_1.position = (x, y)``` or ```square_1.reposition(x, y)```)
- The position of the shape corresponds to the coordinates at the shape's center
- Expyriment takes (0, 0) to be the center of the screen and measures space in pixel units
"""

from expyriment import design, control, stimuli

exp = design.Experiment(name="Two squares")

control.set_develop_mode()
control.initialize(exp)

offset = 200

left_square = stimuli.Rectangle(size=(50, 50), colour=(255, 0, 0), position=(-offset//2, 0))
right_square = stimuli.Rectangle(size=(50, 50), colour=(0, 255, 0), position=(offset//2, 0))

# since the center of the screen is (0,0)
# The first value (x-coordinate) defines the horizontal position (left/right).
# The second value (y-coordinate) defines the vertical position (up/down).



control.start(subject_id=1)

left_square.present(clear=True, update=False)
right_square.present(clear=False, update=True)
exp.keyboard.wait()

control.end()