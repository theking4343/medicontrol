from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.extensions import db
from app.models import Paciente

bp_pacientes = Blueprint("pacientes", __name__)


@bp_pacientes.route("/")
def lista():
    pacientes = Paciente.query.all()
    return render_template("pacientes/lista.html", pacientes=pacientes)


@bp_pacientes.route("/crear", methods=["GET", "POST"])
def crear():
    if request.method == "POST":
        p = Paciente(nombre=request.form["nombre"],
                     telefono=request.form["telefono"])
        db.session.add(p)
        db.session.commit()
        flash("Paciente creado correctamente", "success")
        return redirect(url_for("pacientes.lista"))
    return render_template("pacientes/form.html", paciente=None)


@bp_pacientes.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    p = Paciente.query.get_or_404(id)
    if request.method == "POST":
        p.nombre = request.form["nombre"]
        p.telefono = request.form["telefono"]
        db.session.commit()
        flash("Paciente actualizado", "success")
        return redirect(url_for("pacientes.lista"))
    return render_template("pacientes/form.html", paciente=p)


@bp_pacientes.route("/eliminar/<int:id>", methods=["POST"])
def eliminar(id):
    p = Paciente.query.get_or_404(id)
    db.session.delete(p)
    db.session.commit()
    flash("Paciente eliminado", "warning")
    return redirect(url_for("pacientes.lista"))