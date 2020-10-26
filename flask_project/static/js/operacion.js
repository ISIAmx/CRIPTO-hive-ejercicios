$(function(){
	$('button').click(function(){
		$.ajax({
			url: '/index', //URL a la cual se enviará la peticion
			type: 'POST', //Petiición POST al servidor
			dataType: "json", //Se esperan datos Json del servidor
         
			data: $('form').serialize(), //Envia todos los datos del form	

			success: function(data){
				$("#resultado").text(data.resultado); //Imprime resultado en parrafo con id resultado
                
			},
			error: function(error){ //Si se obtiene algun error
				console.log(error);
			}
		});
	});
});