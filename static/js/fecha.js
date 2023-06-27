function setMinDate(input) {
  // Obtener el valor seleccionado en el primer input
  var fechaInicio = input.value;
  var fechaTermino = document.getElementById("id_fecha_termino");

    // Establecer el valor mínimo en el segundo input
    fechaTermino.setAttribute("min", fechaInicio);

    // Verificar si la fecha de término es menor que la fecha de inicio
    if (fechaTermino.value < fechaInicio) {
      fechaTermino.value = fechaInicio;
    }
}

window.onload = function () {
  // Obtener todos los elementos de entrada de tipo fecha
  var fechaInputs = document.querySelectorAll('input[type="date"]');

  // Obtener la fecha actual
  var fechaActual = new Date().toISOString().split('T')[0];

  // Establecer la fecha mínima en cada campo de entrada de fecha
  for (var i = 0; i < fechaInputs.length; i++) {
    fechaInputs[i].setAttribute('min', fechaActual);
  }
};
