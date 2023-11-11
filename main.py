from DSEngine import *
from pygame import Vector2
import sys

window = Window(fps=120, size=(1280, 720), bg=(100, 100, 100))
carpet = Image2D("Test.png")
death = Rect2D(1, position=Vector2(0, 620), size=Vector2(1280, 720), offset=Vector2(0, 100))
carpet.init(window)
death.init(window)
while window.running:
    #if not carpet.moving_towards
    carpet.move(Vector2(0.0, 5.0))
    if carpet.is_colliding_with(death):
        sys.exit(0)
    keys = window.frame()
    if keys[key_to_scancode(" ")]:
        carpet.move(Vector2(0.0, -20.0))
