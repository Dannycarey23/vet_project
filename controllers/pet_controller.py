from flask import Flask, render_template, request, redirect, Blueprint
from models.vet import Vet 
from models.pet import Pet 

import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

pets_blueprint = Blueprint("pets", __name__)

@pets_blueprint.route("/pets")
def index():
    pets = pet_repository.pets_view_all()
    vets = vet_repository.vets_view_all()
    return render_template("pets/index.html", pets=pets, vets=vets, title="All pets currently registered at the surgery")

@pets_blueprint.route("/newpet", methods=['POST'])
def new_pet():
    name = request.form['name']
    dob = request.form['dob']
    type = request.form['type']
    gender = request.form['gender']
    owners_name = request.form['owners_name']
    owners_phone = request.form['owners_phone']
    treatment_notes = request.form['treatment_notes']
    vet = vet_repository.display_vet(request.form['vet'])

    pet = Pet(name, dob, type, gender, owners_name, owners_phone, treatment_notes, vet)
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


@pets_blueprint.route("/pets/<id>/edit")
def go_to_edit(id):
    pet = pet_repository.display_pet(id)
    return render_template("pets/edit.html", pet=pet)

@pets_blueprint.route("/pets/<id>", methods=["POST"])
def edit_pet(id):
    name = request.form['name']
    # select one vet from the db with the id
    my_pet = pet_repository.display_pet(id)
    # change the vets name property = name
    pet = Pet(name, my_pet.id)
    pet_repository.update_vet(pet)
   
    return redirect("/vets")