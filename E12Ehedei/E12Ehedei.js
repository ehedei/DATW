window.onload = () => {
    document.getElementById('borrar').onclick = borrar;
    document.getElementById('boton').onclick = reaccionarBoton;
};


let borrar = () => {
    document.getElementById('container').innerHTML = '';
    document.getElementById('input-1').value = "";
    document.getElementById('input-2').value = "";
};

let reaccionarBoton = () => {
    let texto1 = document.getElementById('input-1').value;
    let texto2 = document.getElementById('input-2').value;
    let opcion = document.getElementById('opciones').value;

    if(texto1.length == 0 || texto2.length == 0) {
        alert("Las cadenas de texto no tienen la suficiente extensión");
    } else if (opcion == 'comparar') {
        comparar(texto1, texto2);
    } else {
        concatenar(texto1, texto2);
    }

}

let concatenar = (t1, t2) => {
    let p = document.createElement('p');
    p.append(`${t1} ${t2}`);

    document.getElementById('container').appendChild(p);
}

let comparar = (t1, t2) => {
    if (t1.length > t2.length) {
        alert(`El texto "${t1}" tiene mayor longitud (${t1.length})`);
    } else if (t1.length < t2.length) {
        alert(`El texto "${t2}" tiene mayor longitud (${t2.length})`);
    } else {
        alert(`Los textos "${t1}" y "${t1}" tienen la misma longitud (${t1length})`);
    }

}