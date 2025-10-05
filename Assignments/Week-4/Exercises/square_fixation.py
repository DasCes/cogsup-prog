"""
Exercise 1: Double buffer
Run square_fixation.py. The script should plot a fixation inside an empty
square but it does something differently. Try to understand why it does not work, then fix it.
"""

"""
Pipeline explanation
the code has given was updating the fixation stimuli to early, to fix it
we need to set Flase the parameter update on fixation.present and the update
only at the last element we call on the present() function 
"""

from expyriment import design, control, stimuli

exp = design.Experiment(name="Square")

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
square = stimuli.Rectangle(size=(100, 100), line_width=5)

control.start(subject_id=1)

fixation.present(clear=True, update=False)
#clear=True → Pulisce lo schermo (sfondo grigio o nero)
# Disegna la croce nel buffer nascosto
# update=False → NON mostrare ancora!
exp.clock.wait(500)

square.present(clear=False, update=True)
# clear=False → NON pulire lo schermo (mantiene la croce)
# Disegna il quadrato sopra la croce
# update=True → Mostra IMMEDIATAMENTE
exp.keyboard.wait()

control.end()