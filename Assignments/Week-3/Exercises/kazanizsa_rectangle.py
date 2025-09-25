from expyriment import design, control, stimuli


def kanizsa_rectangle(aspect_ratio, rectangle_scale, circle_scale):

    exp = design.Experiment(name="kanizsa-rectangle", background_colour=(128, 128, 128))

    control.set_develop_mode()
    control.initialize(exp)

    w, h = exp.screen.size
    bg = exp.background_colour

    base_size = min(w,h) // 4  #dontwant exploding outside screen
    rect_width = int(base_size * rectangle_scale * aspect_ratio)
    rect_height = int(base_size * rectangle_scale)

    circle_radius = int((base_size // 8) * circle_scale)

    corner_x = rect_width // 2
    corner_y = rect_height // 2

    square_corners = [
        [corner_x, corner_y],  # top-right
        [corner_x, -corner_y],  # bottom-right
        [-corner_x, corner_y],  # top-left
        [-corner_x, -corner_y]  # bottom-left
    ]

    print(f"Rectangle size: {rect_width} x {rect_height}")
    print(f"Aspect ratio: {aspect_ratio}")
    print(f"Circle radius: {circle_radius}")
    print(f"Corner positions: {square_corners}")






    rectangle = stimuli.Rectangle(
        size=(rect_width, rect_height),
        colour=bg
    )


    rightUp_circle = stimuli.Circle(radius=circle_radius,colour=(0, 0, 0),position=square_corners[0])
    rightDown_circle = stimuli.Circle(radius=circle_radius,colour=(255, 255, 255),position=square_corners[1])
    leftUp_circle = stimuli.Circle(radius=circle_radius,colour=(0, 0, 0),position=square_corners[2])
    leftDown_circle = stimuli.Circle(radius=circle_radius,colour=(255, 255, 255),position=square_corners[3])

    control.start(subject_id=1)

    rightUp_circle.present(clear=True, update=False)
    rightDown_circle.present(clear=False, update=False)
    leftUp_circle.present(clear=False, update=False)
    leftDown_circle.present(clear=False, update=False)

    rectangle.present(clear=False, update=True)

    # Wait for key press
    exp.keyboard.wait()
    control.end()

if __name__ == "__main__":
    # You can test with different values:
    kanizsa_rectangle(aspect_ratio=1.5, rectangle_scale=1.0, circle_scale=2.2)