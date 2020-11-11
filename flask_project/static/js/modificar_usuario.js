
$(function () {
    //Modificar Usuario
    $('#btn-modificar').click(function () {
        let num_id = localStorage.getItem("var_compartida");
        id_mod = Number(num_id);

        nombre = $('#mod-nombre').val();
        apellido = $('#mod-apellido').val();
        correo = $('#mod-correo').val();
        tel = $('#mod-telefono').val();

        $.ajax({
            url: '/modificar_usuario', //URL a la cual se enviará la peticion
            type: 'POST', //Petiición POST al servidor
            dataType: "json", //Se esperan datos Json del servidor
            contentType: "application/json",
            data: JSON.stringify({
                id: id_mod,
                nom: nombre,
                ape: apellido,
                cor: correo,
                tel: tel,
            }),
            success: function (data) {
                alert(data.status);
            },
            error: function (error) { //Si se obtiene algun error
                console.log(error);
            }
        });
    });
})