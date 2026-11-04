from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.extensions import db
from app.models import Medico

bp_medicos = Blueprint("medicos", __name__)


@bp_medicos.route("/")
def lista():
    medicos = Medico.query.all()
    return render_template("medicos/lista.html", medicos=medicos)


@bp_medicos.route("/crear", methods=["GET", "POST"])
def crear():
    if request.method == "POST":
        m = Medico(nombre=request.form["nombre"],
                   especialidad=request.form["especialidad"])
        db.session.add(m)
        db.session.commit()
        flash("Médico creado correctamente", "success")
        return redirect(url_for("medicos.lista"))
    return render_template("medicos/form.html", medico=None)


@bp_medicos.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    m = Medico.query.get_or_404(id)
    if request.method == "POST":
        m.nombre = request.form["nombre"]
        m.especialidad = request.form["especialidad"]
        db.session.commit()
        flash("Médico actualizado", "success")
        return redirect(url_for("medicos.lista"))
    return render_template("medicos/form.html", medico=m)


@bp_medicos.route("/eliminar/<int:id>", methods=["POST"])
def eliminar(id):
    m = Medico.query.get_or_404(id)
    db.session.delete(m)
    db.session.commit()
    flash("Médico eliminado", "warning")
    return redirect(url_for("medicos.lista"))