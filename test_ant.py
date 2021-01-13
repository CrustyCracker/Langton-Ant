from ant import Langton_Ant
import pytest

def test_change_direction_left():
    ant = Langton_Ant(150, 150)
    direction = ant._new_direction_random(['up', 'down', 'right'])
    assert direction == 'left'



def test_step_1x1_map():
    ant = Langton_Ant(1, 1)
    assert ant.xpos() == 0
    assert ant.xpos() == 0
    assert ant.step(0) == 255
    assert ant.step(255) == 0
