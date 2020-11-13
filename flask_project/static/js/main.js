
$(function () {
	$('#registrar').click(function () {
		nombre = $('#nombre').val();
		apellido = $('#apellido').val();
		correo = $('#correo').val();
		tel = $('#tel').val();

		if (nombre == '' || apellido == '' || correo == '' || tel == '') {
			alert("No ha llenado todos los campos!");
		} else {
			$.ajax({
				url: '/index', //URL a la cual se enviará la peticion
				type: 'POST', //Petiición POST al servidor
				dataType: "json", //Se esperan datos Json del servidor
				contentType: "application/json", //Contenido enviado: json
				data: JSON.stringify({
					nom: nombre,
					ape: apellido,
					cor: correo,
					tel: tel
				}),//Envia datos ne formato json

				success: function (data) {
					alert(data.status); //Imprime resultado en parrafo con id resultado

				},
				error: function (error) { //Si se obtiene algun error
					console.log(error);
				}
			});

		}
	});
});

