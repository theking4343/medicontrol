from datetime import date, time
from app import create_app
from app.extensions import db
from app.models import Medico, Paciente, Cita

app = create_app()

with app.app_context():
    medicos = [
        Medico(nombre="Dr. Carlos Mendoza", especialidad="Cardiología"),
        Medico(nombre="Dra. Lucía Rojas", especialidad="Pediatría"),
        Medico(nombre="Dr. Andrés Quispe", especialidad="Traumatología"),
    ]
    pacientes = [
        Paciente(nombre="Juan Pérez", telefono="70011223"),
        Paciente(nombre="María Gómez", telefono="71122334"),
        Paciente(nombre="Pedro Condori", telefono="72233445"),
    ]
    db.session.add_all(medicos + pacientes)
    db.session.commit()

    citas = [
        Cita(fecha=date(2026, 11, 10), hora=time(9, 0), medico_id=medicos[0].id, paciente_id=pacientes[0].id),
        Cita(fecha=date(2026, 11, 10), hora=time(10, 30), medico_id=medicos[1].id, paciente_id=pacientes[1].id),
        Cita(fecha=date(2026, 11, 11), hora=time(15, 0), medico_id=medicos[2].id, paciente_id=pacientes[2].id),
    ]
    db.session.add_all(citas)
    db.session.commit()
    print("Datos de prueba insertados")