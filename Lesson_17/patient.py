from person import Person


class Patient(Person):
    def __init__(self, first_name, last_name, id: str):
        super().__init__(first_name, last_name)

        if not isinstance(id, str):
            print("The id must be a string!")
        
        else:
            self.__id = id

    def set_id_code(self, id: str):

        if isinstance(id, str):
            self.__id = id
        
        else:
            print("Your id must be a string!")

    
    def get_id_code(self) -> str:

        return self.__id

    def patient_info(self):

        print(f"Patient: {self.first_name} {self.last_name}\nID: {self.get_id_code()}")
