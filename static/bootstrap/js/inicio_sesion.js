document.querySelector('form').addEventListener('submit', function(event) {
    var password = document.querySelector('input[name="password"]').value;

    // Validación de longitud mínima
    if (password.length < 8) {
        document.querySelector('input[name="password"]').classList.add('error');
        document.getElementById('error_password_length').style.display = 'block';
        event.preventDefault(); // Evita enviar el formulario si hay errores
    } else {
        document.querySelector('input[name="password"]').classList.remove('error');
        document.getElementById('error_password_length').style.display = 'none';
    }
});