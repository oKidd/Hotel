function setMinDate(input) {
  // Obtener el valor seleccionado en el primer input
  var fechaInicio = input.value;
  var fechaTermino = document.getElementById("id_fecha_termino");

  // Calcular la fecha de término sumando 1 día a la fecha de inicio
  var minDate = new Date(fechaInicio);
  minDate.setDate(minDate.getDate() + 1);
  var minDate = minDate.toISOString().split("T")[0];

  // Establecer el valor mínimo en el segundo input
  fechaTermino.setAttribute("min", minDate);

  // Verificar si la fecha de término es menor que la fecha de inicio
  if (fechaTermino.value <= fechaInicio) {
    fechaTermino.value = minDate;
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
