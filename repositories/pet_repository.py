from db.run_sql import run_sql

from models.pet import Pet 

def pet_add(pet):
    sql = "INSERT INTO pets (name, dob, type, gender, owners_name, owners_phone, treatment_notes ) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [pet.name, pet.dob, pet.type, pet.gender, pet.owners_name, pet.owners_phone, pet.treatment_notes]
    results = run_sql(sql, values)
    id = results[0]['id']
    pet.id = id
    return pet

def pets_view_all():
    pets = []
    sql = "SELECT * FROM pets"
    results = run_sql(sql)

    for row in results:
        pet = Pet(row['name'], row['dob'], row['type'], row['gender'], row['owners_name'], row['owners_phone'], row['treatment_notes'], row['id'])
        pets.append(pet)
    return pets

def pet_delete(id):
    sql = "DELETE FROM pets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def display_pet(id):
    pet = None
    sql = "SELECT * FROM pets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if len(results) > 0:
        result = results[0]
        pet = Pet(result['name'], result['dob'], result['type'], result['gender'], result['owners_name'], result['owners_phone'], result['treatment_notes'], result['id'])
    return pet
