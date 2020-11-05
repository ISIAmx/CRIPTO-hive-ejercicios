function opciones(event, id_seccion) {

    num_secciones = document.getElementsByClassName("seccion");
    //Oculta campos no seleccionados
    for (var i = 0; i < num_secciones.length; i++) {
        num_secciones[i].style.display = "none";
    }
    //Activa campo seleccionado
    document.getElementById(id_seccion).style.display = "block";
}

//Se activa si se selecciona Modificar
function activar_contenedor(event, cont) {
    document.getElementById(cont).style.display = "block";
}

// Variable global para guardar el id del usuario a borrar si fuera necesario
id_borrar = 0;

$(function () {
    //Buscar por nombre
    $('#btn1').click(function () {
        nombre = $('#nom').val();

        $.ajax({
            url: '/buscar_usuario', //URL a la cual se enviará la peticion
            type: 'POST', //Petiición POST al servidor
            dataType: "json", //Se esperan datos Json del servidor
            contentType: "application/json",
            data: JSON.stringify({
                nom: nombre,
                op: "1",
            }),
            success: function (data) {
                data = JSON.stringify(data);//Convierte lista json en string json
                data = $.parseJSON(data);//Convierte string json en objetos js
                //Imprime en los campos los datos del usuario buscado
                $(data).each(function (index, data) {
                    $("#resultado").text(data.nombre + "--" + data.apellido + "--" + data.correo);
                    $("#cont-nombre").val(data.nombre);
                    $("#cont-apellido").val(data.apellido);
                    $("#cont-correo").val(data.correo);
                    $("#cont-telefono").val(data.tel);
                    id_borrar = data.id; //guarda id de usuario obtenido para borrarlo si es necesario
                });
            },
            error: function (error) { //Si se obtiene algun error
                console.log(error);
            }
        });
    });

    //Buscar por apellido
    $('#btn2').click(function () {
        apellido = $('#ape').val();

        $.ajax({
            url: '/buscar_usuario', //URL a la cual se enviará la peticion
            type: 'POST', //Petiición POST al servidor
            dataType: "json", //Se esperan datos Json del servidor
            contentType: "application/json",
            data: JSON.stringify({
                ape: apellido,
                op: "2",
            }),
            success: function (data) {
                data = JSON.stringify(data);//Convierte lista json en string json
                data = $.parseJSON(data);//Convierte string json en objetos js
                //Imprime en los campos los datos del usuario buscado
                $(data).each(function (index, data) {
                    $("#resultado").text(data.nombre + "--" + data.apellido + "--" + data.correo);
                    $("#cont-nombre").val(data.nombre);
                    $("#cont-apellido").val(data.apellido);
                    $("#cont-correo").val(data.correo);
                    $("#cont-telefono").val(data.tel);
                    id_borrar = data.id; //guarda id de usuario obtenido para borrarlo si es necesario
                });

            },
            error: function (error) { //Si se obtiene algun error
                console.log(error);
            }
        });
    });

    //Buscar por correo
    $('#btn3').click(function () {
        correo = $('#cor').val();

        $.ajax({
            url: '/buscar_usuario', //URL a la cual se enviará la peticion
            type: 'POST', //Petiición POST al servidor
            dataType: "json", //Se esperan datos Json del servidor
            contentType: "application/json",
            data: JSON.stringify({
                cor: correo,
                op: "3",
            }),
            success: function (data) {
                data = JSON.stringify(data);//Convierte lista json en string json
                data = $.parseJSON(data);//Convierte string json en objetos js
                //Imprime en los campos los datos del usuario buscado
                $(data).each(function (index, data) {
                    $("#resultado").text(data.nombre + "--" + data.apellido + "--" + data.correo);
                    $("#cont-nombre").val(data.nombre);
                    $("#cont-apellido").val(data.apellido);
                    $("#cont-correo").val(data.correo);
                    $("#cont-telefono").val(data.tel);
                    id_borrar = data.id; //guarda id de usuario obtenido para borrarlo si es necesario
                });
            },
            error: function (error) { //Si se obtiene algun error
                console.log(error);
            }
        });
    });

    //Borra usuario de la base de datos
    $('#borrar-usuario').click(function () {

        $.ajax({
            url: '/borrar_usuario', //URL a la cual se enviará la peticion
            type: 'POST', //Petiición POST al servidor
            dataType: "json", //Se esperan datos Json del servidor
            contentType: "application/json",
            data: JSON.stringify({
                id: id_borrar, //Envía id del usuario a borrar
            }),
            success: function (data) {
                alert(data.status) //Muestra mensaje del servidor
            },
            error: function (error) { //Si se obtiene algun error
                console.log(error);
            }
        });
    });
});

