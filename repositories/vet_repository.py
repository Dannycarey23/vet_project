from db.run_sql import run_sql
import pdb
from models.pet import Pet 
from models.vet import Vet 

def vets_view_all():
    vets = []
    sql = "SELECT * FROM vets"
    results = run_sql(sql)

    for row in results:
        vet = Vet(row['name'], row['id'])
        vets.append(vet)
    return vets


def vet_add(vet):
    sql = "INSERT INTO vets (name) VALUES (%s) RETURNING *"
    values = [vet.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    vet.id = id
    return vet


def vet_delete(id):
    sql = "DELETE FROM vets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def display_vet(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if len(results) > 0:
        result = results[0]
        vet = Vet(result['name'], result['id'])
    return vet
    

def update_vet(vet):
    sql = "UPDATE vets SET name = %s WHERE id = %s"
    values = [vet.name, vet.id]
    updated_vet = run_sql(sql, values)
    print(updated_vet)
    return updated_vet

def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)