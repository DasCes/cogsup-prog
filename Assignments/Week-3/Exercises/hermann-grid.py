"""
Write a hermann-grid.py program that generates a grid illusion. The program
should have customizable grid parameters controlling the size and color of
the squares, the space between them, the number of rows and number of
columns, and the screen background color.

Hints:

Use paper and pencil to draw the figure
Think how to compute the center of the square in row i and column j
Use nested loops to draw each square one by one
Play around with these parameters and test your perception: What factors does the illusion most depend on?

"""
from expyriment import design, control, stimuli
control.set_develop_mode()


def grid():


    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            square = stimuli.Rectangle(size=(square_size, square_size),
                                       colour=(square_color, position=(square_corners[0][0], square_corners[0][1]))




# Global settings
exp = design.Experiment(name="Kanizsa rectangle")
control.initialize(exp)


grid_size = [3,3] #rows, column
square_size = 30 #in px
square_color = 'Blue' #in words for now
squares_padding = 10 #in px
bg_color = 'white'
w, h = exp.screen.size


#call the creation grid and display grid function


# End the current session and quit expyriment
control.end()
