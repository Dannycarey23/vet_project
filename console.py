from models.pet import Pet 
from models.vet import Vet

import repositories.vet_repository as vet_repository
import repositories.pet_repository as pet_repository

pet_repository.delete_all()
vet_repository.delete_all()

vet1 = Vet("Herschell")
vet_repository.vet_add(vet1)
vet2 = Vet("Radagast")
vet_repository.vet_add(vet2)
vet3 = Vet("Steve Irwin")
vet_repository.vet_add(vet3)


pet1 = Pet("Holly", "10/11/2012", "Cat", "Female", "Danny", "447123456789", "Excessive drooler", vet1)
pet_repository.pet_add(pet1)
pet2 = Pet("Layla", "14/01/2021", "Cat", "Female", "Jamie-Lee", "447987654321", "God complex;", vet2)
pet_repository.pet_add(pet2)
pet3 = Pet("Denver", "06/07/2020", "Dog", "Male", "Carol-Ann", "447135792468", "Eating disorder: Addicted to chipolatas", vet3)
pet_repository.pet_add(pet3)
pet4 = Pet("Dolly", "22/03/2019", "Dog", "Female", "Carol-Ann", "447135792468", "Runny bum", vet1)
pet_repository.pet_add(pet4)

results = pet_repository.display_pet(pet4.id)