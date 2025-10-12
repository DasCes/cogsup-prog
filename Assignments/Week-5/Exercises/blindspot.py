"""
this is supposed to be run withot the develop mode...since the size of the screen its too small to see the cross if ran
in the develop mode
"""


from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK
from expyriment.misc.constants import K_SPACE, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE

""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
# control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
def make_circle(r, pos=(0,0)):
    c = stimuli.Circle(r, position=pos, anti_aliasing=10)
    c.preload()
    return c


def adjust_circle(circle, key, displacement):
    if key == K_UP:
        circle.move((0, displacement))
    if key == K_DOWN:
        circle.move((0, -displacement))
    if key == K_LEFT:
        circle.move((-displacement, 0))
    if key == K_RIGHT:
        circle.move((displacement, 0))



def run_trial():


    exp.data.add_variable_names(["eye", "key_pressed", "raidus", "x_cord", "y_cord"])

    side_text = stimuli.TextScreen(
        heading="Blind Spot Experiment",
        text="Instructions:\n\n"
             "1. Decide what eye you want to test\n"
             "2. Press l or r\n"
    )
    side_text.present()
    side, rt = exp.keyboard.wait(keys=[ord('l'), ord('r')])

    print("side", side)
    side_data = "left"


    if side == ord('l'):
        fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=[-500, 0])
        fixation.preload()
    else:
        fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=[500, 0])
        fixation.preload()
        side_data = "right"



    instruction_text = stimuli.TextScreen(
        heading="Blind Spot Experiment",
        text="Instructions:\n\n"
             "1. Cover your LEFT eye\n"
             "2. Look at the fixation cross (+) with your RIGHT eye\n"
             "3. Use arrow keys to move the circle\n"
             "4. Press 1 to make circle smaller, 2 to make larger\n"
             "5. Adjust until the circle disappears\n"
             "6. Press SPACE when done\n\n"
             "Press SPACE to start"
    )
    instruction_text.present()
    exp.keyboard.wait(keys=[K_SPACE])



    radius = 75
    circle = make_circle(radius)
    displacement = 10

    fixation.present(True, False)
    circle.present(False, True)

    sizes_radius = {ord('1'): -3, ord('2'): +3} #here i want to set the size of increment or decrement of radius and pass it in the check inside while
    useful_keys = [K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE] + list(sizes_radius.keys())

    exp.data.add([side_data, 0, radius, 0, 0])

    # print(useful_keys)
    #TODO place here i think a loop where you get input for move the circle
    while True:
        key, rt = exp.keyboard.wait(keys=useful_keys) #i also cant do this... i though that is better if i wait just for the key i need and not for 'a..6..etc'
        print(f"key: {key}, rt:{rt}")
        exp.data.add([side_data, key, circle.radius, circle.position[0], circle.position[1]])

        if key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
            adjust_circle(circle, key, displacement)
            fixation.present(clear=True, update=False)
            circle.present(clear=False, update=True)

        elif key == K_SPACE:
            control.end()

        elif key in sizes_radius:
            radius = max(5, radius+sizes_radius[key]) #here i had to put max since if the circle goes to smaller the program crash... i have to have a minimum radius
            circle = make_circle(radius)
            fixation.present(clear=True, update=False)
            circle.present(clear=False, update=True)


control.start(subject_id=1)

run_trial()
    
control.end()




"""
Variation and experiment


you can use also ord() instead of import K_SPACE, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE from
expyriment.misc.constants
The idea is that ord('character') converts a character (string) to its ASCII code (integer)
SO, for example i can write  

# above i cant use ord with arrows since they are special keys
"""