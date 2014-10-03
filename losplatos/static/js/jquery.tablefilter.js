(function($) {
    $.fn.filterTable = function(options) {
        var settings = $.extend({
            texto         :  $("#FilterTextBox")
        }, options);    
                    	
    	var selector=this['selector']
    	//add index column with all content.
    	$(selector + " tr:has(td)").each(function(){
    	var t = $(this).text().toLowerCase(); //all row text
    	t=limpiar(t); 
    	$("<td class='indexColumn'></td>")
    	.hide().text(t).appendTo(this);
    	});//each tr
    	settings.texto.keyup(function(){    	 	
    		var s = $(this).val().toLowerCase().split(" ");    
    		
    		//show all rows.
    		$(selector + " tr:hidden").show();
    		if(s=="")
    			return;
    		
    		$.each(s, function(){
    			texto=limpiar(this);
    			$(selector + " tr:visible .indexColumn:not(:contains('"
    					+ texto + "'))").parent().hide();
    		});//each
    	});//key up.
        
    	function limpiar(text){
    	      var text = text; // a minusculas
    	      text = text.replace(/[áàäâå]/, 'a');
    	      text = text.replace(/[éèëê]/, 'e');
    	      text = text.replace(/[íìïî]/, 'i');
    	      text = text.replace(/[óòöô]/, 'o');
    	      text = text.replace(/[úùüû]/, 'u');
    	      text = text.replace(/[ýÿ]/, 'y');
    	      text = text.replace(/[ñ]/, 'n');
    	      text = text.replace(/[ç]/, 'c');
    	      text = text.replace(/['"]/, '');
    	      text = text.replace(/[^a-zA-Z0-9-]/, ''); 
    	      text = text.replace(/\s+/, '-');
    	      text = text.replace(/' '/, '-');
    	      text = text.replace(/(_)$/, '');
    	      text = text.replace(/^(_)/, '');
    	      return text;
    	   }    	
    	
    };
})(jQuery);