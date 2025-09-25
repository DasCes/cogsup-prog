from expyriment import design, control, stimuli
exp = design.Experiment(name="display-edges", background_colour=(128, 128, 128))

control.set_develop_mode()
control.initialize(exp)


bg = exp.background_colour
w, h = exp.screen.size
squareSize = (w//100)*25
circle_radius = (w//100)*5
ss = squareSize//2

square_corners = [[ss,ss],[ss,-ss],[-ss,ss],[-ss,-ss]]

square = stimuli.Rectangle(size=(squareSize, squareSize), colour=(bg))
rightUp_circle = stimuli.Circle(radius=circle_radius, colour=("black"), position=(square_corners[0][0], square_corners[0][1]))
rightDown_circle = stimuli.Circle(radius=circle_radius, colour=("white"), position=(square_corners[1][0], square_corners[1][1]))
leftUp_circle = stimuli.Circle(radius=circle_radius, colour=("black"), position=(square_corners[2][0], square_corners[2][1]))
leftDown_circle = stimuli.Circle(radius=circle_radius, colour=("white"), position=(square_corners[3][0], square_corners[3][1]))

control.start(subject_id=1)


rightUp_circle.present(clear=True, update=False)
rightDown_circle.present(clear=False, update=False)
leftUp_circle.present(clear=False, update=False)
leftDown_circle.present(clear=False, update=False)
square.present(clear=False, update=True)

exp.keyboard.wait()
control.end()