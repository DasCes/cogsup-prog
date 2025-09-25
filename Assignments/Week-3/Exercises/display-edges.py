"""
Exercise 1: Screen edges
In Assignments/Exercises, you will find an empty python file called display-edges.py.
Write a script that displays four fully visible squares with red contours (square length: ~5%
of the screen width, line width: 1 pixel) at the screen edges until a key is pressed. The display
must be independent of screen resolution (to check this, run with and without control.set_develop_mode()).
"""

"""
I've done two version, the V1 is actually my first one... i didn't know that i could use line_width parameter to draw 
empty shape... so i realized the square exercise drawing one red square inside another smalle square with color=backGground
so it looks like a border of red square as well.
But since exist linewidth parameter this way of solve the exercise is not very smart :)
"""


"""
#V1

from expyriment import design, control, stimuli

exp = design.Experiment(name="display-edges")

control.set_develop_mode()
control.initialize(exp)


width, height = exp.screen.size
squareSize = (width//100)*5
inner_square_size = squareSize-1.5 #here i put 1.5 because if i select 1 i cant see some of the red border..idk maybe its a display resolution issue
background_colour = exp.background_colour

#reduce lenght of variable name
w = width
h = height
ss = squareSize
iss = inner_square_size
bg = background_colour
print("screen width: \n", width)
print("screen height: \n", height)

print("square size: ", squareSize)
print("inner square size:", inner_square_size)



#my idea here is to draw two squares, one inside the other, so that the one in the inside is smaller and with the color
#of the background and the back one bigger and with the color of the contours are asked for (red here).
leftUp_square = stimuli.Rectangle(size=(ss, ss), colour=("red"), position=(((-w//2)+(ss//2)), ((h//2)-ss//2)))
leftUp_square_inner = stimuli.Rectangle(size=(iss, iss), colour=(bg), position=(((-w//2)+(ss//2)), ((h//2)-ss//2)))

rightUp_square = stimuli.Rectangle(size=(ss, ss), colour=("red"), position=(((w//2)-(ss//2)), ((h//2)-ss//2)))
rightUp_square_inner = stimuli.Rectangle(size=(iss, iss), colour=(bg), position=(((w//2)-(ss//2)), ((h//2)-ss//2)))

leftDown_square = stimuli.Rectangle(size=(ss, ss), colour=("red"), position=(((-w//2)+(ss//2)), ((-h//2)+ss//2)))
leftDown_square_inner = stimuli.Rectangle(size=(iss, iss), colour=(bg), position=(((-w//2)+(ss//2)), ((-h//2)+ss//2)))

rightDown_square = stimuli.Rectangle(size=(ss, ss), colour=("red"), position=(((w//2)-(ss//2)), ((-h//2)+ss//2)))
rightDown_square_inner = stimuli.Rectangle(size=(iss, iss), colour=(bg), position=(((w//2)-(ss//2)), ((-h//2)+ss//2)))



control.start(subject_id=1)

leftUp_square.present(clear=True, update=False)
leftUp_square_inner.present(clear=False, update=False)
rightUp_square.present(clear=False, update=False)
rightUp_square_inner.present(clear=False, update=False)
leftDown_square.present(clear=False, update=False)
leftDown_square_inner.present(clear=False, update=False)
rightDown_square.present(clear=False, update=False)
rightDown_square_inner.present(clear=False, update=True)

exp.keyboard.wait()
control.end()
"""


#V2 this version is like the one suggested in class... iterate over the four corners of the screen
from expyriment import design, control, stimuli
exp = design.Experiment(name="display-edges")

control.set_develop_mode()
control.initialize(exp)

w, h = exp.screen.size
squareSize = (w//100)*5

w = (w//2) - (squareSize//2)
h = (h//2) - (squareSize//2)
corners = [[w,h],[w,-h],[-w,h],[-w,-h]]

rightUp_square = stimuli.Rectangle(size=(squareSize, squareSize), colour=("red"), line_width=1, position=(corners[0][0], corners[0][1]))
rightDown_square = stimuli.Rectangle(size=(squareSize, squareSize), colour=("red"), line_width=1, position=(corners[1][0], corners[1][1]))
leftUp_square = stimuli.Rectangle(size=(squareSize, squareSize), colour=("red"), line_width=1, position=(corners[2][0], corners[2][1]))
leftDown_square = stimuli.Rectangle(size=(squareSize, squareSize), colour=("red"), line_width=1, position=(corners[3][0], corners[3][1]))

control.start(subject_id=1)

rightUp_square.present(clear=True, update=False)
rightDown_square.present(clear=False, update=False)
leftUp_square.present(clear=False, update=False)
leftDown_square.present(clear=False, update=True)

exp.keyboard.wait()
control.end()
