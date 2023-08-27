from db.run_sql import run_sql

from models.pet import Pet 

def pets_view_all():
    pets = []
    sql = "SELECT * FROM pets"
    results = run_sql(sql)

    for row in results:
        pet = Pet(row['name'], row['dob'], row['type'], row['gender'], row['owners_name'], row['owners_phone'], row['treatment_notes'], row['id'])
        pets.append(pet)
    return pets