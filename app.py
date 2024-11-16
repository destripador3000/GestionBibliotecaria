# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Modelos
class Prestamo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    libro = db.Column(db.String(100), nullable=False)
    usuario = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.String(10), nullable=False)

class Multa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prestamo_id = db.Column(db.Integer, db.ForeignKey('prestamo.id'), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.String(10), nullable=False)

# Crear las tablas
with app.app_context():
    db.create_all()

# Rutas
@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/registrar_prestamo', methods=['GET','POST'])
def registrar_prestamo():
    # Código para manejar el registro del préstamo
    return render_template('prestamos.html')

@app.route('/registrar_multa', methods=['GET','POST'])
def registrar_multa():
    # Código para manejar el registro del préstamo
    return render_template('multas.html')

@app.route('/informacionLibro', methods=['GET','POST'])
def mostrarInformacion():
    return render_template('informacionLibro.html')

#@app.route('/prestamos')
#def prestamo():
#    prestamos = Prestamo.query.all()
#    return render_template('prestamos.html', prestamos=prestamos)
#@app.route('/multas')
#def prestamo():
#    prestamos = Prestamo.query.all()
#    return render_template('multas.html', prestamos=prestamos)

if __name__ == '__main__':
    app.run(debug=True)
