from map import Map, SizeError, ProcentageError
from ant import Langton_Ant
import numpy as np
from PIL import Image
import pytest


def test_white_map_creation():
    width = '3'
    height = '3'

    map = Map(width, height, 'only_white')

    assert map._array.shape == (3, 3)
    assert np.count_nonzero(map._array) == 9


def test_create_map_white_negative_number():
    width = '-3'
    height = '-37'
    with pytest.raises(SizeError):
        map = Map(width, height, 'only_white')


def test_create_map_white_NAN():
    width = '-3dawssd'
    height = '-3qwefds7'
    with pytest.raises(SizeError):
        map = Map(width, height, 'only_white')



def test_create_map_random_zero_odds():
    width = '10'
    height = '10'
    creator_code = 'random'
    odds = '0'
    map = Map(width, height, creator_code, odds_of_black=odds)
    assert np.count_nonzero(map._array) == 100


def test_create_map_random_100_black():
    width = '10'
    height = '10'
    creator_code = 'random'
    odds = '100'
    map = Map(width, height, creator_code, odds_of_black=odds)
    assert np.count_nonzero(map._array) == 0

def test_create_map_random_NAN():
    width = '10'
    height = '10'
    creator_code = 'random'
    odds = 'ToNieJestNumer'
    with pytest.raises(ProcentageError):
        map = Map(width, height, creator_code, odds_of_black=odds)

def test_create_map_random_negative_number():
    width = '10'
    height = '10'
    creator_code = 'random'
    odds = '-125'
    with pytest.raises(ProcentageError):
        map = Map(width, height, creator_code, odds_of_black=odds)

def test_create_map_random_too_high():
    width = '10'
    height = '10'
    creator_code = 'random'
    odds = '101'
    with pytest.raises(ProcentageError):
        map = Map(width, height, creator_code, odds_of_black=odds)