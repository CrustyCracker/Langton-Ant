from map import Map
from ant import Langton_Ant

def main():
    width = '32'
    height = '32'

    map = Map(width, height, 'from_photo', 'cracker/road', img_path='cracker/CrackerHappy.png')


    map.ants_journey(696969)


if __name__ == '__main__':
    main()
