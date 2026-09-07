// Seleccionamos el botón y agregamos un evento al formulario de login
document.getElementById('loginButton').addEventListener('click', function(event) {
    event.preventDefault();

    // Obtenemos los valores de usuario y contraseña
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Verificamos las credenciales (aquí simulamos un login simple)
    if (username === 'admin' && password === '0124') {
        // Guardamos el estado de autenticación en localStorage
        localStorage.setItem('auth', 'true');

        // Redirigimos al usuario a la página principal
        window.location.href = '/inicio';  // Redirige a la URL de la página 'Inicio.html'
    } else {
        alert('Credenciales incorrectas');
    }
});
