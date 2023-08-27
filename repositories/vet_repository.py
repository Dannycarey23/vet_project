from db.run_sql import run_sql

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

# def vet_update():
#     return None