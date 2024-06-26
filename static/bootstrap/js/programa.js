


var botonMostrar = document.getElementById("mostrarFormulario");
var ventanaEmergente = document.getElementById("ventanaEmergente");

botonMostrar.addEventListener("click", () => {
  ventanaEmergente.style.display = "flex"; // Mostrar la ventana emergente
});




const btnCerrar = document.querySelector(".btn-danger");

btnCerrar.addEventListener("click", function() {
    const ventanaEmergente = document.getElementById("ventanaEmergente");
    ventanaEmergente.style.display = "none";
});
