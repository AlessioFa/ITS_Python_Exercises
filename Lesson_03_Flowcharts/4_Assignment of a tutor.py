n_tutor: int = 10 
wait: int = 0

while True:
    s_number = int(input("Enter the number of the students: "))

    if n_tutor > 0:
        n_tutor -= 1
        print("Tutor assigned successfully.")
    else:
        wait += 1
        print("The student is waiting.")
    
    if n_tutor == 0 and wait > 50:
        break
    

