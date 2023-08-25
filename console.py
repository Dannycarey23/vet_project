import pdb
from models.pet import Pet 
from models.vet import Vet

vet1 = Vet("Herschell")
vet2 = Vet("Radagast")
vet3 = Vet("Steve Irwin")

pet1 = Pet("Holly", "10/11/2012", "Cat", "Female", "Danny", 07123456789, "Excessive drooler")
pet2 = Pet("Layla", "14/01/2021", "Cat", "Female", "Jamie-Lee", 07987654321, "God complex;")
pet3 = Pet("Denver", "06/07/2020", "Dog", "Male", "Carol-Ann", 07135792468, "Eating disorder: Addicted to chipolatas")
pet4 = Pet("Dolly", "22/03/2019", "Dog", "Female", "Carol-Ann", 07135792468, "Runny bum")

pdb.set_trace()