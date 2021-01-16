import numpy as np
from PIL import Image
from random import randrange
from ant import Langton_Ant
import os


class ProcentageError(Exception):
    '''ProcentageError occurs when the user inputs odds
    that isn't an element of set [0, 100].
    Attributes:
    -procentage, users input
    '''
    def __init__(self, percentage):
        self.percentage = percentage
        msg = f'The percantage of black square appearing cannot be equal to {percentage}%'
        super().__init__(msg)


class StepValueError(Exception):
    '''StepValueError occurs when the user inputs some string that
    is not convertable to an integer
    Attributes:
    -string, users input
    '''
    def __init__(self, user_string):
        self.user_string = user_string
        msg = f'The number of steps cannot be equal to {user_string}'
        super().__init__(msg)


class SizeError(Exception):
    ''' SizeError class, occurs when the user inputs data that
    isn't convertable to int
    Attributes:
    -width, maps width
    -height, maps height
    '''
    def __init__(self, width, height):
        self.width = width
        self.height = height
        super().__init__(f'Size cannot be {self.width} x {self.height}')


class CreatorCodeError(Exception):
    '''CreatorCodeError, occurs when a unsupported creator_code is given
    when creating a new instance of the map class
    attributes:
    creator_code- code that was given when creating a new instance of map class
    '''
    def __init__(self, creator_code):
        self.creator_code = creator_code
        super().__init__(f'Creator code {creator_code} is not supported')


class Map():
    ''' Map class
    Attributes:
    -width
    -height
    -creator_code - to determine how the arrey should be built
    -save_dir - directory which to save the map images
    -odds_of_black - odds of black sqare, if creator_code='random'
    -img_path - relative path to the image
    '''

    _creator_codes = ['from_image', 'white', 'random']

    def __init__(
        self,
        width,
        height,
        creator_code,
        save_dir='',
        odds_of_black=None,
        img_path=None
    ):

        if creator_code == 'from_image':
            self._array = self._create_map_from_image(img_path)
            self._height, self._width = self._array.shape
        else:
            try:
                self._width = int(float(width))
                self._height = int(float(height))
                if self._width <= 0 or self._height <= 0:
                    raise SizeError(width, height)
            except Exception:
                raise SizeError(width, height)
        if creator_code == 'white':
            self._array = self._create_map_white()
        if creator_code == 'random':
            try:
                self._odds_of_black = int(float(odds_of_black))
            except ValueError:
                raise ProcentageError(odds_of_black)
            if self._odds_of_black < 0 or self._odds_of_black > 100:
                raise ProcentageError(odds_of_black)
            self._array = self._create_map_random(self._odds_of_black)

        self._ant = Langton_Ant(self._width, self._height)
        self.set_save_directory(save_dir)
        if creator_code not in self._creator_codes:
            raise CreatorCodeError(creator_code)

    def array(self):
        return self._array

    def set_save_directory(self, save_dir):
        if save_dir == '':
            save_dir = "map_photos"
        self._create_directory(save_dir)
        self._save_dir = save_dir

    def _create_directory(self, save_dir):
        '''Creates a directory, if directory already exists,
        it deletes the contents of the directory
        '''
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, save_dir)
        try:
            os.makedirs(path)
        except FileExistsError:
            filelist = [file for file in os.listdir(path) if file.endswith('.png')]
            for file in filelist:
                os.remove(os.path.join(path, file))

    def _create_map_white(self):
        shape = (self._height, self._width)
        array = np.full(shape, fill_value=255, dtype=np.dtype('uint8'))
        return array

    def _create_map_random(self, odds_of_black):
        shape = (self._height, self._width)
        array = np.full(shape, fill_value=255, dtype=np.dtype('uint8'))
        for ypos in range(self._height):
            for xpos in range(self._width):
                if self._random_bool(odds_of_black):
                    array[ypos][xpos] = 0
        return array

    def _random_bool(self, odds_of_black):
        return randrange(100) < odds_of_black

    def _create_map_from_image(self, path):
        '''Creates array from an image of a given path relative to this module
        '''
        with Image.open(f'{path}') as image:
            function = lambda x: 255 if x > 122 else 0
            image = image.convert('L').point(function, mode='1')
            image = image.convert('L')
            array = np.array(image)
            return array

    def ants_journey(self, steps, save_every_step=True):
        try:
            steps = abs(int(float(steps)))
        except Exception:
            raise StepValueError(steps)
        for step in range(0, steps+1):
            if save_every_step:
                self.save_map(step=f'step_{step}')
            ant_xpos = self._ant.xpos()
            ant_ypos = self._ant.ypos()
            self._array[ant_ypos][ant_xpos] = self._ant.step(self._array[ant_ypos][ant_xpos])

    def save_map(self, directory=None, step=None):
        '''Saves current map to a given directory
        '''
        if not directory:
            directory = self._save_dir
        # converts to '1' so less space is taken
        img = Image.fromarray(self._array, mode='L').convert(mode='1')
        img.save(f'{directory}/{step}.png')
