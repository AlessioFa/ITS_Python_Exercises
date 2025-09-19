from person import Person

class Doctor(Person):
    def __init__(self, first_name: str, last_name: str, specialization: str, fee: float):
        super().__init__(first_name, last_name)

        self.__specialization = specialization
        self.__parcel = fee

        specialization_type = [
            "Pediatrician",
            "Obstetrician",
            "General Practitioner",
            "Cardiologist",
            "Dermatologist",
            "Neurologist",
            "Orthopedic Surgeon",
            "Psychiatrist",
            "Radiologist",
            "Surgeon"
            ]

        if self.__specialization not in specialization_type:
            print("The entered specialization is not valid!")
        
        else:
            self.__specialization = None

        if not isinstance(fee, float):
            print("The entered fee is not valid!")
    
    def set_specialization(self, specialization: str):
        
        if not isinstance(specialization, str):
            print("The entered specialization is not a string!")
        
        else:
            self.__specialization = specialization
        
    def set_parcel(self, parcel: float) -> float:
        
        if not isinstance(parcel, float):
            print("The entered parcel is not a float!")
        
        else:
            self.__parcel = parcel
        
    def get_specialization(self):

        return self.__specialization
    
    def parcel(self):

        return self.__parcel
    
    def is_a_validDoctor(self) -> str:

        if self.get_age() < 30:
            print(f"Doctor {self.first_name} {self.last_name} is valid!")
        
        else:
            print(f"Doctor {self.first_name} {self.last_name} is not valid!")
    
    def doctor_greet(self):

        self.greet()

        print(f"I'm a {self.getSpecialization} medic!")
    


        