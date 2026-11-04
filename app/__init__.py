from flask import Flask, render_template
from config import Config
from app.extensions import db, migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app import models  # necesario para que las migraciones detecten los modelos

    from app.medicos.routes import bp_medicos
    from app.pacientes.routes import bp_pacientes
    from app.citas.routes import bp_citas

    app.register_blueprint(bp_medicos, url_prefix="/medicos")
    app.register_blueprint(bp_pacientes, url_prefix="/pacientes")
    app.register_blueprint(bp_citas, url_prefix="/citas")

    @app.route("/")
    def index():
        return render_template("index.html")

    return app