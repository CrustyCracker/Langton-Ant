from map import Map, SizeError, ProcentageError, StepValueError, CreatorCodeError
import numpy as np
import pytest


def test_white_map_creation():
    width = '3'
    height = '3'

    map = Map(width, height, 'white')

    assert map.array().shape == (3, 3)
    assert np.count_nonzero(map.array()) == 9


def test_create_map_white_negative_number():
    width = '11'
    height = '11'
    with pytest.raises(CreatorCodeError):
        map = Map(width, height, 'unsupported code')


def test_create_map_white_negative_number():
    width = '-3'
    height = '-37'
    with pytest.raises(SizeError):
        map = Map(width, height, 'white')


def test_create_map_white_NAN():
    width = '-3dawssd'
    height = '-3qwefds7'
    with pytest.raises(SizeError):
        map = Map(width, height, 'white')


def test_create_map_random_zero_odds():
    width = '10'
    height = '10'
    creator_code = 'random'
    odds = '0'
    map = Map(width, height, creator_code, odds_of_black=odds)
    assert np.count_nonzero(map.array()) == 100


def test_create_map_random_100_black():
    width = '10'
    height = '10'
    creator_code = 'random'
    odds = '100'
    map = Map(width, height, creator_code, odds_of_black=odds)
    assert np.count_nonzero(map.array()) == 0


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

def test_create_map_from_photo():
    width = None
    height = None
    creator_code = 'from_image'
    img_path = 'photos/cracker/CrackerHappy.png'

    map = Map(width, height, creator_code, img_path=img_path)
    assert map.array().shape == (450, 450)

def test_create_map_from_photo_nonexistant():
    width = '10'
    height = '10'
    creator_code = 'from_image'
    with pytest.raises(FileNotFoundError):
        map = Map(width, height, creator_code, '', img_path='nonexistant_PHOTO')


def test_set_save_directory():
    width = '10'
    height = '10'
    creator_code = 'white'
    map = Map(width, height, creator_code, save_dir='')
    assert map.save_dir() == 'photos/default_directory'
    map.set_save_directory('photos/default_directory/test1')
    assert map.save_dir() == 'photos/default_directory/test1'


def test_ants_journey():
    width = '3'
    height = '3'

    map = Map(width, height, 'white')

    assert map.array().shape == (3, 3)
    assert np.count_nonzero(map.array()) == 9
    map.ants_journey(1, False)
    assert map.array()[1][1] == 0


def test_ants_journey_unconvertible_number_of_steps():
    width = '3'
    height = '3'

    map = Map(width, height, 'white')

    assert map.array().shape == (3, 3)
    assert np.count_nonzero(map.array()) == 9
    map.ants_journey('1', False)
    assert map.array()[1][1] == 0
    with pytest.raises(StepValueError):
        map.ants_journey('unconvertible', False)
