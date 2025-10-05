"""
Exercise 2: Timing puzzle
Have a look at timing_puzzle.py and try to predict what will happen. For how long
will the fixation cross stay on-screen? Run the script to find out. After figuring
out why it does not work, fix it such that the fixation cross is displayed for one second.
"""

"""
Pipeline explanation
as explain on the slides in order to present the fixation cross and the text
for exactly 1 second we need to wait not 1 second but one second minus
the time the present process spent
I check this plotting the duration

The second pipile adrress the problem using the second solution as propsed
on the slide
"""

from expyriment import design, control, stimuli

exp = design.Experiment(name="timing puzzle")

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
text = stimuli.TextLine("Fixation removed")

t0 = exp.clock.time
fixation.present()
dt = exp.clock.time - t0
exp.clock.wait(1000 - dt)
# in this way I can display the cros for exactly one second

t1 = exp.clock.time
fix_cross_duration = (t1 - t0)/1000

t0 = exp.clock.time
text.present()  #quando qui faccio text.present() sto di fatto pulendo la scena precedente e mostrando text
dt = exp.clock.time - t0
exp.clock.wait(1000 - dt)


units = "second" if fix_cross_duration == 1.0 else "seconds"
duration_cross_text = f"Fixation was present on the screen for {fix_cross_duration} {units}."


text2 = stimuli.TextLine(duration_cross_text)
text2.present()
exp.keyboard.wait()

control.end()


"""
if i try with this pipeline (in which i preload the stimuli) i cant find the expected result of have the cross
fixation for exactly 1 second...this the results
1) if I run on develop_mode() i obtain 1.022-1.0025 on average
2) if I run on full-screen mode i obtain 1.008 which is better but not 1s
These results are better compared to run the pipeline without the preload
but as said the improvement is 10ms on average
"""
"""
from expyriment import design, control, stimuli

exp = design.Experiment(name="timing puzzle")

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
text = stimuli.TextLine("Fixation removed")

fixation.preload()
text.preload()

t0 = exp.clock.time
fixation.present()
exp.clock.wait(1000)
t1 = exp.clock.time
fix_cross_duration = (t1 - t0)/1000


units = "second" if fix_cross_duration == 1.0 else "seconds"
duration_cross_text = f"Fixation was present on the screen for {fix_cross_duration} {units}."


text2 = stimuli.TextLine(duration_cross_text)
text2.present()
exp.keyboard.wait()

control.end()
"""