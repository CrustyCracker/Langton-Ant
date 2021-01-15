from map import Map
from ant import Langton_Ant

def main():

    save_dir = 'map_photos'
    odds_of_black = None
    img_path = None
    width = None
    height = None
    print("Langtons Ant photo creator")
    print("Choose how to create your map")
    while True:
        print("Type 1 to create a white map")
        print("Type 2 to create a random map")
        print("Type 3 to create a map from a photo")
        creator_code_number = input('> ')
        if creator_code_number == '1':
            creator_code = "white"
            print("map width:")
            width = input("> ")
            print("map height:")
            height = input("> ")
        elif creator_code_number == '2':
            creator_code = "random"
            print("map width:")
            width = input("> ")
            print("map height:")
            height = input("> ")
            print("Odds of black squares")
            odds_of_black = input('> ')
        elif creator_code_number == '3':
            creator_code = "from_photo"
            print("Photo path:")
            img_path = input("> ")
        else:
            print('WRONG NUMBER TRY AGAIN')
            continue
        print("Save Directory:")
        save_dir = input("> ")
        print('Number of steps:')
        steps = input("> ")
        break

    map = Map(width, height, creator_code, save_dir, odds_of_black, img_path)
    map.ants_journey(steps)




if __name__ == '__main__':
    main()
