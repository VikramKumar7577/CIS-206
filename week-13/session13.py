class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"


class Patient(Person):
    def __init__(self, name, age, patient_id, illness):
        super().__init__(name, age)
        self.patient_id = patient_id
        self.illness = illness

    def get_patient_info(self):
        return (
            f"{self.get_info()}, "
            f"Patient ID: {self.patient_id}, Illness: {self.illness}"
        )


class Staff(Person):
    def __init__(self, name, age, staff_id, role):
        super().__init__(name, age)
        self.staff_id = staff_id
        self.role = role

    def work(self):
        return f"{self.name} works as {self.role}"


class Doctor(Staff):
    def __init__(self, name, age, staff_id, role, doctor_id, specialty):
        super().__init__(name, age, staff_id, role)
        self.doctor_id = doctor_id
        self.specialty = specialty

    def treat_patient(self, patient):
        return (
            f"Dr. {self.name} is treating {patient.name} "
            f"for {patient.illness}"
        )


class Procedure:
    def __init__(self, procedure_name, cost):
        self.procedure_name = procedure_name
        self.cost = cost

    def perform(self):
        return f"{self.procedure_name} costs ${self.cost}"


class Bill:
    def __init__(self, bill_id, amount):
        self.bill_id = bill_id
        self.amount = amount

    def generate_bill(self):
        return f"Bill ID: {self.bill_id}, Amount: ${self.amount}"


class Hospital:
    def __init__(self, hospital_name, location):
        self.hospital_name = hospital_name
        self.location = location

    def add_patient(self, patient):
        return (
            f"{patient.name} was added to {self.hospital_name} "
            f"in {self.location}"
        )


def main():
    patient1 = Patient("Mike Long", 25, "P101", "Flu")
    patient2 = Patient("Vik Danger", 31, "P102", "Cold")

    doctor1 = Doctor("Smith", 45, "S201", "Doctor", "D301",
                     "General Medicine")
    doctor2 = Doctor("Brown", 50, "S202", "Doctor", "D302",
                     "Cardiology")

    procedure1 = Procedure("Blood Test", 200)
    procedure2 = Procedure("X-ray", 500)

    bill1 = Bill("B401", 700)
    hospital1 = Hospital("City Hospital", "Chicago")

    print("Patient Test")
    print(patient1.get_patient_info())
    print(patient2.get_patient_info())
    print()

    print("Doctor Test")
    print(doctor1.get_info())
    print(doctor1.work())
    print(doctor1.treat_patient(patient1))
    print()

    print("Procedure Test")
    print(procedure1.perform())
    print(procedure2.perform())
    print()

    print("Bill Test")
    print(bill1.generate_bill())
    print()

    print("Hospital Test")
    print(hospital1.add_patient(patient1))
    print(hospital1.add_patient(patient2))
    print()

    print("More Object Tests")
    print(doctor2.get_info())
    print(doctor2.work())
    print(doctor2.treat_patient(patient2))


main()