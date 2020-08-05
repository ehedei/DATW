let realizarOperaciones = (event) => {
    event.preventDefault();

    let numero1 = parseInt(document.getElementById('input-1').value);
    let numero2 = parseInt(document.getElementById('input-2').value);

    //Seria mejor usar un map para esto, pero funciona igual xD
    let operaciones = [ ['Suma', numero1 + numero2], 
                        ['Resta', numero1 - numero2],
                        ['División', numero1 / numero2],
                        ['Multiplicación', numero1 * numero2],
                        ['Potencia', Math.pow(numero1, numero2)],
                        ['Módulo', numero1 % numero2]];

    mostrarResultados(numero1, numero2, operaciones);
}

let mostrarResultados = (numero1, numero2, operaciones) => {
    let resultados = `Resultados para los números ${numero1} y ${numero2}:`;
    operaciones.forEach(element => resultados += `\n${element[0]}: ${element[1]}`);    
    alert(resultados);
}




window.onload = () => {
    document.getElementById('boton').onclick = realizarOperaciones;
}