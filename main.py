from doctor import add_doctors, get_doctors
from patient import register_patient,get_patient
from appointment import book_appointment, appoined_patients,cancel_appointment

def show_menu():
    print('''
        1. Add Doctor

        2. Register Patient

        3. Book Appointment

        4. Cancel Appointment

        5. View Doctor's Schedule

        6. View Patient History

        7. Generate Daily Appointment

        8. Check Doctor Availability

        9. View All Appointments

        10.Exit
''' )
    
def main():
    while True:
        show_menu()
        choice = input('Enter your choice:')
        if choice == '1':
          doctor_id = int(input("Enter ur id:")) 
          name = input("Enter ur name:") 
          specialist = input("Enter ur speaciliaty:")
          add_doctors(doctor_id,name,specialist)
        elif choice == '2':
            patient_id = int(input("enter ur id:"))
            name = input("enter ur name:")
            age = int(input("enter ur age:"))
            contact = int(input("enter ur contact number"))
            register_patient(patient_id, name , age , contact)
        elif choice == "3":
            patient_id = int(input("enter ur patient  id:"))
            doctor_id = int(input("Enter doctor id:"))
            date = int(input("enter your date for appoinment "))
            time = input("enter ur time : ")
            book_appointment(patient_id,doctor_id,date,time)
        elif choice == "4":
            appointment_id = int(input("enter ur appointment id"))
            cancel_appointment(appointment_id)
        else:
            print("not available...")

if __name__ == '__main__':
    main()
    


