$(function() {
	$('#modal_change_password').modal({
		show: false,
	});//modal 

	

	$('#change_password').on('click', function() {
		
		$("#modal_change_password").modal('show');
		$.ajax({
			url: '/account/index.passwordForm',
			success: function(data){
				$('#modal_change_password').find('.modal-body').html(data);

			}//success 
		})//ajax
	});//click
    //alert("Thank you for your comment!"); 
}); //ready

