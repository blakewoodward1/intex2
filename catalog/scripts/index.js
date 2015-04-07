$(function() {
	$('#add_to_cart').modal({
		show: false,
	});//modal 

	

	$('.add_button').on('click', function() {
		var pid = $(this).attr('data-pid');//
		
		console.log (pid)
		
		$.loadmodal({
			url: "/catalog/shopping_cart.add/" + pid +"/" + 1,
			title: "Shopping Cart",
			width: '1000px',


		});//loadmodal



		// $("#add_to_cart").modal('show');
		// $.ajax({
		// 	url: '/catalog/shopping_cart.add/' + pid + '/' + qty,
		// 	success: function(data){
		// 		$('#add_to_cart').find('.modal-body').html('hey yall');
		// 	}//success
		// })
		//load modal
	});//click

			$('.add_product').on('click', function() {
		var pid = $(this).attr('data-pid');//
		
		console.log (pid)
		
		$.loadmodal({
			url: "/catalog/shopping_cart.add/" + pid +"/" + 1,
			title: "Shopping Cart",
			width: '1000px',


		});
	});

    //alert("Thank you for your comment!"); 
}); //ready

