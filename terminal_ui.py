from map import Map


def main():

    save_dir = 'photos/default_directory'
    odds_of_black = None
    img_path = None
    width = None
    height = None

    print("Welcome to LangtonAntor")
    print("Choose how to create your map")

    while True:
        print("Type 1 to create a white map")
        print("Type 2 to create a random map")
        print("Type 3 to create a map from image")
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
            print("Odds of black squares(from 0% to 100% inclusive)")
            odds_of_black = input('> ').strip('%')
        elif creator_code_number == '3':
            creator_code = "from_image"
            print("Image path(relative to this module)")
            img_path = input("> ")
            if img_path == '':
                img_path = 'map_photos'
        else:
            print('WRONG NUMBER TRY AGAIN')
            continue

        print('WARNING: if you use the same folder twice, the older images will be deleted permanently')

        print("Save Folder(relative to this module):")
        save_dir = input("> ").strip()

        print('Do you want to save every step? Y/n')
        save_every_step = input('> ').strip().lower()

        try:
            map = Map(width, height, creator_code, save_dir, odds_of_black, img_path)
        except Exception as e:
            print(e)
            print("Restarting the program")
            continue

        if save_every_step != 'n':
            print('Number of steps:')
            steps = input("> ")
            try:
                map.ants_journey(steps)
            except Exception as e:
                print(e)
                print("Restarting the program")
                continue
        else:
            print("TIMESKIP MODE")
            print('The program will save every image of the map after each time skip')
            print('How many steps will the ant take between every time skip?')
            steps = input('> ')
            print('How many time skips will occur?')
            skips = input('> ')
            try:
                skips = abs(int(float(skips)))
            except Exception:
                print("The given value of skips is not convetable to an integer")
                print("10 skips will occur instead")
                skips = 10
            print('This might take a while')
            try:
                for skip in range(0, skips+1):
                    map.save_map(save_dir, f'skip_{skip}')
                    map.ants_journey(steps, save_every_step=False)
            except Exception as e:
                print(e)
                print("Restarting the program")
                continue
        print('Done!')
        print(f'The images are saved in {save_dir}')
        break


if __name__ == '__main__':
    main()
