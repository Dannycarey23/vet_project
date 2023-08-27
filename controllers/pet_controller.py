from flask import Flask, render_template, request, redirect, Blueprint
from models.vet import Vet 
from models.pet import Pet 

import repositories.pet_repository as pet_repository

pets_blueprint = Blueprint("pets", __name__)

@pets_blueprint.route("/pets")
def index():
    pets = pet_repository.pets_view_all()
    return render_template("pets/index.html", pets=pets, title="All pets currently registered at the surgery")





