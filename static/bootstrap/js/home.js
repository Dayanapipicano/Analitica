const hamBurger = document.querySelector(".toggle-btn");

hamBurger.addEventListener("click", function () {
  document.querySelector("#sidebar").classList.toggle("expand");
});


var botonMostrar = document.getElementById("mostrarFormulario");
var ventanaEmergente = document.getElementById("ventanaEmergente");

botonMostrar.addEventListener("click", () => {
  ventanaEmergente.style.display = "flex"; // Mostrar la ventana emergente
});



const btnCerrar = document.querySelector("#formularioEmergente .btn-cerrar");

btnCerrar.addEventListener("click", function() {
    ventanaEmergente.style.display = "none";
});
