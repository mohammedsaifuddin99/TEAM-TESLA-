

appointed_patient =[
    {

        "patient_id" : 1122,
        "doctor_id" :1663,
        "date" : 22,
        "time" : 4 
    }
]


        
def book_appointment(patient_id, doctor_id, date , time ):
    appointed_patient.append({
        "patient_id" : patient_id,
        "doctor_id" : doctor_id,
        "date" : date,
        "time" : time
    })
    print("appointment added successfully.")





def cancel_appointment(appointment_id):
    for i in appointed_patient:
        if appointment_id == i["patient_id"]:
            appointed_patient.pop("patient_id")
            print("canceled successfully")





cancel_appointment(1122)


def appoined_patients():
    return appointed_patient
