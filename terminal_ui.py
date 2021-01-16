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
            print("Image path(relative to this module):")
            img_path = input("> ").strip()
        else:
            print('WRONG NUMBER TRY AGAIN')
            continue
        print('WARNING: if you use the same folder twice, the older images will be deleted permanently')
        while True:
            try:
                print("Save Folder:")
                save_dir = input("> ").strip()
                break
            except Exception:
                print('Directory does not exist, try again!')
                continue

        print('Save every step? Y/n')
        save_every_step = input('> ').strip().lower()
        if save_every_step == "n":
            break
        print('Number of steps:')
        steps = input("> ")
        break
    map = Map(width, height, creator_code, save_dir, odds_of_black, img_path)
    if save_every_step != 'n':
        map.ants_journey(steps)
    else:
        print("Sandbox Mode")
        print('The program will save images of the map after x steps')
        print('Type STOP to stop the program')
        map.save_map(save_dir, f'jump_0')
        jumps = 1
        while True:
            try:
                print("How many steps to take?")
                value = input('> ')
                if value.lower().strip() == 'stop':
                    break

                steps = int(float(value))
                print('Wait!')
                map.ants_journey(steps, save_every_step=False)
                map.save_map(save_dir, f'jump_{jumps}')
                jumps += 1
            except Exception:
                print('unsupported input, try again')
                continue

    print(f'The images are saved in {save_dir}')





if __name__ == '__main__':
    main()
