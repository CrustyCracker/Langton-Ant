from ant import Langton_Ant
import pytest


def test_ant_init():
    width = 100
    height = 200
    ant = Langton_Ant(width, height)
    assert ant.map_height() == 200
    assert ant.map_width() == 100
    assert ant.xpos() == 50
    assert ant.ypos() == 100
    assert ant.direction() in ['up', 'right', 'down', 'left']



def test_get_illegal_directions_topleft():
    width = 100
    height = 200
    ant = Langton_Ant(width, height)
    ant._xpos = 0
    ant._ypos = 0
    assert ant._get_illegal_directions() == ['left', 'up']


def test_get_illegal_directions_topright():
    width = 100
    height = 200
    ant = Langton_Ant(width, height)
    ant._xpos = width - 1
    ant._ypos = 0
    assert ant._get_illegal_directions() == ['right', 'up']


def test_get_illegal_directions_downright():
    width = 100
    height = 200
    ant = Langton_Ant(width, height)
    ant._xpos = width - 1
    ant._ypos = height - 1
    assert ant._get_illegal_directions() == ['right', 'down']


def test_get_illegal_directions_downleft():
    width = 100
    height = 200
    ant = Langton_Ant(width, height)
    ant._xpos = 0
    ant._ypos = height - 1
    assert ant._get_illegal_directions() == ['left', 'down']


def test_step_1x1_map():
    ant = Langton_Ant(1, 1)
    assert ant.xpos() == 0
    assert ant.xpos() == 0
    assert ant.step(0) == 255
    assert ant.step(255) == 0


def test_step_normal_map_step_black():
    width = 100
    height = 200
    ant = Langton_Ant(width, height)
    assert ant.map_height() == 200
    assert ant.map_width() == 100
    assert ant.xpos() == 50
    assert ant.ypos() == 100
    ant._direction = 'up'
    ant.step(0)
    assert ant.direction() == "right"
    assert ant.xpos() == 51
    assert ant.ypos() == 100
    ant.step(0)
    assert ant.direction() == "down"
    assert ant.xpos() == 51
    assert ant.ypos() == 101
    ant.step(0)
    assert ant.direction() == "left"
    assert ant.xpos() == 50
    assert ant.ypos() == 101
    ant.step(0)
    assert ant.direction() == "up"
    assert ant.xpos() == 50
    assert ant.ypos() == 100


def test_step_normal_map_step_white():
    width = 100
    height = 200
    ant = Langton_Ant(width, height)
    assert ant.map_height() == 200
    assert ant.map_width() == 100
    assert ant.xpos() == 50
    assert ant.ypos() == 100
    ant._direction = 'up'
    ant.step(255)
    assert ant.direction() == "left"
    assert ant.xpos() == 49
    assert ant.ypos() == 100
    ant.step(255)
    assert ant.direction() == "down"
    assert ant.xpos() == 49
    assert ant.ypos() == 101
    ant.step(255)
    assert ant.direction() == "right"
    assert ant.xpos() == 50
    assert ant.ypos() == 101
    ant.step(255)
    assert ant.direction() == "up"
    assert ant.xpos() == 50
    assert ant.ypos() == 100
