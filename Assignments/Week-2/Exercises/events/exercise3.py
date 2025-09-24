"""
## Exercise 3: Causal perception
### 3A: Michottean launching
Check out the first video at [this link](https://www.jfkominsky.com/demos.html), under **Launching and simple non-causal events**. Duplicate`two_squares.py` in the same **Assignments/Week-2/Exercises** subfolder and rename it to `launching.py`. Modify the code as follows:
1. Present the two squares side by side for 1 second but modify their positions such that:
    - the red square starts on the left side, 400 pixels left from the center
    - the green square starts at the center
2. Using the ```position``` [attribute](https://docs.expyriment.org/expyriment.stimuli.Rectangle.html#expyriment.stimuli.Rectangle) or the ```move``` [method](https://docs.expyriment.org/expyriment.stimuli.Rectangle.html#expyriment.stimuli.Rectangle.move), animate the left square to move to the left until it reaches the green square. Adjust the speed to approximately match the one in the video.
3. Once the red square reaches the green square, the green square should move to the right, at the same speed and for the same amount of time as the red square.
4. Show this display for 1 second.
5. Add explanatory comments at each step in the script.

**Do you get the impression that the red square causes the green square to move?**

Things to consider:
- How do I move a square to the left at a given speed?
- How do I encode the collision moment between the two squares?
"""