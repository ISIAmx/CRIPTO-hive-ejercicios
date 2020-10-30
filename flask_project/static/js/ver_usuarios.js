$(function () {
    $('#visualizar').click(function () {

        $.ajax({
            url: '/users', //URL a la cual se enviará la peticion
            type: 'POST', //Petiición POST al servidor
            dataType: "json", //Se esperan datos Json del servidor
            contentType: "application/json",
            data: JSON.stringify({ click: "true" }),
            success: function (data) {
                data = JSON.stringify(data);//Convierte lista json en string json
                data = $.parseJSON(data);//Convierte stringjson en objetos js

                $("#lista_usuarios").append("<table><tr><th>Nombre</th><th>Apellido</th><th>Correo</th><th>Telefono</th></tr>");
                $(data).each(function (index, data) {
                    $("#lista_usuarios").append("<tr><td> " + data.nombre + " </td><td> " + data.apellido + " </td><td> " + data.correo + " </td><td> " + data.tel + " </td><tr>");
                });
                $("#lista_usuarios").append("</table>");

            },
            error: function (error) { //Si se obtiene algun error
                console.log(error);
            }
        });
    });
});
