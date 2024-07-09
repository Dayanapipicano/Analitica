document.getElementById('password_reset_form').addEventListener('submit', function(event) {
    var emailInput = document.getElementById('id_email');
    var errorEmailFormat = document.getElementById('error_email_format');
    var errorEmailNotFound = document.getElementById('error_email_not_found');

    // Validación de formato de correo electrónico antes de enviar el formulario
    var isValidEmailFormat = /\S+@\S+\.\S+/.test(emailInput.value);
    if (!isValidEmailFormat) {
        errorEmailFormat.style.display = 'block';
        errorEmailNotFound.style.display = 'none';  // Ocultar mensaje de correo no encontrado
        event.preventDefault();  // Evita enviar el formulario si hay errores
    } else {
        errorEmailFormat.style.display = 'none';
    }

    // Verificación de existencia del correo electrónico en la base de datos
    var url = validarEmailURL + '?email=' + emailInput.value;
    fetch(url)
        .then(response => response.json())
        .then(data => {
            if (data.exists) {
                errorEmailNotFound.style.display = 'none';
                document.getElementById('password_reset_form').submit();  // Envía el formulario si el correo existe
            } else {
                errorEmailNotFound.style.display = 'block';
            }
        })
        .catch(error => {
            console.error('Error al verificar el correo electrónico:', error);
        });

    event.preventDefault();  // Evita enviar el formulario mientras se verifica
});
