$(".mi-item").removeClass("active");
$("#item-articulos").addClass("active");

$("#tabla").tablesorter({
    headers: {         
      4: {sorter:false},
      5: {sorter:false}
    }
}); 
$("#tabla").filterTable();

function getFrm(id){
	if (id==0){		    
		$("#campos_frm").load("/articulo_frm/");					  
	}else{
	 	$("#campos_frm").load("/articulo_frm/?id="+id);
	}	 
	$('#addFrm').foundation('reveal', 'open');
}  
  
function eliminarArticulo(id,desc){
	$.Zebra_Dialog('<strong>Los Platos</strong>, esta seguro de eliminar el articulo: ' + desc, {
		    'type':     'question',
		    'title':    'Pregunta del Sistema',
		    'buttons':  [
		                    {caption: 'Yes', callback: function() { 
		                    	$.get( "/articulo_delete/"+id,function(data){
		                    		var estado=$.trim(data);
		                    		if(data==1){
		                    			window.location.href='/inventario/';
		                    		}else{
		                    			new $.Zebra_Dialog('<strong>Los Platos</strong> el articulo no pudo ser eliminado.')
		                    		}
		                    	} );
		                    }},
		                    {caption: 'No'}
		                ]
		});	
}  