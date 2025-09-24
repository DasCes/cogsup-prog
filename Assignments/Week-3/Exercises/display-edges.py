"""
Exercise 1: Screen edges
In Assignments/Exercises, you will find an empty python file called display-edges.py.
Write a script that displays four fully visible squares with red contours (square length: ~5%
of the screen width, line width: 1 pixel) at the screen edges until a key is pressed. The display
must be independent of screen resolution (to check this, run with and without control.set_develop_mode()).
"""

from expyriment import design, control, stimuli

exp = design.Experiment(name="display-edges")

control.set_develop_mode()
control.initialize(exp)

offset = 200
width, height = exp.screen.size
squareSize = 50
print("width, height: ", width, height)

# print(((-width//2)+(squareSize//2)))
# print(((height//2)-squareSize//2))

lefleft_square = stimuli.Rectangle(size=(squareSize, squareSize), colour=(255, 0, 0), position=(((-width//2)+(squareSize//2)), ((height//2)-squareSize//2)))
centerleft_square = stimuli.Rectangle(size=(squareSize, squareSize), colour=(255, 0, 0), position=(((width//2)-(squareSize//2)), ((height//2)-squareSize//2)))
centerright_square = stimuli.Rectangle(size=(squareSize, squareSize), colour=(255, 0, 0), position=(((-width//2)+(squareSize//2)), ((-height//2)+squareSize//2)))
rightright_square = stimuli.Rectangle(size=(squareSize, squareSize), colour=(255, 0, 0), position=(((width//2)-(squareSize//2)), ((-height//2)+squareSize//2)))

control.start(subject_id=1)

lefleft_square.present(clear=True, update=False)
centerleft_square.present(clear=False, update=False)
centerright_square.present(clear=False, update=False)
rightright_square.present(clear=False, update=True)

exp.keyboard.wait()
control.end()

#its broken right now... they are 4 square and not 4 border

"""

Solution by prof
extract sceen coordinates

set size base on them
stim_lengh = width//10
stim_size = (stim_lengh, stim_lengh)


compute edges
edges = []
for x in (-w,w):
    for y in(-h,h):
    
"""