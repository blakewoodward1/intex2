$(function() {
	//console.log($('#loginform'));
	$('#login_dialog').modal({
		show: false,


	});//modal
 

	$('#show_login_dialog').on('click', function() {
		$("#login_dialog").modal('show');
		$.ajax({
			url: '/homepage/login.loginform',
			success: function(data){
				$('#login_dialog').find('.modal-body').html(data);

			}//success
		})//ajax
	});//click
    //alert("Thank you for your comment!"); 

	$('#add_button').on('click', function() {
	
		$.loadmodal({
			url: "/catalog/shopping_cart",//.add/" + pid +"/" + qty,
			title: "Shopping Cart",
			width: '1000px',


		});//loadmodal

		//load modal
	});//click

$('#keywordBtn').on('click', function() {
	
		var keywords = document.getElementById('keywords').value
		console.log(keywords)

		window.location.href = "/catalog/index.query/"+keywords;
		//load modal
	});//click




}); //ready
















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
