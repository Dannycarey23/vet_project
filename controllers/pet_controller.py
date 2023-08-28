from flask import Flask, render_template, request, redirect, Blueprint
from models.vet import Vet 
from models.pet import Pet 

import repositories.pet_repository as pet_repository

pets_blueprint = Blueprint("pets", __name__)

@pets_blueprint.route("/pets")
def index():
    pets = pet_repository.pets_view_all()
    return render_template("pets/index.html", pets=pets, title="All pets currently registered at the surgery")


@pets_blueprint.route("/pets/<id>/delete", methods=['POST'])
def delete_a_pet(id):
    pet_repository.pet_delete(id)
    return redirect ('/pets')

@pets_blueprint.route("/pets/<id>", methods=['GET'])
def show_pet(id):
    pet = pet_repository.display_pet(id)
    return render_template("pets/show.html", pet=pet)
