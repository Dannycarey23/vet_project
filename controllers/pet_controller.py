from flask import Flask, render_template, request, redirect, Blueprint
from models.vet import Vet 
from models.pet import Pet 

import repositories.pet_repository as pet_repository

pets_blueprint = Blueprint("pets", __name__)

@pets_blueprint.route("/pets")
def index():
    pets = pet_repository.pets_view_all()
    return render_template("pets/index.html", pets=pets, title="All pets currently registered at the surgery")

@pets_blueprint.route("/newpet", methods=['POST'])
def new_pet():
    name = request.form['name']
    dob = request.form['dob']
    type = request.form['type']
    gender = request.form['gender']
    owners_name = request.form['owners_name']
    owners_phone = request.form['owners_phone']
    treatment_notes = request.form['treatment_notes']
    pet = Pet(name, dob, type, gender, owners_name, owners_phone, treatment_notes)
    pet_repository.pet_add(pet)
    return redirect("/pets")




@pets_blueprint.route("/pets/<id>/delete", methods=['POST'])
def delete_a_pet(id):
    pet_repository.pet_delete(id)
    return redirect ('/pets')

@pets_blueprint.route("/pets/<id>", methods=['GET'])
def show_pet(id):
    pet = pet_repository.display_pet(id)
    return render_template("pets/show.html", pet=pet, title=pet.name)
