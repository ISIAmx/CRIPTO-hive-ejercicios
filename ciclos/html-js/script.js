function abrirSeccion(evt, nombreSeccion) {
  // Variables
  var i, contenedorContenido;

  /* Obtiene elementos de class="contenedorInfo"
  (Informacion de cada seccion) y los oculta*/
  contenedorContenido = document.getElementsByClassName("contenedorInfo");
  for (i = 0; i < contenedorContenido.length; i++) {
    contenedorContenido[i].style.display = "none";
  }
  console.log(nombreSeccion);
  // Activa el contenedor seleccionado
  document.getElementById(nombreSeccion).style.display = "block";
}


function palabraPalindroma() {
  //Obtiene el elemnto con id resultado del documento HTML
  let resultado = document.getElementById('resultado');
  //Obtiene el primer elemento input del documento HTML
  let entrada = document.getElementById('palabra');

  //Obtiene la palabra ingresada por el usuario
  let palabraIngresada = entrada.value;
  contador = 0;
  //Obtiene indice de la ultima letra de la palabra
  numLetras = palabraIngresada.length - 1;

  //Continua el ciclo hasta abarcar todos los indices de las letras
  for (i = 0; i < palabraIngresada.length; i++) {
    //Compara primera letra con última, segunda con penúltima...
    if (palabraIngresada[i] == palabraIngresada[numLetras]) {
      //Si las dos son iguales, aumenta contador
      contador++;
    }
    //Disminuye indice
    numLetras--;
  }

  let mensaje = "";
  //Si contador es igual a numero de letras de la palabra
  if (contador == palabraIngresada.length) {
    mensaje = "SÍ es palíndroma";
  } else {
    mensaje = "NO es palindroma";
  }

  return resultado.innerHTML = mensaje;
}


function generarTabla() {
  let contenedorTabla = document.getElementById('resultadoTabla')
  let texto = "";

  for (let i = 1; i <= 10; i++) {
    texto += "\n";
    for (let j = 1; j <= 10; j++) {
      //Concatena el valor de texto para ir generando la tabla
      texto = (texto + "\n" + i + " x " + j + "= " + i * j);
    }
  }

  contenedorTabla.innerHTML = texto;
}
