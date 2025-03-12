max_spots: int = int(input("Enter the number of all the spots: "))

free_spots: int = max_spots


max_spots: int = int(input("Enter the number of all the spots: "))
free_spots: int = max_spots

while True:
    option: str = input("Enter an option (entrance/exit/state/go out): ").lower()

    match option:
        case "entrance":
            if free_spots > 0:
                free_spots -= 1
                print(f"A vehicle has entered. Free spots remaining: {free_spots}")
            else:
                print("There are no free spots available.")

        case "exit":
            if free_spots < max_spots:
                free_spots += 1
                print(f"A vehicle has exited. Free spots remaining: {free_spots}")
            else:
                print("All spots are already available.")

        case "state":
            print(f"Free spots: {free_spots}")
            print(f"Occupied spots: {max_spots - free_spots}")

        case "go out":
            print("You are now out of the program.")
            break  

        case _:  
            print("You have to insert a valid option like 'entrance', 'exit', 'state', or 'go out'.")