$(document).ready(function(){

	$('#time-start-picker').datetimepicker({			
		pickDate: false
	});

	$('#time-end-picker').datetimepicker({			
		pickDate: false
	});

	$('#date-start-picker').datetimepicker({			
		pickTime: false
	});

	$('#date-end-picker').datetimepicker({			
		pickTime: false
	});

	if($('#map').length > 0){
		$('.incidents-form').hide();
	}
});