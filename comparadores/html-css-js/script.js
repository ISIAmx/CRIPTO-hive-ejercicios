const pantalla = document.getElementById('pantalla');//Obtiene parrafo donde se impirmirá
let numero1=0;
let numero2=0;

function operaciones(evento, nombreOperacion) {
    obtenerNumeros();//Obtener valores de numeros
    console.log(nombreOperacion);
    let resultado=0;

    if (nombreOperacion == 'sumar') {
        resultado = numero1 + numero2;
    }
    if (nombreOperacion == 'restar') {
        resultado = numero1 - numero2;
    }
    if (nombreOperacion == 'multiplicar') {
        resultado = numero1 * numero2;
    }
    if (nombreOperacion == 'dividir') {
        if (numero2 == 0) {
            resultado = "Operacion no permitida"
        } else {
            resultado = numero1 / numero2;
        }
    }
    pantalla.innerHTML = resultado;
}

function obtenerNumeros() {
    numero1 = document.getElementById('numero1')//Valor ingresado
    numero1 = Number(numero1.value);
    numero2 = document.getElementById('numero2')//Valor ingresado
    numero2 = Number(numero2.value);
}

