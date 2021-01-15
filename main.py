from map import Map
from ant import Langton_Ant

def main():
    width = '128'
    height = '256'

    map = Map(width, height, 'random', 'map_photos', 100)
    map.ants_journey(5)


if __name__ == '__main__':
    main()
