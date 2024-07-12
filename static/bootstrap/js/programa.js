
const botonesMostrar = document.querySelectorAll(".mostrarFormulario");
const ventanaEmergente = document.getElementById("ventanaEmergente");

// Agregar un event listener a cada botón
botonesMostrar.forEach(boton => {
    boton.addEventListener("click", () => {
        ventanaEmergente.style.display = "flex"; // Mostrar la ventana emergente
    });
});

// Escuchar el evento de clic en el botón de cerrar dentro del modal
const btnCerrar = document.querySelector(".btn-danger");
btnCerrar.addEventListener("click", function() {
    ventanaEmergente.style.display = "none";
});
