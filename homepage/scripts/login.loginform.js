$(function() {
	console.log($('#loginform'));
	

	$('#loginform').ajaxForm(function(data) { 
	    //alert("Thank you for your comment!"); 
	   // $('#loginform_container').html(data);
	   //console.log($('#loginform_container'));
		$('#login_dialog').find('.modal-body').html(data);
	}); 





	/*console.log("world")
	//console.log($('#id_username'));
	$('#id_username').on('change', function() {
		var username = $('#id_username').val();
			$.ajax({
				url: "/index.check_username/",// + username,
				data: {
					'u': username,
				},
				type: 'POST',
				success: function(resp){
					//$('#id_username_message').remove();
					if(resp=='1'){
						$('#id_username_message').text("This is a good username");


					}else{
						$('#id_username_message').text("This username is already taken");

						//$('#id_username').after('<span id="id_username_message">Nope</span');
					}

					console.log(resp);
				}

			})
		console.log(username);



	});*/
});