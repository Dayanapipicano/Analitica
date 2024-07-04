document.querySelector('form').addEventListener('submit', function(event) {
    var password1 = document.getElementById('id_new_password1').value;
    var password2 = document.getElementById('id_new_password2').value;
    
    // Validación de longitud mínima
    if (password1.length < 8) {
        document.getElementById('id_new_password1').classList.add('error');
        document.getElementById('error_new_password1_length').style.display = 'block';
        event.preventDefault(); // Evita enviar el formulario si hay errores
    } else {
        document.getElementById('id_new_password1').classList.remove('error');
        document.getElementById('error_new_password1_length').style.display = 'none';
    }
    
    // Validación de contraseñas coincidentes
    if (password1 !== password2) {
        document.getElementById('id_new_password2').classList.add('error');
        document.getElementById('error_new_password_match').style.display = 'block';
        event.preventDefault(); // Evita enviar el formulario si hay errores
    } else {
        document.getElementById('id_new_password2').classList.remove('error');
        document.getElementById('error_new_password_match').style.display = 'none';
    }
});