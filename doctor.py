doctors = [
    {
        'doctor id':1603,
        'name':'henry',
        'specialist':'heart surgen',
        
    },
    {
        'doctor id':1604,
        'name':'tom',
        'specialist':'neurologist',
        
    }
]
def add_doctors(doctor_id, name, specialist):
        doctors.append(
                {
                    'doctor id':doctor_id,
                    'name':name,
                    'specialist':specialist
                }
        )
        print("added doctor successfully")




def get_doctors():
        return doctors