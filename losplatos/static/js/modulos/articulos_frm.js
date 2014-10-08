$(document).foundation();

$("#formulario").on('valid',function (){
  	$("#btn_save").attr('disabled','disabled');
	var postData = $(this).serializeArray();
	var formURL = $(this).attr("action");
	$.ajax({
	    url : formURL,
	    type: "POST",
	    data : postData,
	    success:function(data, textStatus, jqXHR){
	    	$("#btn_save").removeAttr('disabled');  
	        $('#addFrm').foundation('reveal', 'close');
	        window.location.href="/inventario/"
	    },
	    error: function(jqXHR, textStatus, errorThrown) {
	    	console.log(errorThrown);   
		}
	});
	return false;
}); 