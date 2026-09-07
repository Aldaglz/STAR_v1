from flask import Flask, render_template, request, redirect, url_for, flash
import subprocess

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'  # Clave secreta para los mensajes flash

# Ruta para el login
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Validar credenciales en el servidor
    if username == 'admin' and password == '0124':
        # Redirigir al inicio si las credenciales son correctas
        return redirect(url_for('inicio'))
    else:
        # Mostrar mensaje de error si las credenciales son incorrectas
        flash('Credenciales incorrectas')
        return redirect(url_for('index'))

# Ruta para la página de inicio
@app.route('/inicio')
def inicio():
    return render_template('Inicio.html')

@app.route('/sobre-nosotros')
def sobre_nosotros():
    return render_template('sobreNosotros.html')

@app.route('/robot')
def robot():
    return render_template('robot.html')

@app.route('/start_video',methods=['POST'])
def start_video():
	#Aqui se ejecuta la lógica para iniciar la captura de video
	subprocess.Popen(['python3','/home/_alda-03_/Desktop/STAR_v1/Main.py'])
	
	
@app.route('/stop_video',methods=['POST'])
def stop_video():
	#Aqui se ejecuta la lógica para detener la captura de video
	subprocess.run(['pkill','-f','/home/_alda-03_/Desktop/STAR_v1/Main.py'])
	
	
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=False)

