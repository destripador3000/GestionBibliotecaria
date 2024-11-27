# models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Prestamo(db.Model):
    __tablename__ = 'prestamos'

    id = db.Column(db.Integer, primary_key=True)
    libro = db.Column(db.String(150), nullable=False)
    usuario = db.Column(db.String(150), nullable=False)
    fecha = db.Column(db.Date, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<Prestamo {self.libro} - {self.usuario}>"

class Multa(db.Model):
    __tablename__ = 'multas'

    id = db.Column(db.Integer, primary_key=True)
    libro = db.Column(db.String(150), nullable=False)
    usuario = db.Column(db.String(150), nullable=False)
    codigo = db.Column(db.String(50), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Multa {self.libro} - {self.usuario}>"
