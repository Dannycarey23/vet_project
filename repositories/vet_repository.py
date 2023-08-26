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

#vets_view_all() requests all of the information on the vets table on the database and returns it into the "vets" list.

def vet_add():
    return None



def vet_delete():
    return None

def vet_update():
    return None