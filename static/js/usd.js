fetch('https://mindicador.cl/api').then(function(response) {
    return response.json();
}).then(function(dailyIndicators) {
    document.getElementById("DolarO").innerHTML = 'Dólar $' + dailyIndicators.dolar.valor;
    // document.getElementById("DolarA").innerHTML = 'El valor actual del Dólar $' + dailyIndicators.dolar_intercambio.valor;
    document.getElementById("Euro").innerHTML = 'Euro $' + dailyIndicators.euro.valor;
}).catch(function(error) {
    console.log('Requestfailed', error);
});