from random import choice


class Langton_Ant():
    '''Ant class, Atributes:
    -map_width- map width; int
    -map_height- map height; int
    -xpos- ants x-axis position on the map; int
    -ypos- ants y-axis position on the map; int
    -direction: up, right, down, left; string
    '''

    colors = {"black": 0, "white": 255}

    def __init__(self, map_width, map_height):

        self._map_widht = int(float(map_width))
        self._map_height = int(float(map_height))

        self._xpos = int(self._map_widht/2)
        self._ypos = int(self._map_height/2)

        self._direction = self._new_direction_random()

    def xpos(self):
        return self._xpos

    def ypos(self):
        return self._ypos

    def map_height(self):
        return self._map_height

    def map_width(self):
        return self._map_widht

    def direction(self):
        return self._direction

    def set_direction(self, direction):
        self._direction = direction

    def _go_up(self):
        self._ypos -= 1

    def _go_right(self):
        self._xpos += 1

    def _go_down(self):
        self._ypos += 1

    def _go_left(self):
        self._xpos -= 1

    def step(self, color):
        '''Changes ants direction to a legal one and makes the ant
        take a step in that direction.
        Returns the value of a color that the square of the map
        will take.
        '''
        if self.map_height() == 1 and self.map_width() == 1:
            if color == self.colors['black']:
                return self.colors['white']
            if color == self.colors['white']:
                return self.colors['black']

        self.set_direction(self._new_direction(color))
        illegal_directions = self._get_illegal_directions()
        if self.direction() in illegal_directions:
            self.set_direction(self._new_direction_random(illegal_directions))
        self._change_pos()

        if color == self.colors["black"]:
            return self.colors["white"]
        if color == self.colors["white"]:
            return self.colors["black"]

    def _change_pos(self):
        if self.direction() == 'up':
            self._go_up()
        if self.direction() == "right":
            self._go_right()
        if self.direction() == "down":
            self._go_down()
        if self.direction() == "left":
            self._go_left()

    def _get_illegal_directions(self):
        '''Returns a list of illegal directions that would make the
        ant go off the map
        '''
        illegal_directions = []
        if self.xpos() == 0:
            illegal_directions.append('left')
        if self.xpos() == self.map_width() - 1:
            illegal_directions.append('right')
        if self.ypos() == 0:
            illegal_directions.append('up')
        if self.ypos() == self.map_height() - 1:
            illegal_directions.append('down')
        return illegal_directions

    def _new_direction(self, color):
        '''changes ants' direction depending on the color of
        the square that the ant is on
        '''
        if color == self.colors['black']:
            if self.direction() == 'up':
                return 'right'
            if self.direction() == 'right':
                return 'down'
            if self.direction() == 'down':
                return 'left'
            if self.direction() == 'left':
                return 'up'
        if color == self.colors['white']:
            if self.direction() == 'up':
                return 'left'
            if self.direction() == 'left':
                return 'down'
            if self.direction() == 'down':
                return 'right'
            if self.direction() == 'right':
                return 'up'

    def _new_direction_random(self, illegal_directions=[]):
        '''Returns a random direction that is legal
        Takes a list of illegal directions as the argument
        '''
        legal_directions = ['up', 'right', 'down', 'left']
        if not illegal_directions == []:
            for direction in illegal_directions:
                legal_directions.remove(direction)
        return choice(legal_directions)
