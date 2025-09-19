from doctor import Doctor
from patient import Patient

class Receipt:

    def __init__(self, patients: list, doctor: str):
        
        if doctor.is_a_validDoctor():
            
            self.patients = patients
            self.doctor = doctor
            self.receipts = len(patients)
            self.salary = 0

        else:
            self.patient =  None
            self.doctor = None
            self.receipts = None
            self.salary = None
            print("It's not possible to create the receipt class cause the doctor is not valid!")
    
    def get_salary(self) -> float:
        """Return the salary of a doctor"""
        if self.doctor is not None and self.patients is not None:
            self.salary = self.doctor.parcel * len(self.patients)
            return self.salary
        return None
    
    def get_receipt(self) -> int | None:
        """Update and return the number of patients."""
        if self.patients is not None:
            self.receipts = len(self.patients)
            return self.patients
        return None
    
    def add_patient(self, new_patient) -> str:
        """Update patient's list and the number of receipts."""
        if self.doctor is None and self.patients is None:
            print("The doctor is not valid.")
        
        else:
            self.patients.append(new_patient)

            self.get_receipt()
            self.get_salary()
            print(f"To the doctor {self.doctor.get_last_name()}'s list has benn added the patient {self.patient.get_id_code()} ")

    def remove_patient(self, id_code) -> str:

        for patient in self.patients:
            if id_code == patient.get_id_code():
                self.patients.remove(id_code)


        self.get_receipt()
        self.get_salary()

        print(f"To the doctor {self.doctor.get_last_name()}'s has been removed the patient {self.id_code} ")








    


        

