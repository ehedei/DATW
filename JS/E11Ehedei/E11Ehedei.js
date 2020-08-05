window.onload = () => {
    document.getElementById("borrar").addEventListener('click', borrar);
    
    document.getElementById("input-2").addEventListener('change', toogleLink);
    
    document.getElementById("ocultar").addEventListener('click', ocultarImagen);
    
    document.getElementById("mostrar").addEventListener('click', mostrarImagen);

    document.getElementById("mostrarAlerta").addEventListener('click', mostrarAlerta);

    document.getElementById("cambiarColor").addEventListener('click', cambiarColorFondo);

    document.getElementById("colores").addEventListener('change', cambiarColor);
}

let borrar = () => {
    document.getElementById('input-1').value = "";
};

let toogleLink = () => {
    let checkbox = document.getElementById('input-2');
    let link = document.getElementById("link");

    if(checkbox.checked)
        link.target = "_blank";
    else
        link.target = "_self";

};

let ocultarImagen = () => {
    document.getElementById('imagen').style.visibility = 'hidden';
};

let mostrarImagen = () => {
    document.getElementById('imagen').style.visibility = 'visible';
};

let mostrarAlerta = () => {
    let texto = document.getElementById("input-3").value;
    alert(texto);
};

let cambiarColorFondo = () => {
    let color = document.getElementById('input-4').value;
    document.body.style.backgroundColor = color;
};

let cambiarColor = () => {
    let color = document.getElementById('colores').value;
    document.body.style.backgroundColor = color;
};