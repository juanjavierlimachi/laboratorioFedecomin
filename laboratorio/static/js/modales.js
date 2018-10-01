$("table tr td a").on("click",function(e){
		e.preventDefault()
		var urla=$(this).attr("href");  
		if (urla == '/ok/'){
			var r=$(this).attr("id");
			//alert(r);
			//window.load('/kardex/'+r);
			$.ajax({
				type:'GET',
				url:r,
				beforeSend:Espera,
				success:function(res){
					$('#FormAjax').html(res);
				}
			});
			function Espera(){
        		$("#FormAjax").html('<img src="{{STATIC_URL}}img/log.gif" id="icono"></img><br>Procesando...');
     		}
		}

		else{
			cargarFormularios(urla)
				$("#ventanas").dialog({
					modal:true,
					show:"blind",
					width: 600,
					hide:"explode",
					title:"Detalles.",
					position: "center"
				});	
		}
		
	});
cargarFormularios=function(url){
				$.ajax({
						url: url,
						type: 'GET',
						data: {}
					})
					.done(function(response) {
						$("#ventanas").html(response);
					})
					.fail(function() {
						console.log("error");
					})
					.always(function() {
						console.log("complete");
					});
			}