document.querySelector('form').addEventListener('submit', function(event) {
    var email = document.querySelector('input[name="email"]').value;

    // Validación de formato de correo electrónico usando patrón HTML5
    var emailPattern = /[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$/;
    if (!emailPattern.test(email)) {
        document.querySelector('input[name="email"]').classList.add('error');
        document.getElementById('error_email_format').style.display = 'block';
        event.preventDefault(); // Evita enviar el formulario si hay errores
    } else {
        document.querySelector('input[name="email"]').classList.remove('error');
        document.getElementById('error_email_format').style.display = 'none';
    }
});