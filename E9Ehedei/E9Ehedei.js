let validar = (evento) => {
    evento.preventDefault();
    let cadena = document.getElementById('input').value;
    if (cadena.length >= 6 && cadena.includes(' ')) {
        document.getElementById('input').style.backgroundColor = 'palegreen';        
        alert("¡Cadena de texto validada!");
        
    } else {
        document.getElementById('input').style.backgroundColor = 'indianred';        
        alert("La cadena de texto no es válida.");        
    }

}

let limpiar = () => {
    document.getElementById('input').style.backgroundColor = 'white';
}


window.onload = () => {
    document.getElementById('boton').onclick = validar;
    document.getElementById('reset').onclick = limpiar;
}