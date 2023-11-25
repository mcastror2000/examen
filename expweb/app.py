from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'ejercicio1' in request.form:
            return render_template('formulario_ejercicio1.html')
        elif 'ejercicio2' in request.form:
            return render_template('formulario_ejercicio2.html')
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])
        precio_tarro = 9000
        total_sin_descuento = cantidad * precio_tarro

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        descuento_aplicado = int(total_sin_descuento * descuento)
        total_con_descuento = total_sin_descuento - descuento_aplicado

        return render_template('formulario_ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento, descuento=descuento_aplicado, total_con_descuento=total_con_descuento)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        if usuario == 'juan' and contrasena == 'admin':
            mensaje = 'Bienvenido administrador juan'
        elif usuario == 'pepe' and contrasena == 'user':
            mensaje = 'Bienvenido usuario pepe'
        else:
            mensaje = 'Usuario o contraseña incorrectos'

        return render_template('formulario_ejercicio2.html', mensaje=mensaje)

    return render_template('formulario_ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)
