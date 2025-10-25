patients = [
    {
        'patient id':36,
        'name':'jerry',
        'age':30,
        'contact':9398584431
    }
]



def register_patient(patient_id, name ,age, contact):
    patients.append(
        {
        'patient id': patient_id,
        'name':name,
        'age':age,
        'contact':contact
        }
    )
    print("successfully registerd")


register_patient(241,"kareem", 22 , 2154963287)
print(patients)



def get_patient():
    return patients

