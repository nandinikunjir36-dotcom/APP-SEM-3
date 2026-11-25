class Resident:
    def __init__(self, name, flat_number, maintenance_fee, status):
        self.name = name
        self.flat_number = flat_number
        self.maintenance_fee = maintenance_fee
        self.status = status

    def display_details(self):
        print("\nResident Name:", self.name)
        print("Flat Number:", self.flat_number)
        print("Maintenance Fee:", self.maintenance_fee)
        print("Maintenance Status:", self.status)


class Society:
    def __init__(self):
        self.residents = []

    def add_resident(self):
        name = input("Enter Resident Name: ")
        flat_number = input("Enter Flat Number: ")
        maintenance_fee = float(input("Enter Maintenance Fee: "))

        status = input("Enter Status (Paid/Pending): ")

        if status.lower() == "paid":
            status = "Paid"
        else:
            status = "Pending"

        resident = Resident(name, flat_number, maintenance_fee, status)

        self.residents.append(resident)

        print("\nResident Added Successfully!")

    
    def display_all(self):
        if len(self.residents) == 0:
            print("\nNo Resident Records Found!")
        else:
            print("\n===== APARTMENT MAINTENANCE DETAILS =====")

            for resident in self.residents:
                resident.display_details()
                print("--------------------------------")



society = Society()

while True:
    print("\n===== APARTMENT MANAGEMENT SYSTEM =====")
    print("1. Add Resident")
    print("2. Display All Maintenance Details")
    print("3. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        society.add_resident()

    elif choice == "2":
        society.display_all()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Please Try Again.")