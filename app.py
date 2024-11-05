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
    prestamos = Prestamo.query.all()
    return render_template('index.html', prestamos=prestamos)

@app.route('/prestamos/registrar', methods=['POST'])
def registrar_prestamo():
    libro = request.form['libro']
    usuario = request.form['usuario']
    fecha = request.form['fecha']
    nuevo_prestamo = Prestamo(libro=libro, usuario=usuario, fecha=fecha)
    db.session.add(nuevo_prestamo)
    db.session.commit()
    flash('Préstamo registrado con éxito.')
    return redirect(url_for('index'))

@app.route('/prestamos/eliminar/<int:id>')
def eliminar_prestamo(id):
    prestamo = Prestamo.query.get(id)
    if prestamo:
        db.session.delete(prestamo)
        db.session.commit()
        flash('Préstamo eliminado con éxito.')
    return redirect(url_for('index'))

@app.route('/multas/crear/<int:prestamo_id>', methods=['POST'])
def crear_multa(prestamo_id):
    valor = request.form['valor']
    fecha = request.form['fecha']
    nueva_multa = Multa(prestamo_id=prestamo_id, valor=valor, fecha=fecha)
    db.session.add(nueva_multa)
    db.session.commit()
    flash('Multa creada con éxito.')
    return redirect(url_for('index'))

@app.route('/multas/eliminar/<int:id>')
def eliminar_multa(id):
    multa = Multa.query.get(id)
    if multa:
        db.session.delete(multa)
        db.session.commit()
        flash('Multa eliminada con éxito.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
