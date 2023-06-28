fetch('https://mindicador.cl/api').then(function (response) {
    return response.json();
}).then(function (dailyIndicators) {
    document.getElementById("DolarO").innerHTML = 'Dólar $' + dailyIndicators.dolar.valor;
    // document.getElementById("DolarA").innerHTML = 'El valor actual del Dólar $' + dailyIndicators.dolar_intercambio.valor;
    document.getElementById("Euro").innerHTML = 'Euro $' + dailyIndicators.euro.valor;
}).catch(function (error) {
    console.log('Requestfailed', error);
});

// Agregar un evento de escucha para el evento "input"
function setValor(input) {
    // Obtener el valor actual del campo de entrada
    var valor = input.value;

    // Verificar si el valor comienza con "$"
    if (!valor.startsWith("$")) {
        // Agregar "$" al principio del valor
        valor = "$" + valor;

        // Asignar el nuevo valor al campo de entrada
        input.value = valor;
    }
};