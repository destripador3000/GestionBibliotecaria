# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config
from datetime import datetime
from models import Prestamo, db  # Importa db desde models.py

app = Flask(__name__)
app.config.from_object(Config)

# Usa la instancia de db ya definida en models.py
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar_prestamo', methods=['GET', 'POST'])
def registrar_prestamo():
    if request.method == 'POST':
        libro = request.form['libro']
        usuario = request.form['usuario']
        fecha = request.form['fecha']

        # Validar la fecha
        try:
            fecha = datetime.strptime(fecha, '%Y-%m-%d').date()
        except ValueError:
            flash('Fecha no válida. Usa el formato YYYY-MM-DD.', 'danger')
            return redirect(url_for('registrar_prestamo'))

        # Crear un nuevo préstamo y guardarlo en la base de datos
        nuevo_prestamo = Prestamo(libro=libro, usuario=usuario, fecha=fecha)
        db.session.add(nuevo_prestamo)
        db.session.commit()

        flash('Préstamo registrado con éxito.', 'success')
        return redirect(url_for('registrar_prestamo'))

    # Obtener todos los préstamos para mostrarlos en el template
    prestamos = Prestamo.query.all()
    return render_template('prestamos.html', prestamos=prestamos)

@app.route('/registrar_multa', methods=['GET', 'POST'])
def registrar_multa():
    if request.method == 'POST':
        flash('Multa registrada con éxito.')
        return redirect(url_for('index'))
    return render_template('multas.html')

@app.route('/informacionLibro', methods=['GET', 'POST'])
def mostrarInformacion():
    return render_template('informacionLibro.html')

@app.route('/registrarPrestamos', methods=['GET', 'POST'])
def registrarPrestamos():
    if request.method == 'POST':
        flash('Préstamo registrado con éxito.')
        return redirect(url_for('index'))
    return render_template('registrarPrestamos.html')

@app.route('/eliminarPrestamos', methods=['GET', 'POST'])
def eliminarPrestamos():
    if request.method == 'POST':
        flash('Préstamo eliminado con éxito.')
        return redirect(url_for('index'))
    return render_template('eliminarPrestamos.html')

@app.route('/consultarPrestamo', methods=['GET', 'POST'])
def consultarPrestamo():
    if request.method == 'POST':
        flash('prestamo consultado con éxito.')
        return redirect(url_for('index'))
    return render_template('consultarPrestamo.html')
@app.route('/modificarPrestamo', methods=['GET', 'POST'])
def modificarPrestamo():
    if request.method == 'POST':
        flash('Préstamo modificado con éxito.')
        return redirect(url_for('index'))
    return render_template('modificarPrestamo.html')
if __name__ == '__main__':
    app.run(debug=True)
