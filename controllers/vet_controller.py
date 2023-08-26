from flask import Flask, render_template, request, redirect, Blueprint
from models.pet import Pet 
from models.vet import Vet
import repositories.vet_repository as vet_repository
import repositories.pet_repository as pet_repository

vets_blueprint = Blueprint("vets", __name__)

@vets_blueprint.route("/vets")
def vets():
    vets = vet_repository.vets_view_all()
    return render_template("vets/index.html", vets=vets)

@vets_blueprint.route("/newvet", methods=['POST'])
def new_vet():
    name = request.form['name']
    vet = Vet(name)
    vet_repository.vet_add(vet)
    return redirect('/vets/index.html')

@vets_blueprint.route("/vets/<id>/delete", methods=['POST'])
def delete_a_vet(id):
    vet_repository.vet_delete(id)
    return redirect('/books')