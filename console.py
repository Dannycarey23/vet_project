import pdb
from models.pet import Pet 
from models.vet import Vet

import repositories.vet_repository as vet_repository
import repositories.pet_repository as pet_repository

vet1 = Vet("Herschell")
vet_repository.vet_add(vet1)
vet2 = Vet("Radagast")
vet_repository.vet_add(vet2)
vet3 = Vet("Steve Irwin")
vet_repository.vet_add(vet3)

pet1 = Pet("Holly", "10/11/2012", "Cat", "Female", "Danny", "447123456789", "Excessive drooler")
pet_repository.pet_add(pet1)
pet2 = Pet("Layla", "14/01/2021", "Cat", "Female", "Jamie-Lee", "447987654321", "God complex;")
pet_repository.pet_add(pet2)
pet3 = Pet("Denver", "06/07/2020", "Dog", "Male", "Carol-Ann", "447135792468", "Eating disorder: Addicted to chipolatas")
pet_repository.pet_add(pet3)
pet4 = Pet("Dolly", "22/03/2019", "Dog", "Female", "Carol-Ann", "447135792468", "Runny bum")
pet_repository.pet_add(pet4)

