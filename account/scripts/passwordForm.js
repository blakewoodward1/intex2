$(function() {
	console.log($('#loginform'));
	

	$('#passwordForm').ajaxForm(function(data) { 
		$('#modal_change_password').find('.modal-body').html(data);
	}); 



});