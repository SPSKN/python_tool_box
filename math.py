import rectangles
import temp


def main():
    task = input(' 1 - Rectangles \n 2 - Temp Converter \n 3 - Binary Converter \n Q - Quit \n')

    while True:

        if task == "1":
            rectangles.main()
        elif task == "2":
            temp.main()
        #elif task == "3":
         #   binary.main()
        elif task == "q":
            print("Exiting.")
            break
        else:
            print("Invalid choice.")



if __name__ == "__main__":
    main()