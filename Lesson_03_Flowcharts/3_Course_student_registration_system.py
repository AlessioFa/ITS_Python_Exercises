course_name: str = input("Enter the name of a course: ")

max_spots: int = 100


while True: 


    option: str = input("Enter one option between subscribe/cancel/view/delete/exit : ").lower()

    if option == "subscribe":
        if max_spots > 0:
           max_spots += 1
        else:
            print("There are not aviable spots.")
    
    elif option == "cancel":
        if max_spots < 100:
           max_spots += 1
        else:
            print("All the spots are already aviable.")
    
    elif option == "view":
        print(f"These are all the spots: {max_spots}")
        print(max_spots - 100)

    elif option == "delete":
        deleted_course = input("Enter the name of the course to delete: ")
        print(f"{deleted_course} has been deleted")
        continue
    
    else:
        option == "exit"
        print("You are now out of the program.")
        break
