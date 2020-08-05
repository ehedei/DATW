let calcularMayor = (numero1, numero2) => {
    return (numero1 >= numero2) ? numero1 : numero2;
}

let mostrarMayor = (numero1, numero2) => {
    alert('Resultado: ' + calcularMayor(numero1, numero2));
}
                            
let calcularMayorDeTres = (numero1, numero2, numero3) => {
    let mayor;
    if (numero1 > numero2 && numero1 > numero3) {
        mayor = numero1;
    } else if (numero2 > numero1 && numero2 > numero3) {
        mayor = numero2;
    } else {
        mayor = numero3;
    }
    return mayor;
}

let mostrarNumeros = (numero) => {
    let numeros = '';
    for (let index = 0; index <= numero; index++) {
        numeros += index.toString()
        if(index != numero) {
            numeros += ' ';
        }
    }
    alert('Serie de números: \n' + numeros);

}

let mostrarNumerosInversos = (numero) => {
    let numeros = '';
    for (let index = numero; index >= 0; index--) {
        numeros += index.toString()
        if(index != 0) {
            numeros += ' ';
        }
    }
    alert('Serie inversa de números: \n' + numeros);

}

let calcularPotencia = (numero1, numero2) => {
    return Math.pow(numero1, numero2);
}

let gestionarCalcularMayor = () => {
    let numero1 = parseInt(prompt("Inserte el primer número:"));
    let numero2 = parseInt(prompt("Inserte el segundo número:"));

    if(!numero1 || !numero2) {
        alert('Uno de los números no es correcto');
    } else {
        mostrarMayor(numero1, numero2);
    }
}

let gestionarCalcularMayorDeTres = () => {
    let numero1 = parseInt(prompt("Inserte el primer número:"));
    let numero2 = parseInt(prompt("Inserte el segundo número:"));
    let numero3 = parseInt(prompt("Inserte el tercer número:"));

    if(!numero1 || !numero2 || !numero3) {
        alert('Uno de los números no es correcto');
    } else {
        alert('Resultado: ' + calcularMayorDeTres(numero1, numero2, numero3));
    }
}

let gestionarSerieDeNumerosPositivos = () => {
    let numero1 = parseInt(prompt("Inserte un número positivo:"));

    if(!numero1 || numero1 < 0) {
        alert('El número insertado no es correcto');
    } else {
       mostrarNumeros(numero1);
    }
}


let gestionarSerieDeNumerosInverso = () => {
    let numero1 = parseInt(prompt("Inserte un número positivo:"));

    if(!numero1 || numero1 < 0) {
        alert('El número insertado no es correcto');
    } else {
       mostrarNumerosInversos(numero1);
    }
}

let gestionarPotencia = () => {
    let numero1 = parseInt(prompt("Inserte el primer número:"));
    let numero2 = parseInt(prompt("Inserte el segundo número:"));

    if(!numero1 || !numero2) {
        alert('Uno de los números no es correcto');
    } else {
        alert('Resultado: ' + calcularPotencia(numero1, numero2));
    }

}


let mostrarOpciones = () => {
    let menu = `Menú
    1. Calcular el mayor de dos números
    2. Calcular el mayor de tres números
    3. Mostrar serie de números positivos
    4. Mostrar serie de números positivos de forma decreciente
    5. Calcular potencia
    6. Salir`

    let opcion;
    let salir = false;
    
    while (!salir) {
        opcion = prompt(menu);

        switch (opcion) {
            case '1':
                gestionarCalcularMayor();
                break;

            case '2':
                gestionarCalcularMayorDeTres();
                break;    

            case '3':
                gestionarSerieDeNumerosPositivos();
                break;

            case '4':
                gestionarSerieDeNumerosInverso();
                break;

            case '5':
                gestionarPotencia()
                break;    

            case '6':
                alert('Ha seleccionado salir.\n\n ¡Hasta la vista!');
                salir = true;
                break;

            default:
                    alert('Ha seleccionado un valor no válido. Por favor, vuelva a intentarlo.')
                break;
        }

    }

}

window.onload = () => {
    document.getElementById('boton').onclick = mostrarOpciones;
}