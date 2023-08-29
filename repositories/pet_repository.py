from db.run_sql import run_sql
import pdb
from models.pet import Pet 
import repositories.vet_repository as vet_repository

def pet_add(pet):
    sql = "INSERT INTO pets (name, dob, type, gender, owners_name, owners_phone, treatment_notes, vet_id ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [pet.name, pet.dob, pet.type, pet.gender, pet.owners_name, pet.owners_phone, pet.treatment_notes, pet.vet.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    pet.id = id
    return pet

def pets_view_all():
    pets = []
    sql = "SELECT * FROM pets"
    results = run_sql(sql)

    for row in results:
        vet = vet_repository.display_vet(row['vet_id'])
        pet = Pet(row['name'], row['dob'], row['type'], row['gender'], row['owners_name'], row['owners_phone'], row['treatment_notes'], vet, row['id'])
        pets.append(pet)
    return pets

def pet_delete(id):
    sql = "DELETE FROM pets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM pets"
    run_sql(sql)

def display_pet(id):
    pet = None
    sql = "SELECT * FROM pets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if len(results) > 0:
        result = results[0]
        vet = vet_repository.display_vet(result['vet_id'])
        pet = Pet(result['name'], result['dob'], result['type'], result['gender'], result['owners_name'], result['owners_phone'], result['treatment_notes'], vet, result['id'])
    return pet

def update_pet(pet):
    sql = "UPDATE pets SET name = %s, dob = %s, type = %s, gender = %s, owners_name = %s, owners_phone = %s, treatment_notes = %s, vet_id = %s WHERE id = %s"
    values = [pet.name, pet.dob, pet.type, pet.gender, pet.owners_name, pet.owners_phone, pet.treatment_notes, pet.vet.id, pet.id]
    updated_pet = run_sql(sql, values)
    return updated_pet