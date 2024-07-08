document.addEventListener('DOMContentLoaded', function () {
    const messageContainer = document.getElementById('message-container');
    if (messageContainer) {
        setTimeout(function () {
            messageContainer.style.opacity = '0';
            setTimeout(function () {
                messageContainer.style.display = 'none';
            }, 500); // Tiempo adicional para la transición de opacidad
        }, 3000); // Tiempo de visualización en milisegundos
    }
});