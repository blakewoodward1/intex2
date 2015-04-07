$(function() {
	$('#add_to_cart').modal({
		show: false,
	});//modal 

	

	$('.add_button').on('click', function() {
		var pid = $(this).attr('data-pid');//
		
		var qty = document.getElementsByName('qty')[0].value//1;//.val
		console.log (pid,qty)
		
		$.loadmodal({
			url: "/catalog/shopping_cart.add/" + pid +"/" + qty,
			title: "Shopping Cart",
			width: '1000px',


		});//loadmodal
	});//click
	$('.add_rental').on('click', function() {
		var pid = $(this).attr('data-pid');//
		var days = document.getElementsByName('days')[0].value
		var qty = document.getElementsByName('qty')[0].value//1;//.val
		console.log (pid,qty,days)
		
		$.loadmodal({
			url: "/catalog/shopping_cart.add/" + pid +"/" + qty + "/" + days,
			title: "Shopping Cart",
			width: '1000px',


		});//loadmodal
	});//click


    //alert("Thank you for your comment!"); 
}); //ready

