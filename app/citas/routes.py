from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.extensions import db
from app.models import Cita, Medico, Paciente

bp_citas = Blueprint("citas", __name__)


def _leer_form(c):
    c.fecha = datetime.strptime(request.form["fecha"], "%Y-%m-%d").date()
    c.hora = datetime.strptime(request.form["hora"], "%H:%M").time()
    c.medico_id = int(request.form["medico_id"])
    c.paciente_id = int(request.form["paciente_id"])


@bp_citas.route("/")
def lista():
    citas = Cita.query.order_by(Cita.fecha, Cita.hora).all()
    return render_template("citas/lista.html", citas=citas)


@bp_citas.route("/crear", methods=["GET", "POST"])
def crear():
    if request.method == "POST":
        c = Cita()
        _leer_form(c)
        db.session.add(c)
        db.session.commit()
        flash("Cita registrada", "success")
        return redirect(url_for("citas.lista"))
    return render_template("citas/form.html", cita=None,
                           medicos=Medico.query.all(),
                           pacientes=Paciente.query.all())


@bp_citas.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    c = Cita.query.get_or_404(id)
    if request.method == "POST":
        _leer_form(c)
        db.session.commit()
        flash("Cita actualizada", "success")
        return redirect(url_for("citas.lista"))
    return render_template("citas/form.html", cita=c,
                           medicos=Medico.query.all(),
                           pacientes=Paciente.query.all())


@bp_citas.route("/eliminar/<int:id>", methods=["POST"])
def eliminar(id):
    c = Cita.query.get_or_404(id)
    db.session.delete(c)
    db.session.commit()
    flash("Cita eliminada", "warning")
    return redirect(url_for("citas.lista"))