from flask import Flask, render_template, request, redirect, Blueprint
from models.pet import Pet 
from models.vet import Vet
import repositories.vet_repository as vet_repository
# import repositories.pet_repository as pet_repository

vets_blueprint = Blueprint("vets", __name__)

@vets_blueprint.route("/vets")
def index():
    vets = vet_repository.vets_view_all()
    return render_template("vets/index.html", vets=vets, title="A list of all current vets")

@vets_blueprint.route("/vets", methods=['POST'])
def new_vet():
    name = request.form['name']
    vet = Vet(name)
    vet_repository.vet_add(vet)
    return redirect('/vets')

@vets_blueprint.route("/vets/<id>/delete", methods=['POST'])
def delete_a_vet(id):
    vet_repository.vet_delete(id)
    return redirect('/vets')


@vets_blueprint.route("/vets/<id>")
def show_vet(id):
    vet = vet_repository.display_vet(id)
    return render_template ("vets/show.html", vet=vet, title=vet.name)

@vets_blueprint.route("/vets/<id>/edit")
def go_to_edit(id):
    vet = vet_repository.display_vet(id)
    return render_template("vets/edit.html", vet=vet)

@vets_blueprint.route("/vets/<id>", methods=["POST"])
def edit_vet(id):
    name = request.form['name']
    my_vet = vet_repository.display_vet(id)
    vet = Vet(name, my_vet.id)
    vet_repository.update_vet(vet)
    return redirect("/vets")
